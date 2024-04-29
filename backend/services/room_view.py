from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from sqlalchemy.orm import joinedload
from sqlalchemy import select
from sqlite3 import IntegrityError

from backend.models.user import User

from ..entities.coworking.reservation_entity import ReservationEntity
from ..entities.coworking import reservation_seat_table
from ..database import db_session
from ..models.coworking.room_details import RoomDetails, ExtendedRoomDetails
from ..models.coworking.seat_details import SeatDetails
from .permission import PermissionService
from ..entities.coworking.room_entity import RoomEntity
from ..entities.coworking.seat_entity import SeatEntity


class RoomViewService:
    """Service that performs all of the actions on the Room and Seat details"""

    def __init__(
        self,
        session: Session = Depends(db_session),
        permission: PermissionService = Depends(),
    ):
        self._session = session
        self._permission = permission

    def get_rooms(self) -> list[ExtendedRoomDetails]:
        """Returns a list of all current rooms on file."""
        entities = self._session.scalars(select(RoomEntity)).all()
        return [entity.to_extended_details_model() for entity in entities]

    def get_seats(self) -> list[SeatDetails]:
        """Returns a list of all current seats on file."""
        entities = self._session.scalars(select(SeatEntity)).all()
        return [entity.to_model() for entity in entities]

    def delete_room(self, user: User, room_id: str) -> None:
        """Removes a room from the current list of rooms."""
        self._permission.enforce(user, "room.manage", "room")

        room_to_delete = (
            self._session.query(RoomEntity)
            .options(joinedload(RoomEntity.seats))
            .filter(RoomEntity.id == room_id)
            .one_or_none()
        )

        if room_to_delete:
            # Deleting all associated seats
            for seat in room_to_delete.seats:
                self.delete_seat(user, seat.id)

            # Delete the room
            self._session.delete(room_to_delete)
            self._session.commit()
        else:
            raise Exception("Room to delete does not exist")

    def update_room(
        self,
        user: User,
        room_id: str,
        reservable: bool,  # New parameter for reservable status
    ) -> ExtendedRoomDetails:
        """Updates the reservable status of a specific room."""
        # Check user permissions
        self._permission.enforce(user, "room.manage", "room")

        # Get the room entity from the database
        room_entity = (
            self._session.query(RoomEntity)
            .filter(RoomEntity.id == room_id)
            .one_or_none()
        )

        if room_entity is None:
            raise Exception("Room not found")

        # Update reservable status
        room_entity.reservable = reservable

        # Commit changes to the database
        self._session.commit()

        # Return updated room details
        return room_entity.to_extended_details_model()

    def delete_seat(self, user: User, seat_id: int) -> None:
        """Removes a seat from the current list of seats."""
        self._permission.enforce(user, "room.manage", "room")

        self._session.execute(
            reservation_seat_table.delete().where(
                reservation_seat_table.c.seat_id == seat_id
            )
        )

        seat_to_delete = (
            self._session.query(SeatEntity)
            .filter(SeatEntity.id == seat_id)
            .one_or_none()
        )

        if seat_to_delete:
            self._session.delete(seat_to_delete)
            self._session.commit()
        else:
            raise Exception("Seat to delete does not exist")

    def add_room(self, user: User, room: ExtendedRoomDetails) -> ExtendedRoomDetails:
        # Enforce permission check
        self._permission.enforce(user, "room.manage", "room")

        # Proceed with the original logic if the user has permission
        room_entity = RoomEntity.from_model(room)
        self._session.add(room_entity)
        self._session.commit()
        return room_entity.to_extended_details_model()

    def add_seat(self, user: User, seat: SeatDetails) -> SeatDetails:
        """Adds a new seat to the current list of seats."""
        self._permission.enforce(user, "room.manage", "room")

        seat_entity = SeatEntity.from_model(seat)
        room_entity = self._session.get(RoomEntity, seat.room.id)

        if not room_entity:
            raise Exception("Room does not exist for the given seat ID")

        # Set the room nickname in the seat details
        seat_entity.room = room_entity
        seat_entity.room.nickname = room_entity.nickname

        self._session.add(seat_entity)
        self._session.commit()
        return seat_entity.to_model()

    def get_room_by_id(self, room_id: str) -> ExtendedRoomDetails:
        """Returns details of a specific room by its ID."""
        room_entity = (
            self._session.query(RoomEntity)
            .filter(RoomEntity.id == room_id)
            .one_or_none()
        )

        if room_entity:
            return room_entity.to_extended_details_model()
        else:
            raise Exception(f"Room with ID {room_id} does not exist")
