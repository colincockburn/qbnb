from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent


# Tests what happens if email and password are empty
def test_register_r11():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    # read expected in/out
    expected_in_r11 = open(current_folder.joinpath(
        'r11.in'))
    expected_out_r11 = open(current_folder.joinpath(
        'r11.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r11,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r11.strip()


# Tests the reliability of the email format parameters
def test_register_r13():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    expected_in_r13 = open(current_folder.joinpath(
        'r13.in'))
    expected_out_r13 = open(current_folder.joinpath(
        'r13.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r13,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r13.strip()


# Testing password complexity requirements piece by piece
def test_register_r14():  # Systematic Functionality Testing Method
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    expected_in_r14 = open(current_folder.joinpath(
        'r14.in'))
    expected_out_r14 = open(current_folder.joinpath(
        'r14.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r14,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r14.strip()


# Testing all possibilities of username failure
def test_register_r15():  # Exhaustive Testing Method
    """capsys -- object created by pytest to 
    capture stdout and stderr"""
    expected_in_r15 = open(current_folder.joinpath(
        'r15.in'))
    expected_out_r15 = open(current_folder.joinpath(
        'r15.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r15,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r15.strip()


# Testing the length boundaries of a username
def test_register_r16():  # Boundary Testing Method
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    expected_in_r16 = open(current_folder.joinpath(
        'r16.in'))
    expected_out_r16 = open(current_folder.joinpath(
        'r16.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r16,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r16.strip()


# Testing if an email hasn't already been used
def test_register_r17a():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    expected_in_r17a = open(current_folder.joinpath(
        'r17a.in'))
    expected_out_r17a = open(current_folder.joinpath(
        'r17a.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r17a,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r17a.strip()


# Testing if an email has already been used
def test_register_r17b():
    """capsys -- object created by pytest to 
    capture stdout and stderr"""

    expected_in_r17b = open(current_folder.joinpath(
        'r17b.in'))
    expected_out_r17b = open(current_folder.joinpath(
        'r17b.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r17b,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r17b.strip()
