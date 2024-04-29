import { Profile } from '../models.module';

export interface Seat {
  id: number;
  title: string;
  shorthand: string;
  reservable: boolean;
  has_monitor: boolean;
  sit_stand: boolean;
  x: number;
  y: number;
}

export interface SeatDetails {
  id: number;
  title: string;
  shorthand: string;
  reservable: boolean;
  has_monitor: boolean;
  sit_stand: boolean;
  x: number;
  y: number;
  room: Room;
}

export interface RoomDetails extends Room {
  building: string;
  room: string;
  capacity: number;
  reservable: boolean;
  seats: Seat[];
  has_projector: boolean;
  has_whiteboard: boolean;
  has_monitor: boolean;
  gridWidth?: number;
  gridHeight?: number;
}

export interface Room {
  id: string;
  nickname: string;
}
