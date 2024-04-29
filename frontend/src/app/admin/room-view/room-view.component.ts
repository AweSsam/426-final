import { Component, OnInit } from '@angular/core';
import { permissionGuard } from 'src/app/permission.guard';
import { RoomViewService } from './room-view.service';
import { SeatDetails, RoomDetails } from 'src/app/room-view/room-view.models';
import { Observable, filter, startWith } from 'rxjs';
import { NgForm } from '@angular/forms';

@Component({
  selector: 'app-room-view',
  templateUrl: './room-view.component.html',
  styleUrls: ['./room-view.component.css']
})
export class RoomViewComponent implements OnInit {
  public static Route = {
    path: 'room-view',
    component: RoomViewComponent,
    title: 'Dogs & Enclosures',
    canActivate: [
      permissionGuard('room.list', 'rooms/'),
      permissionGuard('seat.list', 'seats/')
    ]
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
    'monitor',
    'deleteRoom'
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
    'y',
    'deleteSeat'
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

  constructor(private roomViewService: RoomViewService) {}

  ngOnInit(): void {
    this.seats$ = this.roomViewService.getSeats().pipe(
      filter((data) => !!data),
      startWith([] as SeatDetails[])
    );

    this.rooms$ = this.roomViewService.getRooms().pipe(
      filter((data) => !!data),
      startWith([] as RoomDetails[])
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

  onSubmitSeat(form: NgForm): void {
    if (form.valid) {
      // Fetch room details by the room ID
      this.roomViewService.getRoomById(this.tempRoomId).subscribe(
        (room) => {
          // If room is found, set the nickname in newSeat
          if (room) {
            this.newSeat.room = {
              id: this.tempRoomId,
              nickname: room.nickname
            };

            // Add seat with the updated room details
            this.roomViewService.addSeat(this.newSeat).subscribe((success) => {
              if (success) {
                form.resetForm();
                this.loadSeats();
                this.loadRooms();
              }
            });
          } else {
            console.error('Room not found with ID:', this.tempRoomId);
            // Handle the case when the room is not found
          }
        },
        (error) => {
          console.error('Error fetching room:', error);
          // Handle any errors
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
}
