from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# Tests if application creates listing with valid data
def test_valid_listing_creation():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('valid_listing.in'))
    expected_out = open(current_folder.joinpath('valid_listing.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if listing title is alphanumeric R4-1
def test_unalphanumeric_title():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('unalphanumeric_title.in'))
    expected_out = open(
        current_folder.joinpath('unalphanumeric_title.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if listing title first character is space R4-1
def test_first_char_space_title():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('first_char_space_title.in'))
    expected_out = open(
        current_folder.joinpath('first_char_space_title.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if listing title last character is space R4-1
def test_last_char_space_title():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('last_char_space_title.in'))
    expected_out = open(
        current_folder.joinpath('last_char_space_title.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if description is too short R4-3
def test_short_description():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('short_description.in'))
    expected_out = open(
        current_folder.joinpath('short_description.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if description is too long R4-3
def test_long_description():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('long_description.in'))
    expected_out = open(current_folder.joinpath('long_description.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if title is too long R4-2
def test_long_title():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('long_title.in'))
    expected_out = open(current_folder.joinpath('long_title.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if description is longer than title R4-4
def test_longer_desc_than_title():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('longer_desc_than_title.in'))
    expected_out = open(
        current_folder.joinpath('longer_desc_than_title.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if price is too low R4-5
def test_low_price():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('low_price.in'))
    expected_out = open(current_folder.joinpath('low_price.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if price is too high R4-5
def test_high_price():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('high_price.in'))
    expected_out = open(current_folder.joinpath('high_price.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if user already has listing with same title R4-8
def test_duplicate_title():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('duplicate_title.in'))
    expected_out = open(current_folder.joinpath('duplicate_title.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()
