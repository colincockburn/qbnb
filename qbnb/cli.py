from qbnb.models import login, User, register, update_user_profile 
from qbnb.models import create_listing, Listing, update_listing
import datetime


def login_page():
    ''' Requests login information from user. Returns user object from data
    base upon succesful login. returns False if user could not login.
    '''

    # bool keeps loop going until valid email and password found
    valid = False
    while not valid:
        # collect email and password, return false if user enters 3.
        print('enter login info below or enter 3 to exit\n')
        input_email = input('enter email: ')
        if input_email == '3':
            return False
        input_password = input('Please input password: ')
        print()
        # get user from datbase based on email and check password if found
        user = User.query.filter_by(email=input_email).first()
        # email not found. inform user
        if user is None:
            print('email invalid, please try again.\n')
        # email found, check password
        elif user.password == input_password:
            valid = True
        else:
            print('password invalid, please try again\n')

    # loop ending means valid inputs. login with inputs and return user
    return login(input_email, input_password)


def register_page():

    user_id = 0
    # Generate unique id
    for i in range(0, 10000):
        id = User.query.filter_by(user_id=i).first()
        if id is None:
            user_id = id
            break

    # While succesful register hasn't occured prompt user
    while True:

        while True:
            email = input('Please input email or 3 to exit: ')

            if email == '3':
                return False

            input_email = User.query.filter_by(email=email).first()

            # Check that email is unique
            if input_email is None:
                break
            else:
                print("Error: email is already in use")

        # Validate that passowrds match
        while True:
            password = input('Please input password: ')
            password_twice = input('Please input the password again: ')

            if password == password_twice:
                break
            else:
                print("Passwords do no match. Please try again")

        # Validate that username is unique
        while True:
            username = input('Please input username: ')

            input_username = User.query.filter_by(username=username).first()

            if input_username is None:
                break
            else:
                print("Error: username is already in use")
        if register(user_id, username, email, password, "", "", 100):
            print('registration succeeded')
            return login(email, password)
        else:
            print('Registration failed. Please check and re-enter data')

            
def home_page(user):
    '''home page of application accessed after successful log in
    '''
    # loop homepage until user logs out.
    while True:
        print('\nHomepage\n------------- \nPlease select:\n1 - Update'
              ' User\n2 - Create listing\n3 - Update listing\n4 - log '
              'out\n')
        choice = input("enter selection: ")
        if choice == '1':
            profile_update_page(user)
        elif choice == "2":
            create_listing_page(user)
        elif choice == "3":
            update_listing_page(user)
        elif choice == '4':
            print("goodbye")
            exit()
        else:
            print('invalid entry')


def create_listing_page(user):
    ''' let users create a listing. '''

    # get information from user for listing, and add to data base
    while True:
        title = input("enter title of listing: ")
        description = input("please create a description: ")
        address = input("enter address of listing: ")
        while True:
            price = input("enter the price of listing: ")
            if price.isdigit():
                price = int(price)
                break
            else:
                print("must enter a number")
        last_date_modified = datetime.datetime.today()
        # create listing and break loop if successful
        if create_listing(title, user.user_id, 
                          user.email, description, address,
                          last_date_modified, price) == 0:
            break
        # allow user to quit create listing apon unsuccessful attempt
        try_again = input("enter anything to try again or 3 to exit\n")
        if try_again == str(3):
            break


def update_listing_page(user):
    
    # get what listing the user wants to update
    listings = list(Listing.query.filter_by(owner_id=user.user_id))
    print("all of your listings: ")
    index = 1
    for i in listings:
        print("    ", index, ". ", i.listing_title)
        index += 1
    while True:
        choice = input("enter the number corresponding to a listing: ")
        if not choice.isdigit():
            print("invalid entry\n")
        elif int(choice) < 1 or int(choice) > index - 1:
            print("invalid entry\n")
        else:
            to_update = listings[int(choice) - 1]
            break

    new_title = None
    new_description = None
    new_address = None
    new_price = None

    # get new info
    if input("change title? y/n: ") == "y":
        new_title = input("enter  new title: ")
    if input("change description? y/n: ") == "y":
        new_description = input("enter new description: ") 
    if input("change address? y/n: ") == "y":
        new_address = input("enter new address: ")
    # loop back if a non-int str is entered 
    while True:
        if input("change price? y/n: ") == "y":
            print("price must be larger than ", str(to_update.price))
            new_price = input("enter new price: ")
            if new_price.isdigit():
                new_price = int(new_price)
                break
            else:
                print("invalid entry. must enter a integer")
                new_price = None
        else:
            break
    if new_title is None:
        new_title = to_update.listing_title
    if new_description is None:
        new_description = to_update.description
    if new_address is None:
        new_address = to_update.address
    if new_price is None:
        new_price = to_update.price         

    # update with new info
    if update_listing(to_update.listing_id, new_title, to_update.
                      owner_email, new_description, new_address, 
                      new_price) != 0:
        print("failed to update listing due to invalid entries\n")


def profile_update_page(user):
    ''' Allows user to update their user. takes user object as\
    parameter and returns nothing. 
    '''

    print("Welcome to the profile update page")
    print("----------------------------------")
    # loop until user gets updated or user exits
    invalid = True
    while invalid:
        tmp_username, tmp_email, tmp_shipping, tmp_postal =\
            user.username, user.email,\
            user.billing_address, user.postal_code

        # get any new info that needs to be updated
        update_info = input(('Would you like to make changes '
                            'to your account information (y/n)? '))
        if update_info != 'y':
            break
        new_user = input('Would you like to change your usernmae (y/n)?')
        if (new_user == 'y'):
            tmp_username = input('Please enter your new username: ')
        new_email = input('Would you like to change your email (y/n)? ')
        if (new_email == 'y'):
            tmp_email = input('Please enter your new email: ')
        new_shipping = input('Would you like to change your address'
                             ' (y/n)? ')
        if (new_shipping == 'y'):
            tmp_shipping = input('Please enter your new shipping address: ')
        new_postal = input('Would you like to change your postal code'
                           '(y/n)? ')
        if (new_postal == 'y'):
            tmp_postal = input('Please enter your new postal code: ')

        # update user object with new info
        valid_update = update_user_profile(user.username, tmp_username,
                                           user.email, tmp_email,
                                           user.billing_address,
                                           tmp_shipping, tmp_postal)

        if valid_update:
            invalid = False
            print("Your updates have been made!")
            break
        else:
            print("could not update profile. invalid inputs")
