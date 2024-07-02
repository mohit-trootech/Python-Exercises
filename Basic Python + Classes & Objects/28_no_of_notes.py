"""
Python Program to Find the Number of notes 
"""

notes = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def no_of_notes(amount: int) -> dict:
    """
    function to find the number of notes and coins in given amount
    """
    if isinstance(amount, int):
        required_notes = {}
        temporary_amount = amount
        while True:
            for note in notes:
                if note <= temporary_amount:
                    data = divmod(temporary_amount, note)
                    required_notes.setdefault(note, data[0])
                    temporary_amount = data[1]
            if temporary_amount == 0:
                break

        return f"Notes Required in Amount : {amount} -> {required_notes}"


if __name__ == "__main__":
    print(no_of_notes(3))
