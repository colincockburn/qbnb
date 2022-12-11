from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# Tests if application navigates correctly to login page
def test_nav_login_page():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('nav_login_page.in'))
    expected_out = open(current_folder.joinpath('nav_login_page.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()


# Tests if application navigates correctly to login page
def test_nav_register_page():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in = open(current_folder.joinpath('nav_register_page.in'))
    expected_out = open(current_folder.joinpath(
        'nav_register_page.out')).read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out.strip()
