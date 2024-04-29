"""Seat data for tests."""

import pytest
from sqlalchemy import delete
from sqlalchemy.orm import Session
from ....entities.coworking import SeatEntity
from ....models.coworking.seat_details import SeatDetails
from ....models.coworking.seat import Seat
from typing import Sequence

from ..reset_table_id_seq import reset_table_id_seq
from .room_data import the_xl, pair_b, group_a

__authors__ = ["Sameera & Dharshini"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

monitor_seat_00 = SeatDetails(
    id=1,
    title="Standing Monitor 00",
    shorthand="M00",
    reservable=True,
    has_monitor=True,
    sit_stand=True,
    x=0,
    y=0,
    room=the_xl,
)

monitor_seat_01 = SeatDetails(
    id=2,
    title="Standing Monitor 01",
    shorthand="M01",
    reservable=False,
    has_monitor=True,
    sit_stand=True,
    x=0,
    y=1,
    room=the_xl,
)
monitor_seat_10 = SeatDetails(
    id=3,
    title="Monitor 10",
    shorthand="M10",
    reservable=True,
    has_monitor=True,
    sit_stand=False,
    x=1,
    y=0,
    room=the_xl,
)
monitor_seat_11 = SeatDetails(
    id=4,
    title="Monitor 11",
    shorthand="M11",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=1,
    y=1,
    room=the_xl,
)
monitor_seat_12 = SeatDetails(
    id=5,
    title="Monitor 12",
    shorthand="M12",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=6,
    room=pair_b,
)
monitor_seat_50 = SeatDetails(
    id=6,
    title="Monitor 50",
    shorthand="MS50",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=0,
    room=the_xl,
)
monitor_seat_60 = SeatDetails(
    id=7,
    title="Monitor 60",
    shorthand="MS60",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=6,
    y=0,
    room=the_xl,
)
monitor_seat_70 = SeatDetails(
    id=8,
    title="Monitor 70",
    shorthand="MS70",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=7,
    y=0,
    room=the_xl,
)
monitor_seat_55 = SeatDetails(
    id=9,
    title="Monitor 55",
    shorthand="MS55",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=5,
    room=the_xl,
)
monitor_seat_56 = SeatDetails(
    id=10,
    title="Monitor 56",
    shorthand="MS56",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=6,
    room=the_xl,
)
monitor_seat_56 = SeatDetails(
    id=10,
    title="Monitor 56",
    shorthand="MS56",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=6,
    room=the_xl,
)

monitor_seat_65 = SeatDetails(
    id=11,
    title="Monitor 65",
    shorthand="MS55",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=6,
    y=5,
    room=the_xl,
)
checkin = SeatDetails(
    id=17,
    title="Checkin Desk",
    shorthand="checkin",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=3,
    y=1,
    room=the_xl,
)
monitor_seat_66 = SeatDetails(
    id=12,
    title="Monitor 66",
    shorthand="MS56",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=6,
    y=6,
    room=the_xl,
)

standing_seat_45 = SeatDetails(
    id=13,
    title="Standing 45",
    shorthand="SS45",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=4,
    y=5,
    room=group_a,
)
standing_seat_46 = SeatDetails(
    id=14,
    title="Standing 46",
    shorthand="SS46",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=4,
    y=6,
    room=group_a,
)
standing_seat_55 = SeatDetails(
    id=15,
    title="Standing 55",
    shorthand="SS55",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=5,
    room=group_a,
)
standing_seat_56 = SeatDetails(
    id=16,
    title="Standing 56",
    shorthand="SS56",
    reservable=False,
    has_monitor=True,
    sit_stand=False,
    x=5,
    y=6,
    room=group_a,
)

monitor_seats = [
    monitor_seat_00,
    monitor_seat_01,
    monitor_seat_10,
    monitor_seat_11,
    monitor_seat_12,
    monitor_seat_50,
    monitor_seat_60,
    monitor_seat_70,
    monitor_seat_55,
    monitor_seat_56,
    monitor_seat_65,
    monitor_seat_66,
    checkin,
    standing_seat_45,
    standing_seat_46,
    standing_seat_55,
    standing_seat_56,
]

# common_area_00 = SeatDetails(
#     id=20,
#     title="Common Area 00",
#     shorthand="C00",
#     reservable=False,
#     has_monitor=False,
#     sit_stand=False,
#     x=5,
#     y=0,
#     room=the_xl.to_room()
# )
# common_area_01 = SeatDetails(
#     id=21,
#     title="Common Area 01",
#     shorthand="C01",
#     reservable=False,
#     has_monitor=False,
#     sit_stand=False,
#     x=5,
#     y=1,
#     room=the_xl.to_room()
# )
# common_area_seats = [common_area_00, common_area_01]

# conference_table_00 = SeatDetails(
#     id=40,
#     title="Conference Table 01",
#     shorthand="G01",
#     reservable=True,
#     has_monitor=False,
#     sit_stand=False,
#     x=20,
#     y=20,
#     room=the_xl.to_room()
# )
# conference_table_01 = SeatDetails(
#     id=41,
#     title="Conference Table 02",
#     shorthand="G02",
#     reservable=False,
#     has_monitor=False,
#     sit_stand=False,
#     x=20,
#     y=21,
#     room=the_xl.to_room(),
# )
# conference_table_seats = [conference_table_00, conference_table_01]

seats: Sequence[Seat] = monitor_seats  # + common_area_seats + conference_table_seats

reservable_seats = [seat for seat in seats if seat.reservable]

unreservable_seats = [seat for seat in seats if not seat.reservable]


def insert_fake_data(session: Session):
    for seat in seats:
        entity = SeatEntity.from_model(seat)
        session.add(entity)
    reset_table_id_seq(session, SeatEntity, SeatEntity.id, len(seats) + 1)


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()


def delete_all(session: Session):
    session.execute(delete(SeatEntity))
