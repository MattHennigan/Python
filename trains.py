from sys import argv
from read_data import read_data

def is_possible(stops, train_capacity):
    """
    Tests whether the given stops are possible given the trains capacity.
    There is a description for each section of code in each comment.
    """

    # "The train should start the journey empty".
    passengers_in_train = 0

    for left_train, entered_train, stayed_at_station in stops:
        passengers_in_train -= left_train
        if passengers_in_train < 0:
            # Checks that "the train should start .. the journey empty".
            return False

        passengers_in_train += entered_train
        if passengers_in_train > train_capacity:
            # Checks that "the number of people in the train did not exceed the
            # capacity".
            return False
        elif passengers_in_train < 0:
            # Checks that "the number of people in the train .. nor .. was 
            # below 0".
            return False
        elif passengers_in_train < train_capacity and stayed_at_station > 0:
            # Checks that "no passenger waited in vain".
            return False

    if stayed_at_station > 0:
        # Checks that "in particular passengers should not wait for the train
        # at the last station".
        return False

    if passengers_in_train > 0:
        # Checks that "the train should .. finish the journey empty".
        return False

    return True

if len(argv) < 2:
    print("No data file given")
    exit(1)                     # Exit from the program now

data, capacity = read_data(argv[1])
print("possible" if is_possible(data, capacity) else "impossible")
