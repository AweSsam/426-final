from fastapi import APIRouter, Depends, FastAPI, HTTPException
from typing import List
from backend.api.authentication import registered_user

from backend.models.coworking.seat import Seat
from backend.models.user import User
from backend.services.exceptions import UserPermissionException
from ..services import RoomViewService
from ..models.coworking.room_details import ExtendedRoomDetails
from ..models.coworking.seat_details import SeatDetails

from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..services.room_view import RoomViewService

api = APIRouter(prefix="/api/room-view")

openapi_tags = {
    "name": "Room View",
    "description": "Update and retrieve the room and seats view data.",
}


@api.get("/rooms", response_model=List[ExtendedRoomDetails], tags=["Room View"])
def get_all_rooms(
    roomViewService: RoomViewService = Depends(),
) -> list[ExtendedRoomDetails]:
    """Gets a list of all rooms in the system."""
    try:
        return roomViewService.get_rooms()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@api.get("/seats", response_model=List[SeatDetails], tags=["Room View"])
def get_all_seats(roomViewService: RoomViewService = Depends()) -> List[SeatDetails]:
    """Gets a list of all seats in the system."""
    try:
        return roomViewService.get_seats()
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@api.delete("/rooms/{room_id}", tags=["Room View"])
def delete_room(
    room_id: str,
    subject: User = Depends(registered_user),
    roomViewService: RoomViewService = Depends(),
):
    """Removes a room from the system."""
    try:
        roomViewService.delete_room(subject, room_id)
        return {"detail": "Room deleted successfully"}
    except UserPermissionException as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        # If the error is a ForeignKeyViolation, you might want to return a 409 Conflict
        if "ForeignKeyViolation" in str(e):
            raise HTTPException(status_code=409, detail=str(e))
        else:
            # For other types of exceptions, you can use 400 Bad Request
            raise HTTPException(status_code=400, detail=str(e))


def update_room(
    room_id: str,
    reservable: bool,  # New parameter for reservable status
    subject: User = Depends(registered_user),
    roomViewService: RoomViewService = Depends(),
) -> ExtendedRoomDetails:
    """Updates the reservable status of a specific room."""
    try:
        return roomViewService.update_room(subject, room_id, reservable)
    except UserPermissionException as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@api.delete("/seats/{seat_id}", tags=["Room View"])
def delete_seat(
    seat_id: int,
    subject: User = Depends(registered_user),
    roomViewService: RoomViewService = Depends(),
):
    """Removes a seat from the system."""
    try:
        roomViewService.delete_seat(subject, seat_id)
    except UserPermissionException as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@api.post("/rooms", tags=["Room View"])
def add_room(
    room: ExtendedRoomDetails,
    roomViewService: RoomViewService = Depends(),
    subject: User = Depends(registered_user),
) -> ExtendedRoomDetails:
    """Adds a room to the system."""
    try:
        return roomViewService.add_room(subject, room)
    except UserPermissionException as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@api.post("/seats", tags=["Room View"])
def add_seats(
    seat: SeatDetails,
    subject: User = Depends(registered_user),
    roomViewService: RoomViewService = Depends(),
) -> SeatDetails:
    """Adds a seat to the system."""
    try:
        return roomViewService.add_seat(subject, seat)
    except UserPermissionException as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))


@api.get("/rooms/{room_id}", response_model=ExtendedRoomDetails, tags=["Room View"])
def get_room_by_id(
    room_id: str, roomViewService: RoomViewService = Depends()
) -> ExtendedRoomDetails:
    """Gets details of a room by its ID."""
    try:
        return roomViewService.get_room_by_id(room_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


# @api.put("/seats/{seat_id}", tags=["Room View"])
# def update_seat(
#     seat_id: int,
#     updated_seat: SeatDetails,
#     subject: User = Depends(registered_user),
#     roomViewService: RoomViewService = Depends(),
# ) -> SeatDetails:
#     """Updates details of a specific seat."""
#     try:
#         return roomViewService.update_seat(subject, seat_id, updated_seat)
#     except UserPermissionException as e:
#         raise HTTPException(status_code=403, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
