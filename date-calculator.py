# Create age calculator

import datetime

def main():
    # Get the current date
    today = datetime.date.today()
    # Get the user's birthday
    print("What is your birthday?")
    month = int(input("Month [MM]: "))
    day = int(input("Day [DD]: "))
    year = int(input("Year [YYYY]: "))
    # Calculate the age
    birthday = datetime.date(year, month, day)
    age = today.year - birthday.year
    print("You are {} years old.".format(age))

if __name__ == "__main__":
    main()
