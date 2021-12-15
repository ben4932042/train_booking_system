class CabinInfo:
    """[summary]
    number_of_cabin (int): default number of cabin
    number_of_cabin_col (int): default number of col in cabin
    number_of_cabin_row (int): default number of row in cabin
    number_of_seats (int): default number of seats in cabin
    """

    number_of_cabin: int = 10
    number_of_cabin_col: int = 5
    number_of_cabin_row: int = 10
    number_of_seats: int = number_of_cabin_col * number_of_cabin_row


class BusinessCabin:
    """[summary]
    cabin_no_list (list): cabin no list of business cabin
    """
    cabin_no_list: list = [0, 1, 2]


class EconomyCabin:
    """[summary]
    cabin_no_list (list): cabin no list of economy cabin
    """
    cabin_no_list: list = [3, 4, 5, 6, 7, 8, 9]
    