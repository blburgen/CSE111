from bradys_art import read_dictionary
from bradys_art import 
from inspect import signature
from os import path
from tempfile import mktemp
import pytest


def test_read_dictionary():
    """Verify that the read_dictionary function works correctly.
    Parameters: none
    Return: nothing
    """
    I_NUMBER_INDEX = 0

    # Verify that the read_dictionary function uses its filename
    # parameter by doing the following:
    # 1. Get a filename for a file that doesn't exist.
    # 2. Call the read_dictionary function with the filename.
    # 3. Verify that the open function inside the read_dictionary
    #    function raises a FileNotFoundError.
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        call_read_dictionary(filename, I_NUMBER_INDEX)
        pytest.fail("read_dictionary function must use its filename parameter")

    # Call the read_dictionary function which will read the art.csv
    # file and create and return a dictinoary.
    filename = path.join(path.dirname(__file__), "art.csv")
    art_dict = call_read_dictionary(filename, I_NUMBER_INDEX)

    # Verify that the read_dictionary function returns a dictionary.
    assert isinstance(art_dict, dict), \
        "read_dictionary function must return a dictionary:" \
        f" expected a dictionary but found a {type(art_dict)}"

    # Verify that the art dictionary contains atleast five items.
    length = len(art_dict)
    exp_len = 5
    assert length > exp_len, \
        "art dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"

    # Verify the correctness of five items in the dictionary.
    check_art(art_dict, "1", "Why should I care")
    check_art(art_dict, "2", "I quit" )
    check_art(art_dict, "3", "Laying back")
    check_art(art_dict, "4", "asdf")
    check_art(art_dict, "5", "Large")


def call_read_dictionary(filename, key_column_index):
    """Call the read_dictionary function with the correct number of
    parameters.
    """
    sig = signature(read_dictionary)
    length = len(sig.parameters)
    min_len = 1
    max_len = 2
    assert length == min_len or length == max_len, \
        "The read_dictionary function contains too " \
        f"{'few' if length < min_len else 'many'} parameters; " \
        f"expected {min_len} or {max_len} parameters but found {length}"
    if length == min_len:
        dictionary = read_dictionary(filename)
    else:
        dictionary = read_dictionary(filename, key_column_index)
    return dictionary


def check_art(art_dict, idnumber, exp_name):
    """Verify that the data for one art stored in the
    art dictionary is correct.

    Parameters
        art_dict: a dictionary that contains art data
        idnumber: an art's number that should be in the dictionary
        exp_name: the art's expected name
    Return: nothing
    """
    # Verify that idnumber is in the art dictionary.
    assert idnumber in art_dict, \
        f'"{idnumber}" is missing from the art dictionary.'

    actual = art_dict[idnumber]
    assert isinstance(actual, str) or isinstance(actual, list), \
        "Each value in the art dictionary must be either a string " \
        f"or a list. The value for {idnumber} is of type {type(actual)} " \
        "which is not a string or a list."

    if isinstance(actual, str):
        # Verify that the art's name is correct.
        assert actual[1] == exp_name, \
                f'Wrong name for "{idnumber}"; ' \
                f'expected {exp_name} but found {actual}'
    else:
        length = len(actual)
        min_len = 1
        assert length >= min_len, \
            f"The value list for art {idnumber} contains too " \
            f"{'few' if length < min_len else 'many'} elements; " \
            f"expected {min_len} elements but found {length}"

        if length > min_len:
            # Verify that the art's name is correct.
            NAME_INDEX = 1
            act_name = actual[NAME_INDEX]
            assert act_name == exp_name, \
                    f'Wrong name for "{idnumber}"; ' \
                    f'expected {exp_name} but found {act_name}'
        else:
            # Verify that the art's I-Number is correct.
            ID_NUMBER_INDEX = 0
            act_idnum = actual[ID_NUMBER_INDEX]
            assert act_idnum == idnumber, \
                    'Inconsistent IDnumbers in the key and value. ' \
                    f'The key is {idnumber} but {act_idnum} is in ' \
                    'the corresponding value.'

            # Verify that the art's name is correct.
            NAME_INDEX = 1
            act_name = actual[NAME_INDEX]
            assert act_name == exp_name, \
                    f'Wrong name for "{idnumber}"; ' \
                    f'expected {exp_name} but found {act_name}'


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
