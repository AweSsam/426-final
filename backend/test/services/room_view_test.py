"""Unit tests for the room view service class."""

from fastapi import HTTPException
import pytest

from ...entities.coworking.reservation_entity import ReservationEntity
from ...services.permission import PermissionService
from ...services.room_view import RoomViewService
from ...models.coworking.seat_details import SeatDetails
from ...models.coworking.room_details import ExtendedRoomDetails
from ...entities.coworking import RoomEntity
from ...entities.coworking import SeatEntity
from .fixtures import room_view_svc
from sqlalchemy.orm import Session
from ...database import db_session, engine
from ...test.services.coworking.room_data import (
    the_xl,
    group_a,
    group_b,
    group_c,
    pair_a,
    pair_b,
)

from ...test.services.coworking.seat_data import (
    monitor_seat_00,
    monitor_seat_01,
    monitor_seat_10,
    monitor_seat_11,
    monitor_seat_12,
)


def test_get_rooms(room_view_svc: RoomViewService):
    room_view_svc.add_room(the_xl)
    room_view_svc.add_room(group_a)
    room_view_svc.add_room(group_b)
    room_view_svc.add_room(group_c)
    room_view_svc.add_room(pair_a)
    assert room_view_svc.get_rooms() is not None
    assert len(room_view_svc.get_rooms()) == 5


def test_get_rooms_empty(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.get_rooms()


def test_get_seats_no_seats(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.get_seats()


def test_get_seats(room_view_svc: RoomViewService):
    room_view_svc.add_room(the_xl)
    room_view_svc.add_seat(monitor_seat_00)
    room_view_svc.add_seat(monitor_seat_01)
    room_view_svc.add_seat(monitor_seat_10)
    room_view_svc.add_seat(monitor_seat_11)
    assert room_view_svc.get_seats() is not None
    assert len(room_view_svc.get_seats()) == 4


def test_add_room(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(the_xl)
    assert room is not None
    assert room_view_svc.get_rooms() is not None


def test_add_duplicate_room(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(the_xl)
    with pytest.raises(Exception):
        room_view_svc.add_room(room.to_extended_details_model())  # type: ignore


def test_add_seat(room_view_svc: RoomViewService):
    room_view_svc.add_room(the_xl)
    seat = room_view_svc.add_seat(monitor_seat_00)
    assert seat is not None
    assert room_view_svc.get_seats() is not None


def test_add_duplicate_seat(room_view_svc: RoomViewService):
    room_view_svc.add_room(the_xl)
    seat = room_view_svc.add_seat(monitor_seat_00)
    with pytest.raises(Exception):
        room_view_svc.add_seat(seat.to_model())  # type: ignore


def test_add_seat_to_non_existing_room(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.add_seat(monitor_seat_00)


def test_init(room_view_svc: RoomViewService):
    db = Session(engine)
    permission_service = PermissionService(db)
    assert db is not None
    assert permission_service is not None
    assert RoomViewService(session=db, permission=permission_service) is not None


def test_delete_reserved_room(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(the_xl)
    with pytest.raises(Exception):
        room_view_svc.delete_room(the_xl.id)


def test_delete_room(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(pair_b)
    room_view_svc.add_seat(monitor_seat_12)
    room = room_view_svc.delete_room(room.id)
    assert room is None


def test_delete_non_existing_room(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.delete_room("non_existent_room_id")


def test_delete_reserved_room_not_reservable(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(the_xl)
    room_view_svc.add_seat(monitor_seat_00)

    try:
        room_view_svc.delete_room(room.id)
    except HTTPException as e:
        assert e.status_code == 400
        assert e.detail == "Cannot delete, room has been reserved"


def test_delete_seat(room_view_svc: RoomViewService):
    room_view_svc.add_room(the_xl)
    seat = room_view_svc.add_seat(monitor_seat_00)
    seat = room_view_svc.delete_seat(seat.id)
    assert seat is None


def test_delete_non_existing_seat(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.delete_seat(9999)


def test_delete_seat_with_integrity_error(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.delete_seat(9999)


def test_delete_non_reservable_room(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(the_xl)
    room_view_svc.add_seat(monitor_seat_00)

    with pytest.raises(HTTPException):
        room_view_svc.delete_room(room.id)


def test_delete_room_with_non_existing_seats(room_view_svc: RoomViewService):
    room = room_view_svc.add_room(group_a)
    room_view_svc.delete_room(room.id)
    with pytest.raises(Exception):
        room_view_svc.get_rooms()


def test_delete_seat_from_non_existing_room(room_view_svc: RoomViewService):
    with pytest.raises(Exception):
        room_view_svc.delete_seat(9999)
