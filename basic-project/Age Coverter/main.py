from datetime import datetime

def get_age():
    birthdate = input("Enter your birthday (Month-Day-Year) Please include the dash: ")
    birthdate = datetime.strptime(birthdate, "%m-%d-%Y")
    now = datetime.now()
    age = now - birthdate
    current_age = now.year - birthdate.year - ((now.month,now.day)<(birthdate.month,birthdate.day))
    print("You are {} years old".format(current_age))
    return age

def get_days(age):
    days = age.days
    hours , remainder = divmod(age.seconds,3600)
    minutes, seconds = divmod(remainder, 60)
    print("You have lived for {} days, {} hours , {} minutes, {} seconds".format(days,hours,minutes,seconds))
    return days, hours, minutes, seconds

def get_hours(age):
    hours, remainder= divmod(age.total_seconds(),3600)
    minutes, _ = divmod(remainder , 60)
    print("You have lived for {} hours and {} minutes".format(hours,minutes))
'''
HOMEWORK:
Create  a function to return your age in only minutes 
Add the function to the menu
Hint: 3600 seconds = 60 minutes, 60 seconds  = 1 minute
'''
def run():
    age = get_age()
    while True:
        choice =input("""
            How would you like your age?
            1. Days
            2.Hours
            4.Quit
            Enter the number: 
            """)
        if choice == "4":
            quit(0)
        elif choice == "1":
            get_days(age)
        elif choice == "2":
            get_hours(age)
        elif choice == "3":
            pass
        else:
            print("Not a valid choice")
            
            

    