'''A-z portal, its a basic 5 things portal'''
activity_score = 0
login = False

while True:

    print("\nWelcome")
    print("Here you can find all functionalities listed below:")
    print("1.Login/Register")
    print("2.Readings")
    print("3.Games")
    print("4.Quiz")
    print("5.Scorecard")
    print("6.Exit")

    choice = int(input("Enter a choice: "))

    match choice:

        
        case 1:

            print("-----LOGIN/REGISTER-----")

            askk = input("Enter login/register: ").lower()

            if askk == "login":

                username = input("Enter Username: ")
                password = input("Enter password: ")

                if username == "user1" and password == "1234":

                    print("Login Successful")
                    login = True

                else:
                    print("Invalid username/password")

            else:

                name = input("Enter name: ")
                age = input("Enter age: ")
                mob_no = int(input("Enter mobile number: "))

                print("OTP sent")

                otp = input("Enter otp: ")

                if otp == "12345":

                    print("Verification successful")
                    print("Login done")

                    login = True

                else:

                    for i in range(3):

                        otp = input("Enter otp again: ")

                        if otp == "12345":

                            print("Verification successful")
                            print("Login done")

                            login = True
                            break

                    else:
                        print("Failed 3 times")

       

        case 2:

            if login == True:

                while True:

                    print("\n-----READINGS MENU-----")
                    print("1.Thoughts")
                    print("2.Books")
                    print("3.Shayari")
                    print("4.Exit")

                    ch = int(input("Enter readings type: "))

                    match ch:

                        case 1:

                            print("\nThought:")
                            print("“Success doesn’t come from motivation alone, it comes from consistency.”")

                            activity_score += 5

                            ask = input("Want more(yes/no): ").lower()

                            if ask == "yes":

                                print("\n“Your future is created by what you do today, not tomorrow.”")

                                activity_score += 5

                            else:
                                print("Thankyou")

                       

                        case 2:

                            print("\nAvailable books:")
                            print("1.Atomic Habits")
                            print("2.The Alchemist")
                            print("3.Rich Dad Poor Dad")

                            ask2 = input("Give book name: ").lower()

                            if ask2 == "atomic habits" or ask2 == "the alchemist" or ask2 == "rich dad poor dad":

                                print("Download successful")

                                activity_score += 10

                            else:
                                print("Book not available")

                      

                        case 3:

                            print("\n“Sabhi ka khoon hai shamil yahan ki mitti mein,")
                            print("Kisi ke baap ka Hindustan thodi hai.”")

                            activity_score += 5

                            ask3 = input("Do you want more(yes/no): ").lower()

                            if ask3 == "yes":

                                print("\n“Roz taaron ko numaish mein khalal padta hai,")
                                print("Chand pagal hai andhere mein nikal padta hai.”")

                                print("\n“Main jab mar jaun meri alag pehchaan likh dena,")
                                print("Lahu se meri peshani pe Hindustan likh dena.”")

                                activity_score += 5

                            else:
                                print("Thank you")

                        case 4:

                            print("Exiting readings")
                            break

                        case _:
                            print("Invalid input")

            else:
                print("Please login first")

        case 3:

            if login == True:

                while True:

                    print("\n-----GAMES MENU-----")
                    print("1.Guess Number")
                    print("2.Rock Paper Scissors")
                    print("3.Exit")

                    game = int(input("Enter your choice: "))

                    match game:

                        case 1:

                            secret = 7

                            guess = int(input("Guess a number between 1-10: "))

                            if guess == secret:

                                print("Correct Guess")

                                activity_score += 10

                            else:
                                print("Wrong Guess")

                        case 2:

                            user = input("Enter rock/paper/scissors: ").lower()

                            computer = "rock"

                            if user == computer:

                                print("Match Draw")

                            elif user == "paper":

                                print("You Win")

                                activity_score += 10

                            else:
                                print("Computer Wins")

                        case 3:

                            print("Exiting games")
                            break

                        case _:
                            print("Invalid input")

            else:
                print("Please login first")

        case 4:

            if login == True:

                print("\n-----QUIZ-----")

                print("Q1. Capital of India")
                ans1 = input("Enter answer: ").lower()

                if ans1 == "delhi":

                    print("Correct")

                    activity_score += 10

                else:
                    print("Wrong")

                print("\nQ2. Python is a ?")
                ans2 = input("Enter answer: ").lower()

                if ans2 == "language":

                    print("Correct")

                    activity_score += 10

                else:
                    print("Wrong")

            else:
                print("Please login first")

        case 5:

            if login == True:

                print("\n-----SCORECARD-----")

                print("Your activity score is =", activity_score)

                if activity_score >= 40:

                    print("Excellent Performance")

                elif activity_score >= 20:

                    print("Good Performance")

                else:

                    print("Need Improvement")

            else:
                print("Please login first")

        case 6:

            print("Thankyou for using A-z Portal")
            break

        case _:

            print("Invalid choice")