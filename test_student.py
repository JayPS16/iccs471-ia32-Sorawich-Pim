"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from service import add_booking, move_booking


class StudentMoveTests(unittest.TestCase):
    def test_move_overlapping_own_old_interval(self):
        """Given one active A booking from 10 to 14.
        When it is moved to A from 12 to 16.
        Expect the same active booking object to succeed with id 1.
        """
        bookings = []
        booking = add_booking(bookings, "A", 10, 14)

        result = move_booking(bookings, 1, "A", 12, 16)

        self.assertIs(result, booking)
        self.assertIs(result, bookings[0])
        self.assertEqual((result.room, result.start, result.end), ("A", 12, 16))
        self.assertEqual(result.status, "active")
        self.assertEqual(result.id, 1)
        self.assertEqual(len(bookings), 1)

    def test_move_to_same_room_and_times(self):
        """Given one active A booking from 10 to 14.
        When it is moved to A from 10 to 14.
        Expect the same active booking object and unchanged booking details.
        """
        bookings = []
        booking = add_booking(bookings, "A", 10, 14)

        result = move_booking(bookings, 1, "A", 10, 14)

        self.assertIs(result, booking)
        self.assertIs(result, bookings[0])
        self.assertEqual((result.room, result.start, result.end), ("A", 10, 14))
        self.assertEqual(result.status, "active")
        self.assertEqual(result.id, 1)
        self.assertEqual(len(bookings), 1)

if __name__ == "__main__":
    unittest.main()
