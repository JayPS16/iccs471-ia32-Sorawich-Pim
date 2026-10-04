"""Booking operations. Implement only the agreed rescheduling change."""
from models import Booking
from rules import validate_room, validate_interval, has_conflict

def find_booking(bookings: list[Booking], booking_id: int) -> Booking:
    for booking in bookings:
        if booking.id == booking_id:
            return booking
    raise ValueError("Booking not found")

def add_booking(bookings: list[Booking], room: str, start: int, end: int) -> Booking:
    validate_room(room)
    validate_interval(start, end)
    if has_conflict(bookings, room, start, end):
        raise ValueError("Booking conflict")
    next_id = max((booking.id for booking in bookings), default=0) + 1
    booking = Booking(next_id, room, start, end)
    bookings.append(booking)
    return booking

def move_booking(bookings: list[Booking], booking_id: int, new_room: str,
                 new_start: int, new_end: int) -> Booking:
    """Move an active booking to a new room and time window."""
    target = find_booking(bookings, booking_id)
    if target.status != "active":
        raise ValueError("Booking is not active")

    validate_room(new_room)
    validate_interval(new_start, new_end)

    if has_conflict([booking for booking in bookings if booking is not target],
                    new_room, new_start, new_end):
        raise ValueError("Booking conflict")

    if target.room == new_room and target.start == new_start and target.end == new_end:
        return target

    target.room = new_room
    target.start = new_start
    target.end = new_end
    return target
