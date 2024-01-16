daysDecode = {
    "MON": "Monday",
    "TUE": "Tuesday",
    "WED": "Wednesday",
    "THU": "Thursday",
    "FRI": "Friday",
    "SAT": "Saturday",
    "SUN": "Sunday"
}

def welcomeMessage():

    # Intro
    print("Welcome to the Meeting Scheduler App!".upper())
    print("-------------------------------------------------------------")
    print("This app is designed to help you and another person organize a meeting.")
    print("You can input your availability for a specific day and mark the times when you're not available.")
    print("The app will find a suitable time for the meeting based on the overlapping available slots.")
    print("Let's get started!")

    # Instructions
    print("\nInstructions:")
    print("1. Choose a specific day that suits both participants.")
    print("2. Enter your/your friend's availability for that day.")
    print("3. Mark the times when you are not available.")
    print("4. Schedule the meeting and get ready for a productive discussion!")
    print("\n")

def handleInput():
    available_day=None

    # DAY
    while available_day not in daysDecode:
        print("Which day suits best for you?\n")
        print("| MON | TUE | WED | THU | FRI | SAT | SUN |\n")
        available_day = input("Choose one day: ").upper()

        if available_day not in daysDecode:
            print("\nInvalid input. Please choose a valid day.\n")

    print(f"\n{daysDecode[available_day]} sounds like a good day to meet!\n")

    # TIME
    
    # USER 1
    print("I guess that your work day is from 8:00A.M. to 8P.M.\n")
    print("Enter start time and end time of unavalible time period in the following format:")
    print("Start time: 8:00")
    print("End time: 10:00")

    #USER 2


    



    

