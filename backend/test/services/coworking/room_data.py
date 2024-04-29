"""Room data for tests."""

import pytest
from sqlalchemy.orm import Session
from ....entities.coworking import RoomEntity
from ....models.coworking import RoomDetails
from ....models.coworking.room_details import ExtendedRoomDetails
from ..reset_table_id_seq import reset_table_id_seq

__authors__ = ["Kris Jordan"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


the_xl = ExtendedRoomDetails(
    id="SN156",
    building="Sitterson",
    room="156",
    nickname="The XL",
    capacity=40,
    reservable=False,
    seats=[],
    has_projector=False,
    has_whiteboard=True,
    has_monitor=True,
)

group_a = ExtendedRoomDetails(
    id="SN135",
    building="Sitterson",
    room="135",
    nickname="Group A",
    capacity=4,
    reservable=True,
    seats=[],
    has_projector=False,
    has_whiteboard=False,
    has_monitor=False,
)

group_b = ExtendedRoomDetails(
    id="SN137",
    building="Sitterson",
    room="137",
    nickname="Group B",
    capacity=4,
    reservable=True,
    seats=[],
    has_projector=True,
    has_whiteboard=False,
    has_monitor=False,
)

group_c = ExtendedRoomDetails(
    id="SN141",
    building="Sitterson",
    room="141",
    nickname="Group C",
    capacity=6,
    reservable=True,
    seats=[],
    has_projector=False,
    has_whiteboard=True,
    has_monitor=False,
)

pair_a = ExtendedRoomDetails(
    id="SN139",
    building="Sitterson",
    room="139",
    nickname="Pair A",
    capacity=2,
    reservable=True,
    seats=[],
    has_projector=True,
    has_whiteboard=True,
    has_monitor=False,
)

pair_b = ExtendedRoomDetails(
    id="SN777",
    building="Sitterson",
    room="777",
    nickname="Pair B",
    capacity=2,
    reservable=True,
    seats=[],
    has_projector=True,
    has_whiteboard=True,
    has_monitor=False,
)

rooms = [the_xl, group_a, group_b, group_c, pair_a, pair_b]


def insert_fake_data(session: Session):
    for room in rooms:
        entity = RoomEntity.from_model(room)
        session.add(entity)

    # Don't need to reset room sequence because its ID is a string


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
