from pathlib import Path
import subprocess
from qbnb.models import User, db

# add a user to database so we may test for a valid login.
user = User(user_id=5673, email="walterwhite@gmail.com",
            password="Password1$", username='waltuh', balance=100)
db.session.add(user)
db.session.commit()

# get expected input/output file
current_folder = Path(__file__).parent


def test_login_r21():
    """ test for correct email and password
    example of functionality coverage test
    """

    # read expected in/out
    expected_in_r21 = open(current_folder.joinpath('R21.in'))
    expected_out_r21 = open(current_folder.joinpath('R21.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r21,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r21.strip()


def test_login_r22_1():
    """test for empty email 
    example of input coverage test.
    """

    # read expected in/out
    expected_in_r22_1 = open(current_folder.joinpath('R22_1.in'))
    expected_out_r22_1 = open(current_folder.joinpath('R22_1.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r22_1,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r22_1.strip()


def test_login_r22_2():
    """ test for invalid email form
    example of output coverage test
    """

    # read expected in/out
    expected_in_r22_2 = open(current_folder.joinpath('R22_2.in'))
    expected_out_r22_2 = open(current_folder.joinpath('R22_2.out')).read()
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r22_2,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r22_2.strip()


def test_login_r22_3():
    """ test for invalid password
    example of output coverage test
    """

    # read expected in/out
    expected_in_r22_3 = open(current_folder.joinpath('R22_3.in'))
    expected_out_r22_3 = open(current_folder.joinpath('R22_3.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_r22_3,
        capture_output=True
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_r22_3.strip()