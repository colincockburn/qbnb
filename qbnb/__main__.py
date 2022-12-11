from sqlite3 import register_adapter
from qbnb import *
from qbnb.models import *
from qbnb.cli import login_page, profile_update_page, register_page,\
    home_page, create_listing_page, update_listing_page


def main():
    while True:
        selection = int(input(
            'Welcome. Please type 1 to login. '
            'Or type 2 register. Or type 3 to exit: '))
        while selection not in range(1, 4):
            selection = int(input('invalid entry, try again: '))
        print()
        # user wants to login
        if selection == 1:
            # get user object from login info
            user = login_page()

        # user wants to register
        elif selection == 2:
            # get user object once created in register page
            user = register_page()

        elif selection == 3:
            print('goodbye')
            exit()

        # login in to user
        if user:
            print(f'welcome {user.username}')
            home_page(user)
        else:
            print("user not found")


if __name__ == '__main__':
    main()
