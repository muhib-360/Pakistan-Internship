# Task 3 : Student Grade Manager
import time

class Main:
    def __init__(self):
        self.greetings()
        self.course_marks = {}
        self.course_grades = {}


    def show_menu(self):
        while True:
            time.sleep(0.3)
            print("\nCheck the operations below : \n1)Add Grades\n2)Calculate Average\n3)Show Grades\n")

            user_options = int(input("Select from above (1-3) : "))
            if user_options == 1:
                self.take_courses()
                continue
            if user_options == 2:
                self.calculate_avg() 
            if user_options == 3:
                self.show_grades()


    def greetings(self):
        print(" | Welcome to Student Grades Tracker | \n\n".center(150))
        print("Program made by Muhib with 💖\n".center(250))

    def take_courses(self):
        ask_user = int(input("Enter the number of courses you're enrolled in : "))
        while True:
            for i in range(1 , ask_user+1):
                ask_name = input(f"Course {i} Name : ")
                if ask_name == "":
                    print("No entry found !")
                    break                    
                ask_marks = int(input(f"Course {i} Marks : "))

                self.course_marks[ask_name] = ask_marks
            print(self.course_marks)
            break

    def calculate_avg(self):
        sum = 0
        # for course , marks in self.course_marks.items():
        print(f"Courses Enrolled :\n")

        while True:
            if not self.course_marks:
                print("No data found !")
                time.sleep(0.4)
                break

            for course,marks in self.course_marks.items():
                print(f" | {course} | \t ----> {marks}".center(150))

            number_of_courses = len(self.course_marks.keys())

            if number_of_courses <=1:
                print(f"Couldn't find average for {number_of_courses} courses !")
            for course , marks in self.course_marks.items():
                sum = (marks + sum)
            avg_marks = sum/number_of_courses
            print(f"\nAverage Marks : {avg_marks}")
            break

    def show_grades(self):

        print(" | Course Grade Table | " .center(150))

        if not self.course_grades:
            print("No data found ! ")
            time.sleep(0.4)

        for course,marks in self.course_marks.items():
            if marks == 0:
                self.course_grades[course] = "I"
            elif marks in range(1,60):
                self.course_grades[course] = "F"
            elif marks in range(60,67):
                self.course_grades[course] = "C"
            elif marks in range(67,74):
                self.course_grades[course] = "C+"
            elif marks in range(74,81):
                self.course_grades[course] = "B"
            elif marks in range(81,88):
                self.course_grades[course] = "B+"
            elif marks in range(88,101):
                self.course_grades[course] = "A"
            else:
                print("No Grade Found !")
 
        print(self.course_grades)


testing = Main()
testing.show_menu()
