import unittest
from qbnb.models import create_listing,\
    Listing, User, db, update_listing, register, login
from qbnb_test.conftest import pytest_sessionstart
import datetime

# prepare enviroment for testing
pytest_sessionstart()
db.create_all()
# create a user and listing for tests.
user = User(user_id=5678, email="email@string.com",
            password="Led$Zepp67547", username='username', balance=100)
listing = Listing(listing_id=1234, listing_title='title',
                  owner_id=5678, owner_email='email',
                  description='32 characters are in this string',
                  address='123 address lane',
                  last_date_modified=datetime.datetime.today(), price=150)

# Import SQL Injection payload
test_file = open('Generic_SQLI.txt')

# add user and listing to database
db.session.add(user)
db.session.add(listing)
db.session.commit()


def test_create_listing_control():
    ''' tests creating a valid listing '''
    assert create_listing('different title', 5678, 'email',
                          '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 100) == 0


def test_create_listing_R4_1():
    ''' tests for title not alphanumeric'''
    assert create_listing('different title$', 5678, 'email',
                          '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 100) == 1


def test_create_listing_R4_2():
    ''' tests for title longer than 80 characters but still shorter than
    description
    '''
    assert create_listing
    ('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\
     iiiiiiiiiiiiii', 5678, 'email', 'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\
     iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', 'addy',
     datetime.datetime.today(), 100) == 1


def test_create_listing_R4_3():
    ''' tests description not in range of 20 - 2000'''
    assert create_listing('different title', 5678, 'email', 'short desc',
                          'addy', datetime.datetime.today(), 100) == 1


def test_create_listing_R4_4():
    ''' tests descripton shorter than title'''
    assert create_listing(' 33 characters are in this string', 5678,
                          'email', '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 100) == 1


def test_create_listing_R4_5():
    ''' tests price out of range 10-10000'''
    assert create_listing('different title', 5678, 'email',
                          '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 9) == 1


def test_create_listing_R4_6():
    ''' tests for date_last_modified out of range '''
    assert create_listing('different title', 5678, 'email',
                          '32 characters are in this string', 'addy',
                          datetime.datetime(2020, 1, 2), 100) == 1


def test_create_listing_R4_7():
    ''' tests owner email empty'''
    assert create_listing('different title', 5678, '',
                          '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 100) == 1

    ''' tests owner does not exist in database'''
    assert create_listing('different title', 2000, 'email',
                          '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 100) == 1


def test_create_listing_R4_8():
    ''' tests user creating listing with same name as another listing owned
    by this user
    '''
    assert create_listing('title', 5678, 'email',
                          '32 characters are in this string', 'addy',
                          datetime.datetime.today(), 100) == 1


# Testing string for update listing
description = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


class updateListingErrors(unittest.TestCase):
    """Test whether update_listing correctly throws errors and updates data"""

    def test_1(self):
        """Test user updating listing with nonexisting id"""

        with self.assertRaises(Exception):
            update_listing(-1, "title", "email", description, "address", 150)

    def test_2(self):
        """Test user inputs integer for listing_id"""

        with self.assertRaises(TypeError):
            update_listing("string", "title", "email", "description", 
                           "address", 150)

    def test_3(self):
        """Test user inputs alphanumeric string without spaces at prefix or
        suffix R4-1
        """

        with self.assertRaises(TypeError):
            update_listing(" das", 1, "email", description, "address", 150)

    def test_4(self):
        """Test user inputs string for email"""

        with self.assertRaises(TypeError):
            update_listing(1234, "title", 1, description, "address", 150)

    def test_5(self):
        """Test user inputs string for description"""

        with self.assertRaises(TypeError):
            update_listing(1234, "title", "email", 1, "address", 150)

    def test_6(self):
        """Test user inputs integer for price"""

        with self.assertRaises(TypeError):
            update_listing(1234, "title", "email", description, "address",
                           "Price")

    def test_7(self):
        """Tests if listing title is greater than 80 characters R4-2"""

        with self.assertRaises(Exception):
            update_listing(1234, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                           "email", description, "address", 150)

    def test_8(self):
        """Test if email is greater than 120 characters"""

        with self.assertRaises(Exception):
            update_listing(1234, "title", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 
                           "description", "address", 150)

    def test_9(self):
        """Test if description is greater than 2000 characters R4-3"""

        long_string = "a"
        for i in range(0, 2000):
            long_string = long_string + "a"

        with self.assertRaises(Exception):
            update_listing(1234, "title", "email", long_string, "address", 150)

    def test_10(self):
        """Test if address exceeds 80 characters"""

        with self.assertRaises(Exception):
            update_listing(1234, "title", "email", description, "aaaaaaa\
                           aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
                           aaaaaaaaaaaaaaaaaaaaaaaaaa", 150)

    def test_11(self):
        """Test if price is decreased R5-2"""

        with self.assertRaises(Exception):
            update_listing(1234, "title", "email", description, "address", 0)

    def test_12(self):
        """Test if description is longer than product's title R4-4"""
         
        with self.assertRaises(Exception):
            update_listing(1234, "title", "email", "des", "address", 150)

    def test_13(self):
        """Test if price is in range of 10-10,000 R4-5"""

        with self.assertRaises(Exception):
            update_listing(1234, "title", "email", description, "address",
                           11111)

    def test_14(self):
        """Test if email is empty R4-7"""

        with self.assertRaises(Exception):
            update_listing(1234, "title", "", description, "address", 150)

    def test_15(self):
        """Test if modified date properly updates R5-3"""

        assert listing.last_date_modified.replace(microsecond=0) ==\
            datetime.datetime.today().replace(microsecond=0)

    def test_16(self):
        """Test if data updated succesfully R5-1"""

        update_listing(1234, "title", "email", description,
                       "address", 175)

        # Get final listing
        final_listing = Listing.query.filter_by(listing_id=1234).first()

        assert (final_listing.listing_title == "title" and
                final_listing.owner_email == "email" and
                final_listing.description == description
                and final_listing.address == "address" and 
                final_listing.price == 175)


def test_r1_1_user_register():
    """Email and password cannot be empty"""

    assert register(178659, "maxlindsay", "",
                    "", "", "", 100) is False


def test_r1_2_user_register():
    """Unique ID number test"""

    assert register(2847271, "vinnysmalls", "vinnymandolorian@bing.com",
                    "CocA&Cola42", "", "", 100) is True


def test_r1_3_user_register():
    """Email formatting test"""

    assert register(582364, "davidgilmour",
                    "davidfloyd@hotmailcom", "TheWall$", "", "", 100) is False


def test_r1_4_user_register():
    """Password complexity requirements test"""

    assert register(58285927, "kirkhammett", "wahpedalz@gmail.com",
                    "queens53$", "", "", 100) is False


def test_r1_5_user_register():
    """Username requirements test"""

    assert register(654321, "", "therealsugashow@gmail.com",
                    "FlashyKickz$", "", "", 100) is False


def test_r1_6_user_register():
    """Username length test"""

    assert register(46992, "abcdefghijklmnopqrst", "californication@gmail.com",
                    "StellAtheBulldog!", "", "", 100) is False


def test_r1_7_user_register():
    """Unique email test"""

    assert register(8898989, "maxlindsay4235",
                    "maxlindsay@gmail.com", "GoKingsGo2$", "", "", 100) is True


def test_r1_8_user_register():
    """Shipping address is empty at registration"""

    assert register(243, "maxlindsay28", "llindsay@gmail.com",
                    "BigPoppa#", "a", "", 100) is False


def test_r1_9_user_register():
    """Postal code is empty at registration"""

    assert register(99, "jeffsmith", "jeffsmith@gmail.com",
                    "TupAcShakur!", "", "a", 100) is False


def test_r1_10_user_register():
    """Balance initialized to 100 at registration"""

    assert register(1000000, "rick ross", "rossrick@bing.com",
                    "Led$Zepp67547", "", "", 3500) is False


def test_login_R2_1():
    """tests that user can log in with his/her email and password"""

    user2 = login('email@string.com', 'Led$Zepp67547')
    assert user2.email == 'email@string.com'


def test_login_R2_2_1():
    """tests when email is incorrect"""

    assert login('test2@test.com', '123456') is False


def test_login_R2_2_2():
    """tests when password is incorrect"""

    assert login('test2@test.com', '123456') is False


def test_login_R2_2_3():
    """tests if email is empty"""

    assert login('', 123456) is False


def test_login_R2_2_4():
    """tests is password is empty"""

    assert login('test2@test.com', '') is False


# SQL Injection Testing
def test_sqli_listing_title():
    """Tests if the listing title fails an SQLI test"""
    count = 0
    
    while True:
        count += 1
        line = test_file.readline()     # Setting readLine to test
        try:
            assert create_listing(line, listing.owner_id, listing.owner_email,
                                  listing.description, listing.address, 
                                  listing.last_date_modified, listing.price)
        except IndexError as err:       # Expected error handling
            print(err)
        if not line:    # Reached EOF
            break


def test_sqli_owner_id():
    """Tests if the owner ID fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        assert create_listing(listing.listing_title, line, listing.owner_email,
                              listing.description, listing.address, 
                              listing.last_date_modified, listing.price)
        if not line:
            break


def test_sqli_owner_email():
    """Tests if the listing owner email an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        assert create_listing(listing.listing_title, listing.owner_id, line,
                              listing.description, listing.address,
                              listing.last_date_modified, listing.price)
        if not line:
            break


def test_sqli_description():
    """Tests if the descripton fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        assert create_listing(listing.listing_title, listing.owner_id,
                              listing.owner_email, line,
                              listing.address,
                              listing.last_date_modified, listing.price)
        if not line:
            break


def test_sqli_address():
    """Tests if the address fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        assert create_listing(listing.listing_title, listing.owner_id,
                              listing.owner_email, listing.description,
                              line, listing.last_date_modified,
                              listing.price)
        if not line:
            break


def test_sqli_last_modified():
    """Tests if the last modified field fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert create_listing(listing.listing_title, listing.owner_id,
                                  listing.owner_email, listing.description,
                                  listing.address, line, listing.price)
        except TypeError as err:
            print(err)
        if not line:
            break


def test_sqli_price():
    """Tests if the price input fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert create_listing(listing.listing_title, listing.owner_id,
                                  listing.owner_email, listing.description,
                                  listing.address, listing.last_date_modified,
                                  line)
        except TypeError as err:
            print(err)
        if not line:
            break


def test_sqli_register_id():
    """Tests if the register ID fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert register(line, user.email, user.password, 
                            user, user.billing_address, 
                            user.postal_code, user.balance)

        except TypeError as err:
            print(err)
        if not line:
            break


def test_sqli_register_email():
    """Tests if the register email fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert register(user.user_id, line, user.password, 
                            user, user.billing_address, 
                            user.postal_code, user.balance)

        except TypeError as err:
            print(err)
        if not line:
            break


def test_sqli_register_address():
    """Tests if the register address fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert register(user.user_id, user.email, user.password, 
                            user, line, 
                            user.postal_code, user.balance)

        except TypeError as err:
            print(err)
        if not line:
            break


def test_sqli_register_postal_code():
    """Tests if the register postal code fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert register(user.user_id, user.email, user.password, 
                            user, user.billing_address, 
                            line, user.balance)

        except TypeError as err:
            print(err)
        if not line:
            break


def test_sqli_register_balance():
    """Tests if the register email fails an SQLI test"""
    count = 0

    while True:
        count += 1
        line = test_file.readline()
        try:
            assert register(user.user_id, user.email, user.password, 
                            user, user.billing_address, 
                            user.postal_code, line)

        except TypeError as err:
            print(err)
        if not line:
            break


if __name__ == '__main__':
    unittest.main()
