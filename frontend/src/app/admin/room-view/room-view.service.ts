import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Seat } from 'src/app/coworking/coworking.models';
import { RoomDetails, SeatDetails } from 'src/app/room-view/room-view.models';

@Injectable({
  providedIn: 'root'
})
export class RoomViewService {
  private apiUrl = '/api/room-view';

  constructor(private http: HttpClient) {}
  /** Adds a seat into the backend database using the backend HTTP post request.
   * @param newSeat: Seat model object defining the seat to add to the database
   * @returns {Observable<boolean>}
   */
  addSeat(newSeat: Seat): Observable<boolean> {
    return this.http.post<boolean>(`${this.apiUrl}/seats`, newSeat);
  }

  /** Adds a room into the backend database using the backend HTTP post request.
   * @param room: Seat model object defining the room to add to the database
   * @returns {Observable<boolean>}
   */
  addRoom(room: RoomDetails): Observable<boolean> {
    return this.http.post<boolean>(`${this.apiUrl}/rooms`, room);
  }

  getRooms(): Observable<RoomDetails[]> {
    return this.http.get<RoomDetails[]>(`${this.apiUrl}/rooms`);
  }

  getRoomById(roomId: string): Observable<RoomDetails> {
    return this.http.get<RoomDetails>(`${this.apiUrl}/rooms/${roomId}`);
  }

  /** Returns a list of seats from the backend database table using the backend HTTP get request.
   * @returns {Observable<Seat[]>}
   */
  getSeats(): Observable<SeatDetails[]> {
    return this.http.get<SeatDetails[]>(`${this.apiUrl}/seats`);
  }

  /** Removes a seat from the backend database using the backend HTTP delete request.
   * @param seatId: Number representing the id of the seat to remove
   * @returns {Observable<boolean>}
   */
  deleteSeat(seatId: number): Observable<boolean> {
    return this.http.delete<boolean>(`${this.apiUrl}/seats/${seatId}`);
  }

  /** Removes a room from the backend database using the backend HTTP delete request.
   * @param roomId: String representing the id of the room to remove
   * @returns {Observable<boolean>}
   */
  deleteRoom(roomId: string): Observable<boolean> {
    return this.http.delete<boolean>(`${this.apiUrl}/rooms/${roomId}`);
  }
}
