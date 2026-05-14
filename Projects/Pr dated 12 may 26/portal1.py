'''Job Portal with multiple Functionalities'''
login = False

while True:
    print("Welcome to Multifax portal")
    print("---MENU---")
    print("1. LOGIN/REGISTER ")
    print("2. RESUME MAKER ")
    print("3. JOB FINDER ")
    print("4. EXIT")

    choice = int(input("Enter a choice: "))

    match choice:

        case 1:
            print("Login/Register")

            while True:
                ch = input("Enter choice(login/register): ").lower()

                if ch == "login":

                    username = input("Enter username: ")
                    password = input("Enter password: ")

                    if username == "user1" and password == "1234":
                        print("Login Successful")
                        login = True
                        break

                    else:
                        print("Invalid credentials")
                        login = False

                else:

                    name = input("Enter Full Name: ")
                    age = int(input("Enter your age: "))
                    education = input("Enter degree name: ")
                    gender = input("Enter your gender: ")

                    print("Registration Done, logging in automatically")
                    login = True
                    break

        case 2:

            if login == True:

                print("Welcome to Resume Maker")
                print("Provide all details")

                Name = input("Enter Full Name: ")
                profession = input("Enter your profession: ")
                mail = input("Enter mail id: ")
                phone_no = int(input("Enter your Phone no: "))
                Linked_in = input("Enter your Linkedin Id: ")
                Leetcode = input("Enter your Leetcode Id: ")

                exp = input("Do you have experience(Yes/No): ").lower()

                # default values
                exp1 = ""
                com_1 = ""
                working_time1 = ""

                exp2 = ""
                com_2 = ""
                working_time2 = ""

                if exp == "yes":

                    exper = "Experienced"

                    com = int(input("Enter no of companies(max 2): "))

                    match com:

                        case 1:

                            exp1 = input("Enter designation: ")
                            com_1 = input("Enter company name: ")
                            working_time1 = int(input("Enter years: "))

                        case 2:

                            exp1 = input("Enter designation: ")
                            com_1 = input("Enter company name: ")
                            working_time1 = int(input("Enter years: "))

                            exp2 = input("Enter designation: ")
                            com_2 = input("Enter company name: ")
                            working_time2 = int(input("Enter years: "))

                        case _:
                            print("Invalid choice")

                else:
                    exper = "Fresher"

                if exper == "Experienced":

                    print("Enter College education:")

                    course_name = input("Enter Course Name: ")
                    clg_name = input("Enter College Name: ")
                    clg_year = int(input("Enter Passing Year : "))
                    cgpa = float(input("Enter Cgpa: "))

                else:

                    print("Enter College education:")

                    course_name = input("Enter Course Name: ")
                    clg_name = input("Enter College Name: ")
                    clg_year = int(input("Enter Passing Year : "))
                    cgpa = float(input("Enter Cgpa: "))

                    print("Enter School details")

                    stream = input("Enter Stream: ")
                    scl_name = input("Enter school name: ")
                    scl_year = input("Enter passing year: ")
                    percent = float(input("Enter your percentage: "))

                skills = input("Enter skills: ")

                print("Done,Making your resume")

                print("                         RESUME                         ")

                print(f"{Name}\n{profession}\n📱{phone_no}\t\t\t\tlinkedin@{Linked_in}\n📨{mail}\t\t\t\tleetcode@{Leetcode}")

                print("Dedicated, results-driven individual with a strong work ethic and a commitment to excellence.")

                print("Skilled in effective communication, problem-solving, and collaboration.")

                print("🧑‍💼 EXPERIENCE")

                if exper == "Experienced":

                    print(f'{exp1} at {com_1} and worked for {working_time1} years')

                    if com == 2:
                        print(f'{exp2} at {com_2} and worked for {working_time2} years')

                else:
                    print("Fresher")

                print("🎓 EDUCATION")

                print(f'{course_name} from {clg_name} in {clg_year} with cgpa {cgpa}')

                if exper != "Experienced":
                    print(f'{stream} from {scl_name} in {scl_year} with percent = {percent}')

                print("💻 SKILLS")
                print(skills)

                print("\nWith Regards")
                print(Name)

            else:
                print("Please login First")

        case 3:

            if login == True:

                print("Job Search Portal")

                role = input("Enter role for job search: ")
                experien = int(input("Enter experience in years(0 if fresher): "))

                print("2 jobs found")

                if experien >= 1:

                    print(f"{role} at xyz company\nexperience required : 2 years\n")

                    print(f"{role} at Mnt company\nexperience required : 0-2 years")

                    print(f"1.Apply for {role} at xyz company")
                    print(f"2.Apply for {role} at Mnt company")

                    cho = int(input("Enter choice: "))

                    match cho:

                        case 1:

                            p = float(input("Enter experience in years: "))

                            if p >= 2:
                                print("Applied Successfully")

                            else:
                                print("You dont have enough experience")

                        case 2:

                            q = float(input("Enter experience : "))

                            if q >= 0:
                                print("Applied Successfully")

                        case _:
                            print("Invalid choice")

                else:

                    print(f"Internship at xyzz company for {role}, skills required are Good communication, problem solving")

                    print(f"Internship at myzz company for {role}, Skills required Team work and comfortable with night shift")

                    ask = input("want to apply(yes/no): ").lower()

                    if ask == "yes":
                        print("Applied successfully")

                    else:
                        print("Thank you ")

            else:
                print("Please login First")

        case 4:
            print("Thankyou , exiting system")
            break

        case _:
            print("Invalid choice")