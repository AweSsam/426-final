from __future__ import annotations
from pydantic import BaseModel
from .seat import Seat
from .room_details import Room

__authors__ = ["Sameera & Dharshini"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"


class SeatDetails(Seat, BaseModel):
    room: Room
