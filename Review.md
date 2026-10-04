# Review

## Identity
Name: Sorawich Pimsen, student ID 6681297
AI tool used: GitHub Copilot (Plan mode for the plan, Interactive mode to implement)
Discussion partners: [Worked independently]

## Review decision
In `service.py / move_booking`, the agent checks conflicts with `has_conflict([booking for booking in bookings if booking is not target], new_room, new_start, new_end)`. I kept it. It leaves out only the booking being moved, so its own old interval can't block the move, while every other booking in the list can still conflict. It also runs after the find, cancelled, room and interval checks and before any assignment to `target`, so a failed move leaves the booking unchanged. I read the diff and confirmed `rules.py` and `SPEC.md` were not edited.

## Checks
Baseline commit: 06ff2b7
Baseline: `uv run --python 3.12 python -m unittest -v test_baseline` ran 6 tests, OK. `test_move_smoke` ran 3 tests with 3 errors (NotImplementedError) before implementation.
Final: `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student` ran 11 tests, OK.

## Remaining uncertainty
The tests do not cover every possible combination of invalid room/time inputs or interactions with multiple other bookings, I'm not sure if this solution covers all the edge cases that can be entered in, while an admittedly vague concern one that i can provide more on is,Back-to-back bookings: I did not test moving a booking so that it ends exactly when another one starts, has_conflict should allow this but i haven't check how it interacts with moves