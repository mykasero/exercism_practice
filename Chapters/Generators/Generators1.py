"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    iter1 = 0
    iter_letters = -1
    while True:
        iter_letters += 1
        if iter1 == number:
            break
        elif iter_letters == 0:
            yield "A"
        elif iter_letters == 1:
            yield "B"
        elif iter_letters == 2:
            yield "C"
        else:
            iter_letters = -1
            yield "D"
        iter1 += 1


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """
    seat_amount = 0
    iter_row = 1
    iter_letter = -1
    seat_letter = ["A", "B", "C", "D"]

    while True:
        iter_letter += 1

        if number < 12 * 4:

            if iter_row == 13:
                iter_row += 1
                iter_letter -= 1
            elif seat_amount == number:
                break
            elif iter_letter == 0:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
            elif iter_letter == 1:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
            elif iter_letter == 2:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
            else:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
                iter_letter = -1
                iter_row += 1

            seat_amount += 1
        else:
            if iter_row == 13:
                iter_row += 1
                iter_letter -= 1
            elif iter_letter == 0:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
            elif iter_letter == 1:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
            elif iter_letter == 2:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
            else:
                yield f"{str(iter_row) + seat_letter[iter_letter]}"
                iter_letter = -1
                iter_row += 1
            if seat_amount == number:
                break
            seat_amount += 1


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    final = {}
    seats = generate_seats(len(passengers))
    ppl_counter = 0
    for iter in seats:
        final[passengers[ppl_counter]] = iter
        ppl_counter += 1

    return final


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    base = ""
    zero0 = "0"
    for item in seat_numbers:
        base = f"{str(item) + flight_id}"
        if len(base) < 12:
            base = base + f"{(12 - len(base)) * zero0}"
            yield base
