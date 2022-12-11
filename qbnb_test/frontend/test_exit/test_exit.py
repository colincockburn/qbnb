from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# Tests if application exits correctly from home
def test_home_exit():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('home_exit.in'))
    expected_out = open(current_folder.joinpath('home_exit.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if application exits correctly from login page
def test_login_exit():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('login_exit.in'))
    expected_out = open(current_folder.joinpath('login_exit.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if application exits correctly from register page
def test_register_exit():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('register_exit.in'))
    expected_out = open(current_folder.joinpath('register_exit.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()
