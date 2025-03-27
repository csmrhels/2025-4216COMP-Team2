# Creating a dictionary
members = {
    "Kian": {
        "Question 1": "kian_question1",
        "Question 2": "kian_question2"
    },
    "Connor": {
        "Question 1": "connor_question1",
        "Question 2": "connor_question2"
    },
    "Elliot": {
        "Question 1": "elliot_question1",
        "Question 2": "elliot_question2"
    },
    "Charlotte": {
        "Question 1": "charlotte_question1",
        "Question 2": "charlotte_question2"
    },
    "Ross": {
        "Question 1": "ross_question1",
        "Question 2": "ross_question2"
    },
    "John": {
        "Question 1": "john_question1",
        "Question 2": "john_question2"
    },
    "Lola": {
        "Question 1": "lola_question1",
        "Question 2": "lola_question2"
    },
}

def main_menu():
    """Displays the main menu where the user selects a person or exits."""
    while True:
        print("\n--- Select a person ---")
        
        options = list(members)
        options.append("Exit")

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(members):
                member_name = options[choice - 1]
                print(f"\nYou selected: {member_name}")
                members_menu(member_name)
            elif choice == len(options):
                print("Exiting program...")
                break
            else:
                print("Invalid choice, try again.")
        else:
            print("Invalid input, please enter a number.")

def members_menu(member_name):
    """Displays the menu for a selected member's questions."""
    while True:
        print(f"\n--- {member_name}'s Questions ---")
        
        questions = members[member_name]
        options = list(questions)
        options.append("Go Back") 

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        choice = input("Enter your choice: ")

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(questions):
                question_name = options[choice - 1]
                script_name = questions[question_name]
                
                print(f"\nRunning {script_name}.py...\n")
                exec(open(f"{script_name}.py").read())
                
            elif choice == len(options):
                print("Returning to main menu...")
                break
            else:
                print("Invalid choice, try again.")
        else:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main_menu()
