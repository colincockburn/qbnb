from pathlib import Path
import subprocess
from qbnb.models import User, Listing, db

# add a user to database so we may test for a valid login.
user = User(user_id=5773, email="nelsonman@gmail.com",
            password="Password2$", username='leader', balance=100)
lisitng = Listing(lisitng_id=5783, listing_title='Bungalow',
                  owner_id=5773, owner_email='nelsonman@gmail.com',
                  description='Two Bed-Room Bungalow',
                  address='123 Test Rd.', last_date_modified='',
                  price=2000)
db.session.add(user)
db.session.add(lisitng)
db.session.commit()

# get expected input/output file
current_folder = Path(__file__).parent


def test_update_listing_ult1():
    """ test for ability to update
    title of possible listing
    """

    # read expected in/out
    expected_in_ult1 = open(current_folder.joinpath('ult1.in'))
    expected_out_ult1 = open(current_folder.joinpath('ult1.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_ult1,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_ult1.strip()


def test_update_listing_ult2():
    """ test for ability to update
    description of possible listing
    """

    # read expected in/out
    expected_in_ult2 = open(current_folder.joinpath('ult2.in'))
    expected_out_ult2 = open(current_folder.joinpath('ult2.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_ult2,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_ult2.strip()


def test_update_listing_ult3():
    """ test for ability to update
    address of possible listing
    """

    # read expected in/out
    expected_in_ult3 = open(current_folder.joinpath('ult3.in'))
    expected_out_ult3 = open(current_folder.joinpath('ult3.out')).read()
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_ult3,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_ult3.strip()


def test_update_listing_ult4():
    """ test for ability to update
    price of possible listing
    """

    # read expected in/out
    expected_in_ult4 = open(current_folder.joinpath('ult4.in'))
    expected_out_ult4 = open(current_folder.joinpath('ult4.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_ult4,
        capture_output=True
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_ult4.strip()


def test_update_listing_ult5():
    """ test for invalid listing
    """

    # read expected in/out
    expected_in_ult5 = open(current_folder.joinpath('ult5.in'))
    expected_out_ult5 = open(current_folder.joinpath('ult5.out')).read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in_ult5,
        capture_output=True
    ).stdout.decode()

    print('outputs', output)
    assert output.strip().replace("\r\n", "\n") == expected_out_ult5.strip()
