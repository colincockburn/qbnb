from qbnb import app
from flask_sqlalchemy import SQLAlchemy
import datetime
import random
from datetime import date

# setting up SQLAlchemy and data models so we can map data
# models into database tables
db = SQLAlchemy(app)
app.app_context().push()


class User(db.Model):
    """Stores user data such as user_id, username and email"""
    user_id = db.Column(db.Integer, unique=True, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    billing_address = db.Column(db.String(80), nullable=True)
    postal_code = db.Column(db.String(7), nullable=True)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Transaction(db.Model):
    """Stores transaction data such as value, checkin/checkout dates
    and the repsective listing and user ids
    """
    transaction_id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer)
    value = db.Column(db.Float)
    listing_id = db.Column(db.String(120), nullable=False)
    # dates are of form dd-mm-yyyy
    transaction_date = db.Column(db.DateTime)
    checkin_date = db.Column(db.DateTime)
    checkout_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Transaction %r>' % self.transaction_id


class Review(db.Model):
    """reviews entity for verified guests of listings"""
    # primary key is ID number for review
    review_id = db.Column(db.Integer, unique=True, primary_key=True)
    # the id number of the listing the review is about
    listing_id = db.Column(db.Integer, nullable=False)
    # the username of the author for the review
    user_id = db.Column(db.Integer, nullable=False)
    # the title of the review
    title = db.Column(db.String(80), nullable=False)
    # contents of the review
    text = db.Column(db.String(250), nullable=False)
    # a float rating from 1-5
    rating = db.Column(db.Float, nullable=False)
    # date review was made
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Review %r>' % self.title


class Listing(db.Model):
    """
    The property listing database model
    Parameters:
        listing_id: An int representing the property
        listing_title: String representing the listing title
        owner_id: An int representing the id of the property seller
        owner_email: email of the listing owner
        description: a String describing the listing
        address: A string of the properties address
        last_date_modified: dates of form dd-mm-yyyy representing the last
            time the listing was modifed
        price: An int of the properties price
    """
    listing_id = db.Column(db.Integer, unique=True, primary_key=True)
    listing_title = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.String(80), nullable=False)
    owner_email = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    last_date_modified = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Listing %r>' % self.listing_id


class Balance(db.Model):
    """ Stores account data such as account
    balance and deposit/withdrawl amounts
    """
    # id number that the account balance will be added to
    user_id = db.Column(
        db.Integer, unique=True, nullable=False, primary_key=True)
    # users banking information
    card_number = db.Column(db.Integer, nullable=False)
    # the current total within the users account
    account_balance = db.Column(db.Float, default=0)
    # withdrawls/deposits -- withdrawls <= account_balance
    deposit = db.Column(db.Float, default=0)
    withdrawl = db.Column(db.Float, default=0)

    def __repr__(self):
        return '<Balance %r>' % self.account_balance


# create all tables
db.create_all()


def create_listing(listing_title,
                   owner_id, owner_email, description, address,
                   last_date_modified, price):
    """ only takes neccesary parameters, compares against constraints, and
    adds to database if valid.
    parameters: all required fields of listing object
    returns 0 if valid listing parameters
    returns 1 if invalid listing parameters
    """
    # return value, changes to 1 if error found.
    valid = 0
    # R4-1: The title of the product has to be alphanumeric-only,
    # and space allowed only if it is not as prefix and suffix.
    for c in listing_title:
        if not c.isalnum() and c != ' ':
            print("invalid characters in listing title. \
must include alphanumerics only.\n")
<<<<<<< HEAD
            valid = -1
    if listing_title[0] == " " or listing_title[-1] == " ":
        print("Listing title must be alphanumeric without spaces at\
                        suffix or prefix")
        valid = -1
=======
            valid = 1
    if listing_title[0] == " " or listing_title[-1] == " ":
        print("Listing title must be alphanumeric without spaces at\
                        suffix or prefix")
        valid = 1
>>>>>>> 28500add2f88197092ca5e17ff841542de8b562c
    # R4-2: The title of the product is no longer than 80 characters.
    listing_title_len = len(listing_title)
    if listing_title_len > 80:
        print("listing title must be 80 characters or less")
        print("current size = ", listing_title_len, '\n')
        valid = 1
    # R4-3: The description of the product can be arbitrary characters with
    # a minimum length of 20 characters and a maximum of 2000 characters.
    description_len = len(description)
    if description_len < 20 or description_len > 2000:
        print("description length must be between 20 and 2000 characters")
        print("current size = ", description_len, '\n')
        valid = 1
    # R4-4: Description has to be longer than the product's title.
    if description_len <= listing_title_len:
        print("description length must be greater than title length\n")
        valid = 1
    # R4-5: Price has to be of range [10, 10000].
    if price > 10000 or price < 10:
        print("price must be between $10 and $10,000\n")
        valid = 1
    # R4-6: last_modified_date must be after 2021-01-02 and before
    # 2025-01-02.
    if last_date_modified < datetime.datetime(2021, 1, 2)\
       or last_date_modified > datetime.datetime(2025, 1, 2):
        print("last_modified_date must be after \
              2021-01-02 and before 2025-01-02\n")
        valid = 1
    # R4-7: owner_email cannot be empty.
    if len(owner_email) == 0:
        print("owner email cannot be empty\n")
        valid = 1
    # R4-7: The owner of the corresponding product must exist in the database.
    found_owner = User.query.filter_by(user_id=owner_id).first()
    if not found_owner:
        print('this owner does not exist\n')
        valid = 1
    # R4-8: A user cannot create products that have the same title.
        # loop through each listing, if the user id and title are the same ,
    listings = Listing.query.filter_by(owner_id=owner_id).all()
    for l_id in listings:
        if l_id.listing_title == listing_title:
            print('this owner already has a listing with this title\n')
            valid = 1
            break
    # if a constraint was violated, return 1
    if valid == 1:
        return 1
    # create a uniqe listing id
    listing_id = random.randint(0, 9999)
    same_id = Listing.query.filter_by(listing_id=listing_id).first()
    while same_id is not None:
        listing_id = random.randint(0, 9999)
        same_id = User.query.filter_by(listing_id=listing_id).first()

    # all data valid, create listing
    listing = Listing(listing_id=listing_id,
                      listing_title=listing_title, owner_id=owner_id,
                      owner_email=owner_email, description=description,
                      address=address, last_date_modified=last_date_modified,
                      price=price)
    # add listing
    db.session.add(listing)
    # commit listing to database
    db.session.commit()

    return 0


def update_listing(listing_id: int, listing_title: str, owner_email: str,

                   description: str, address: str, price: int):
    """Updates listing data for given listing_id. Price can only be increased.
    Last modified date is updated on succesful update.
    """

    # Ensure passed arguments are of correct data types
    if (not isinstance(listing_id, int)):
        raise TypeError("Entered value for listing_id is not of type int")

    if (not isinstance(listing_title, str)):
        raise TypeError("Enterd value for listing_title is not of type str")

    # Ensure title is alphanumeric with spaces only not at prefix or suffix
    if listing_title[0] == " " or listing_title[-1] == " ":
        raise TypeError("Listing title must be alphanumeric without spaces at\
                        suffix or prefix")
    for c in listing_title:
        if not c.isalnum() and c != ' ':
            raise TypeError("Listing title must be only be alphanumeric\
                            characters")

    if (not isinstance(owner_email, str)):
        raise TypeError("Enterd value for owner_email is not of type str")

    if (not isinstance(description, str)):
        raise TypeError("Enterd value for description is not of type str")

    if (not isinstance(address, str)):
        raise TypeError("Enterd value for address is not str")

    if (not isinstance(price, int)):
        raise TypeError("Entered value for price is not int")

    # Get current data for given id
    listing = Listing.query.filter_by(listing_id=listing_id).first()

    # Ensure listing exists
    if listing is None:
        raise Exception("There is no listing for the entered listing_id")

    if (len(listing_title) > 80):
        raise Exception("Value for listing_title exceeds 80 characters")

    # Ensure new listing titles are unique
    if (listing_title != listing.listing_title and
       Listing.query.filter_by(listing_id=listing_id).first() is None):
        raise Exception("Listing title already exists")

    if (len(owner_email) > 120):
        raise Exception("Value for owner_email exceeds 120 characters")

    if owner_email == "":
        raise Exception("Owner email cannot be empty")

    # Ensure description is between 20-2000 characters
    if len(description) < 20 or len(description) > 2000:
        raise Exception("Value for description exceeds 2000 characters or is\
                        less than 20 characters")

    # Ensure description is longer than listing title
    if len(description) <= len(listing_title):
        raise Exception("Description must be longer than listing title")

    if (len(address) > 80):
        raise Exception("Value for address exceeds 80 characters")

    # Ensure price is between 10-10,000
    if (price < 10 or price > 10000):
        raise Exception("Price has to be in range of 10-10,000")

    # Ensure price cannot be updated to lower value
    if (price < listing.price):
        raise Exception("Price cannot be lowered")

    # Update data
    listing.listing_title = listing_title
    listing.owner_email = owner_email
    listing.description = description
    listing.address = address
    listing.last_date_modified = datetime.datetime.today()
    listing.price = price

    db.session.commit()
    return 0


def register(id, name, email, password, shipping, postal, balance):
    '''
    Function that handles account registration and ensures proper information
    is being collected into database.
    Parameters:
        id  (int):         user identification number (unique)
        name (string):     user username
        email (string):    user email (unique)
        password (string): user password
        shipping (string): user shipping address
        postal (string):   user postal code
        balance (int):     user account money balance
    Returns:
        True and adds the new user to the database if successful
    '''

    # Requirement R1-1: Email and password can't be empty
    if len(email) == 0 or len(password) == 0:
        return False

    # Requirement R2-2: ID # must be unique
    uniqueID = User.query.filter_by(user_id=id).all()
    if (len(uniqueID) > 0):
        return False

    # Symbol list used to check invalidity
    special_chars = {'!', '#', '$', '%', '&', "'", '*', '+', '/', '=', '?',
                     '^', '_', '`', '{', '|', '}', '~', '"', '(', ')', ':',
                     ';', '<', '>', '@', '[', '\\', ']'}

    # Requirement R1-3: Email is in valid format

    if '@' not in email:
        return False

    splitter = email.index('@')  # Separating local handle and domain for tests
    local = email[:splitter]
    domain = email[splitter + 1:]

    if '.' not in domain:
        return False

    for i in special_chars:  # If domain has a special char, fail
        if i in domain:
            return False

    if len(local) > 64 or len(domain) > 255:  # Maximum email component lengths
        return False

    if local[0] != '"' and local[-1] != '"':    # Unquoted email rules
        # None of these symbols allowed
        if ('@' in local or '[' in local or ']' in local
                or '<' in local or '>' in local or '\\' in local
                or ':' in local or ';' in local or '"' in local
                or ',' in local):
            return False

        if '.' in local:    # Can't have two periods in a row in local handle
            if local[local.index('.') - 1] == '.':
                return False
            if local[local.index('.') + 1] == '.':
                return False

    # Requirement R1-4: Password complexity requirements
    if (len(password) < 6
            or any(x.isupper() for x in password) is False):
        return False
    if any(x.islower() for x in password) is False:
        return False

    flag = False        # Password has a special char validation
    for i in password:
        if i in special_chars:
            flag = True
    if flag is False:
        return False

    # Requirement R1-5: Username requirements
    # Non-zero length, can't start or end with a space
    if len(name) == 0 or name[0] == ' ' or name[-1] == ' ':
        return False

    flag = True
    for j in name:      # Username doesn't have special char validation
        if j in special_chars:
            flag = False
    if flag is False:
        return False

    # Requirement R1-6: Username length has to be 2<n<20
    if len(name) <= 2 or len(name) >= 20:
        return False

    # Requirement R1-7: Email has to be unique
    unique_mail = User.query.filter_by(email=email).all()
    if (len(unique_mail) > 0):
        return False

    # Requirement R1-8: Shipping address has to start empty
    if len(shipping) > 0:
        return False

    # Requirement R1-9: Postal code has to start empty
    if len(postal) > 0:
        return False

    # Requirement R1-10: Balance has to start at n=100
    if balance != 100:
        return False

    user = User(user_id=id, username=name, email=email, password=password,
                billing_address=shipping, postal_code=postal, balance=balance)
    db.session.add(user)
    db.session.commit()

    # Passed all the requirements, valid registration
    return True


def login(email, password):
    """ Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    """

    # Requirement R2-2: Checks email and password requirement
    # Refer to line 319
    if '@' not in email:
        return False

    splitter = email.index('@')

    local = email[:splitter]
    domain = email[splitter + 1:]

    if '.' not in domain:
        return False

    if len(local) > 64 or len(domain) > 255:
        return False

    if local[0] != '"' and local[-1] != '"':  # Unquoted email rules
        # None of these symbols allowed
        if ('@' in local or '[' in local or ']' in local
                or '<' in local or '>' in local or '\\' in local
                or ':' in local or ';' in local or '"' in local
                or ',' in local):
            return False

    # Password rules
    if len(password) < 6 or any(x.isupper() for x in password)\
            is False or any(x.islower() for x in password)\
            is False or any(x.isalnum() for x in password) is False:
        return False

    # Requirement R2-1: User can log in with email and password
    valids = User.query.filter_by(email=email,).all()
    if len(valids) != 1:
        return None
    return valids[0]


def update_user_profile(username, new_username, user_email,
                        new_user_email, billing_address,
                        new_billing_address, new_postal_code):
    """ takes username, email, billing address and postal code as the
    parameters to be able to be changed.
    returns not none if vaild and updates
    returns none if in-vaild and does not update
    """

    special_chars = {'!', '#', '$', '%', '&', "'", '*', '+', '/', '=', '?',
                     '^', '_', '`', '{', '|', '}', '~', '"', '(', ')', ':',
                     ';', '<', '>', '@', '[', '\\', ']'}

    # Refer to line 319\
    if new_user_email != '':

        if '@' not in new_user_email:
            return False

        splitter = new_user_email.index('@')

        local = new_user_email[:splitter]
        domain = new_user_email[splitter + 1:]

        if '.' not in domain:
            return False

        if len(local) > 64 or len(domain) > 255:
            return False

        if local[0] != '"' and local[-1] != '"':  # Unquoted email rules
            # None of these symbols allowed
            if ('@' in local or '[' in local or ']' in local
                or '<' in local or '>' in local or '\\' in local
                or ':' in local or ';' in local or '"' in
                    local or ',' in local):
                return False

    # R3-2 & R3-3 : checks if new_postal_code is valid
    if len(new_postal_code) != 7:
        return False

    if not new_postal_code[0].isalpha():
        return False

    if not new_postal_code[1] in "0123456789":
        return False

    if not new_postal_code[2].isalpha():
        return False

    if not new_postal_code[3] != '':
        return False

    if not new_postal_code[4] in "0123456789":
        return False

    if not new_postal_code[5].isalpha():
        return False

    if not new_postal_code[6] in "0123456789":
        return False

    # R3-4 : username constraints must be met on new_username
    if new_username != '':

        if (len(new_username) == 0 or new_username[0] == ' ' or
                new_username[-1] == ' '):
            return False

        flag = True
        for j in new_username:      # New name doesn't have special char check
            if j in special_chars:
                flag = False
        if flag is False:
            return False

        # Requirement R1-6: Username length has to be 2<n<20
        if len(new_username) <= 2 or len(new_username) >= 20:
            return False

    user = User.query.filter_by(username=username).first()

    # must provide current and new parameters to update current parameters
    if username and new_username is not None:
        user.username = new_username

    else:
        user.username = username

    if user_email and new_user_email is not None:
        user.email = new_user_email

    if billing_address and new_billing_address is not None:
        user.billing_address = new_billing_address

    if new_postal_code is not None:
        user.postal_code = new_postal_code

    db.session.commit()
    return True
