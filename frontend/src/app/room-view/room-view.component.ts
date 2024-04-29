import { Component, OnInit } from '@angular/core';
import { Route } from '@angular/router';
import { RoomViewService } from '../room-view.service';
import { of, Observable } from 'rxjs';
import { RoomDetails, SeatDetails } from './room-view.models';
import { NgForm } from '@angular/forms';
import { filter, map } from 'rxjs/operators';
import { startWith } from 'rxjs/operators';
import { MatDialog } from '@angular/material/dialog';
import { SeatDetailsModalComponent } from '../seat-details-modal-component/seat-details-modal-component.component';
import { Seat } from '../coworking/coworking.models';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-room-view',
  templateUrl: './room-view.component.html',
  styleUrls: ['./room-view.component.css']
})
export class RoomViewComponent implements OnInit {
  public static Route: Route = {
    path: 'room-view',
    component: RoomViewComponent,
    title: 'TarPaws Adoption Center'
  };
  rooms$!: Observable<RoomDetails[]>;
  displayedRoomColumns: string[] = [
    'building',
    'id',
    'room',
    'nickname',
    'capacity',
    'reservable',
    'seats',
    'whiteboard',
    'projector',
    'monitor'
  ];
  seats$!: Observable<SeatDetails[]>;
  displayedSeatColumns: string[] = [
    'title',
    'shorthand',
    'id',
    'room_id',
    'room_nickname',
    'reservable',
    'has_monitor',
    'sit_stand',
    'x',
    'y'
  ];
  newRoom: RoomDetails = {
    id: '',
    nickname: '',
    building: '',
    room: '',
    capacity: 0,
    reservable: false,
    seats: [],
    has_projector: false,
    has_whiteboard: false,
    has_monitor: false
  };
  newSeat: SeatDetails = {
    id: 0,
    title: '',
    shorthand: '',
    reservable: false,
    has_monitor: false,
    sit_stand: false,
    x: 0,
    y: 0,
    room: { id: '', nickname: '' }
  };
  tempRoomId: string = '';
  tempRoomNickname: string = '';
  selectedRoomId: string = '';
  currentRoom: RoomDetails | null = null;

  dogPhotoUrl: string = '';

  constructor(
    private roomViewService: RoomViewService,
    public dialog: MatDialog,
    private http: HttpClient
  ) {}

  ngOnInit(): void {
    this.rooms$ = this.roomViewService.getRooms().pipe(
      map((rooms) =>
        rooms.map((room) => ({
          ...room,
          gridWidth: Math.max(...room.seats.map((seat) => seat.x), 0) + 1,
          gridHeight: Math.max(...room.seats.map((seat) => seat.y), 0) + 1,
          seats: room.seats.map((seat) => ({
            ...seat,
            y: 10 - seat.y // Assuming the maximum y value is 9 (since we start from 0)
          }))
        }))
      ),
      startWith([] as RoomDetails[])
    );

    this.seats$ = this.roomViewService.getSeats().pipe(
      filter((data) => !!data),
      startWith([] as SeatDetails[])
    );

    this.rooms$.subscribe((rooms) => {
      if (!this.selectedRoomId && rooms.length > 0) {
        this.selectedRoomId = rooms[0].id;
        this.onRoomSelected();
      }
    });

    this.loadRandomDogPhoto();
  }

  loadRandomDogPhoto() {
    const apiUrl = 'https://api.thedogapi.com/v1/images/search?limit=1';

    this.http.get<any[]>(apiUrl).subscribe(
      (response: any[]) => {
        if (response.length > 0 && response[0].url) {
          this.dogPhotoUrl = response[0].url;
        } else {
          console.error('Invalid response from dog photo API');
        }
      },
      (error) => {
        console.error('Error fetching dog photo:', error);
      }
    );
  }

  onSubmitRoom(form: NgForm): void {
    if (form.valid) {
      this.roomViewService
        .addRoom(this.newRoom)
        .subscribe((success: boolean) => {
          if (success) {
            form.resetForm();
            this.loadRooms();
          }
        });
    }
  }
  showSeatDetails(seat: Seat): void {
    const dialogRef = this.dialog.open(SeatDetailsModalComponent, {
      width: '400px',
      data: seat
    });

    dialogRef.afterClosed().subscribe((result) => {
      console.log('The seat details modal was closed');
    });
  }

  onSubmitSeat(form: NgForm): void {
    if (form.valid) {
      this.roomViewService.getRoomById(this.tempRoomId).subscribe(
        (room) => {
          if (room) {
            this.newSeat.room = {
              id: this.tempRoomId,
              nickname: room.nickname
            };

            this.roomViewService.addSeat(this.newSeat).subscribe((success) => {
              if (success) {
                form.resetForm();
                this.loadSeats();
                this.loadRooms();
              }
            });
          } else {
            console.error('Room not found with ID:', this.tempRoomId);
          }
        },
        (error) => {
          console.error('Error fetching room:', error);
        }
      );
    }
  }

  deleteRoom(roomId: string): void {
    this.roomViewService.deleteRoom(roomId).subscribe((success) => {
      if (success) {
        this.loadRooms();
        this.loadSeats();
      }
    });
  }

  deleteSeat(seatId: number): void {
    this.roomViewService.deleteSeat(seatId).subscribe({
      next: (success) => {
        console.log('Delete seat successful:', success);
        this.loadSeats();
        this.loadRooms();
      },
      error: (error) => {
        console.error('Error deleting seat:', error);
      },
      complete: () => {
        console.log('Delete seat operation completed');
      }
    });
  }

  private loadRooms(): void {
    console.log('Loading rooms...');
    this.rooms$ = this.roomViewService.getRooms();
  }
  private loadSeats(): void {
    console.log('Loading seats...');
    this.seats$ = this.roomViewService.getSeats();
  }

  onRoomSelected(): void {
    if (this.selectedRoomId) {
      this.loadSeatsAndGrid(this.selectedRoomId);
    }
  }

  private loadSeatsAndGrid(roomId: string): void {
    this.roomViewService.getRoomById(roomId).subscribe(
      (room) => {
        if (room) {
          this.currentRoom = room;
          this.currentRoom.gridWidth =
            Math.max(...room.seats.map((seat) => seat.x), 0) + 1;
          this.currentRoom.gridHeight =
            Math.max(...room.seats.map((seat) => seat.y), 0) + 1;

          this.currentRoom.seats = room.seats.map((seat) => ({
            ...seat,
            y: seat.y // Assuming the maximum y value is 9 (since we start from 0)
          }));
        } else {
          console.error('Room not found with ID:', roomId);
        }
      },
      (error) => {
        console.error('Error fetching room:', error);
      }
    );
  }
}
