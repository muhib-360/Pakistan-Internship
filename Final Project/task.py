import sqlite3

connection = sqlite3.connect('finalproject.db')
cursor = connection.cursor()


class Student:
    def __init__(self, student_id, name, course_enrolled):
        self.student_id = student_id
        self.name = name
        self.course_enrolled = course_enrolled
        self.attendance = 0
        self.academic_progress = {}

# Function to insert student data with default academic progress set to 0
    def insert_student(self):
        name = input("Enter student name: ")
        course = input("Enter course enrolled: ")
        attendance = input("Enter attendance (number): ")

        # Set academic progress to 0 by default
        cursor.execute('''
            INSERT INTO students (name, course_enrolled, attendance, academic_progress) 
            VALUES (?, ?, ?, ?)
        ''', (name, course, attendance, 0))
        connection.commit()
        print(f"Student {name} has been added successfully with an academic progress of 0%.\n")

# Function to fetch and display all students
    def fetch_students(self):
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()

        if students:
            print("\nList of Students:")
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Course: {student[2]}, Attendance: {student[3]}, Academic Progress: {student[4]}%")
        else:
            print("No students found in the database.\n")


   # Function to update student attendance
    def update_student_attendance(self):
        student_id = input("Enter student ID to update attendance: ")
        new_attendance = input("Enter new attendance: ")

        cursor.execute('''
            UPDATE students 
            SET attendance = ? 
            WHERE id = ?
        ''', (new_attendance, student_id))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Student ID {student_id} attendance updated successfully.\n")
        else:
            print(f"No student found with ID {student_id}.\n")


    # Function to update student academic progress
    def update_student_progress(self):
        student_id = input("Enter student ID to update academic progress: ")
        new_progress = input("Enter new academic progress (percentage): ")

        cursor.execute('''
            UPDATE students 
            SET academic_progress = ? 
            WHERE id = ?
        ''', (new_progress, student_id))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Student ID {student_id} academic progress updated successfully.\n")
        else:
            print(f"No student found with ID {student_id}.\n")


    # Function to delete student data
    def delete_student(self):
        student_id = input("Enter student ID to delete: ")

        cursor.execute('''
            DELETE FROM students 
            WHERE id = ?
        ''', (student_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Student ID {student_id} deleted successfully.\n")
        else:
            print(f"No student found with ID {student_id}.\n")

        
class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits
        self.prerequisites = []
        self.students_enrolled = []
        self.faculty = None



    # Function to create a new course
    def create_course(self):
        course_name = input("Enter course name: ")
        credits = input("Enter course credits: ")
        schedule = input("Enter course schedule: ")
        prerequisites = input("Enter course prerequisites (leave empty if none): ")

        cursor.execute('''
            INSERT INTO courses (course_name, credits, schedule, prerequisites, faculty_id, student_list) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (course_name, credits, schedule, prerequisites, None, None))
        connection.commit()
        print(f"Course '{course_name}' has been added successfully.\n")


    # Function to modify an existing course
    def modify_course(self):
        course_id = input("Enter the course ID you want to modify: ")
        new_schedule = input("Enter the new schedule: ")
        new_credits = input("Enter the new credits: ")
        new_prerequisites = input("Enter new prerequisites (leave empty if none): ")

        cursor.execute('''
            UPDATE courses 
            SET schedule = ?, credits = ?, prerequisites = ? 
            WHERE course_id = ?
        ''', (new_schedule, new_credits, new_prerequisites, course_id))
        connection.commit()
        print(f"Course with ID {course_id} has been updated.\n")

# Function to delete a course
    def delete_course():
        course_id = input("Enter the course ID you want to delete: ")

        cursor.execute('DELETE FROM courses WHERE course_id = ?', (course_id,))
        connection.commit()
        print(f"Course with ID {course_id} has been deleted.\n")


# Function to assign faculty to a course
    def assign_faculty_to_course(self):
        course_id = input("Enter the course ID: ")
        faculty_id = input("Enter the faculty ID to assign: ")

        cursor.execute('''
            UPDATE courses 
            SET faculty_id = ? 
            WHERE course_id = ?
        ''', (faculty_id, course_id))
        connection.commit()
        print(f"Faculty with ID {faculty_id} has been assigned to course ID {course_id}.\n")
# Function to enroll a student in a course
    def enroll_student_in_course(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID to enroll: ")

        # Fetch the current student list for the course
        cursor.execute('SELECT student_list FROM courses WHERE course_id = ?', (course_id,))
        result = cursor.fetchone()

        if result[0]:
            student_list = result[0] + "," + student_id  # Append the new student ID
        else:
            student_list = student_id  # Start the list if it's empty

        cursor.execute('''
            UPDATE courses 
            SET student_list = ? 
            WHERE course_id = ?
        ''', (student_list, course_id))
        connection.commit()
        print(f"Student {student_id} has been enrolled in course ID {course_id}.\n")

# Function to remove a student from a course
    def remove_student_from_course(self):
        course_id = input("Enter course ID: ")
        student_id = input("Enter student ID to remove: ")

        # Fetch the current student list for the course
        cursor.execute('SELECT student_list FROM courses WHERE course_id = ?', (course_id,))
        result = cursor.fetchone()
        student_list = result[0].split(",")

        # Remove the student if they exist in the list
        if student_id in student_list:
            student_list.remove(student_id)
            updated_student_list = ",".join(student_list)

            cursor.execute('''
                UPDATE courses 
                SET student_list = ? 
                WHERE course_id = ?
            ''', (updated_student_list, course_id))
            connection.commit()
            print(f"Student {student_id} has been removed from course ID {course_id}.\n")
        else:
            print(f"Student {student_id} is not enrolled in course ID {course_id}.\n")

# Function to view course details
    def view_course_details(self):
        course_id = input("Enter course ID to view details: ")

        cursor.execute('SELECT * FROM courses WHERE course_id = ?', (course_id,))
        result = cursor.fetchone()

        if result:
            print(f"Course Name: {result[1]}")
            print(f"Credits: {result[2]}")
            print(f"Schedule: {result[3]}")
            print(f"Prerequisites: {result[4]}")
            print(f"Assigned Faculty ID: {result[5]}")
            print(f"Enrolled Students: {result[6]}\n")
        else:
            print(f"No course found with ID {course_id}.\n")

class Faculty:
    def __init__(self, faculty_id, name, subjects):
        self.faculty_id = faculty_id
        self.name = name
        self.subjects = subjects
        self.assigned_courses = []
        self.performance_feedback = []




    # Function to add a new faculty member
    def add_faculty(self):
        faculty_name = input("Enter faculty name: ")
        designation = input("Enter faculty designation (e.g., Professor, Assistant Professor): ")
        department = input("Enter faculty department: ")

        cursor.execute('''
            INSERT INTO faculty (faculty_name, designation, department, assigned_courses) 
            VALUES (?, ?, ?, ?)
        ''', (faculty_name, designation, department, None))
        connection.commit()
        print(f"Faculty member '{faculty_name}' has been added successfully.\n")


    # Function to modify an existing faculty member's details
    def modify_faculty(self):
        faculty_id = input("Enter the faculty ID you want to modify: ")
        new_name = input("Enter the new name: ")
        new_designation = input("Enter the new designation: ")
        new_department = input("Enter the new department: ")

        cursor.execute('''
            UPDATE faculty 
            SET faculty_name = ?, designation = ?, department = ? 
            WHERE faculty_id = ?
        ''', (new_name, new_designation, new_department, faculty_id))
        connection.commit()
        print(f"Faculty with ID {faculty_id} has been updated.\n")

# Function to delete a faculty member
    def delete_faculty(self):
        faculty_id = input("Enter the faculty ID you want to delete: ")

        cursor.execute('DELETE FROM faculty WHERE faculty_id = ?', (faculty_id,))
        connection.commit()
        print(f"Faculty member with ID {faculty_id} has been deleted.\n")

    # Function to view faculty details and assigned courses
    def view_faculty_details(self):
        faculty_id = input("Enter faculty ID to view details: ")

        cursor.execute('SELECT * FROM faculty WHERE faculty_id = ?', (faculty_id,))
        result = cursor.fetchone()

        if result:
            print(f"Faculty Name: {result[1]}")
            print(f"Designation: {result[2]}")
            print(f"Department: {result[3]}")
            print(f"Assigned Courses: {result[4]}")
        else:
            print(f"No faculty found with ID {faculty_id}.\n")

class Timetable:
    def __init__(self):
        self.schedule = {}


    # Function to add or update a class timetable
    def add_update_timetable(self):
        course_id = input("Enter course ID: ")
        faculty_id = input("Enter faculty ID: ")
        day_of_week = input("Enter day of the week (e.g., Monday, Tuesday): ")
        start_time = input("Enter class start time (e.g., 09:00 AM): ")
        end_time = input("Enter class end time (e.g., 10:30 AM): ")
        room_number = input("Enter room number: ")

        cursor.execute('''
            INSERT INTO timetable (course_id, faculty_id, day_of_week, start_time, end_time, room_number) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (course_id, faculty_id, day_of_week, start_time, end_time, room_number))
        connection.commit()
        print("Class timetable has been added/updated successfully.\n")


    # Function to check for scheduling conflicts
    def check_scheduling_conflicts(self,faculty_id, day_of_week, start_time, end_time, room_number):
        cursor.execute('''
            SELECT * FROM timetable 
            WHERE faculty_id = ? AND day_of_week = ? 
            AND ((start_time <= ? AND end_time >= ?) OR (start_time <= ? AND end_time >= ?))
            OR (room_number = ? AND day_of_week = ? AND ((start_time <= ? AND end_time >= ?) OR (start_time <= ? AND end_time >= ?)))
        ''', (faculty_id, day_of_week, start_time, end_time, start_time, end_time, room_number, day_of_week, start_time, end_time, start_time, end_time))

        conflict = cursor.fetchone()

        if conflict:
            return True  # Conflict found
        return False  # No conflict
    

    # Function to view class timetable for a course
    def view_course_timetable(self):
        course_id = input("Enter course ID to view timetable: ")

        cursor.execute('''
            SELECT * FROM timetable WHERE course_id = ?
        ''', (course_id,))
        results = cursor.fetchall()

        if results:
            for row in results:
                print(f"Day: {row[3]}, Start: {row[4]}, End: {row[5]}, Room: {row[6]}")
        else:
            print("No timetable found for the specified course.\n")

# Function to view class timetable for a faculty
    def view_faculty_timetable(self):
        faculty_id = input("Enter faculty ID to view timetable: ")

        cursor.execute('''
            SELECT * FROM timetable WHERE faculty_id = ?
        ''', (faculty_id,))
        results = cursor.fetchall()

        if results:
            for row in results:
                print(f"Course ID: {row[1]}, Day: {row[3]}, Start: {row[4]}, End: {row[5]}, Room: {row[6]}")
        else:
            print("No timetable found for the specified faculty.\n")


        # Function to update timetable and notify faculty and students
    def update_timetable_and_notify(self):
        timetable_id = input("Enter the timetable ID to update: ")
        day_of_week = input("Enter new day of the week: ")
        start_time = input("Enter new start time: ")
        end_time = input("Enter new end time: ")
        room_number = input("Enter new room number: ")

        cursor.execute('''
            UPDATE timetable 
            SET day_of_week = ?, start_time = ?, end_time = ?, room_number = ?
            WHERE timetable_id = ?
        ''', (day_of_week, start_time, end_time, room_number, timetable_id))
        connection.commit()

        # Notify (Console print)
        print(f"Timetable with ID {timetable_id} has been updated. Notify affected faculty and students.\n")



class Examination:
    global gpa_scale
    gpa_scale = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

    def __init__(self):
        self.grades = {}

    def insert_exam_result(self,student_id, subject_id, score, grade):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''INSERT INTO exam_results (student_id, subject_id, exam_date, score, grade)
                VALUES (?, ?, DATE('now'), ?, ?)'''
        cursor.execute(query, (student_id, subject_id, score, grade))
        connection.commit()
        connection.close()

    def update_exam_result(self,student_id, subject_id, score, grade):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''UPDATE exam_results SET score = ?, grade = ?, exam_date = DATE('now')
                WHERE student_id = ? AND subject_id = ?'''
        cursor.execute(query, (score, grade, student_id, subject_id))
        connection.commit()
        connection.close()


    def calculate_gpa(self,student_id):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''SELECT grade FROM exam_results WHERE student_id = ?'''
        cursor.execute(query, (student_id,))
        results = cursor.fetchall()
        
        total_points = sum(gpa_scale[grade[0]] for grade in results if grade[0] in gpa_scale)
        gpa = total_points / len(results) if results else 0
        connection.close()
        return gpa



    def record_grade(self, student, course, grade):
        if student not in self.grades:
            self.grades[student] = {}
        self.grades[student][course] = grade

    def calculate_gpa(self, student):
        if student in self.grades:
            total_grades = 0
            courses_count = len(self.grades[student])
            for grade in self.grades[student].values():
                total_grades += self.convert_grade_to_points(grade)
            return total_grades / courses_count
        else:
            return None

    @staticmethod
    def convert_grade_to_points(grade):
        grade_point_mapping = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        return grade_point_mapping.get(grade, 0.0)
    

    def generate_report(self,student_id):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''SELECT subject_id, score, grade, exam_date FROM exam_results WHERE student_id = ?'''
        cursor.execute(query, (student_id,))
        results = cursor.fetchall()
        connection.close()

        report = f"Report for Student ID: {student_id}\n"
        for result in results:
            report += f"Subject: {result[0]}, Score: {result[1]}, Grade: {result[2]}, Date: {result[3]}\n"
        
        return report
    



class Administration:
    def __init__(self):
        self.reports = []


    def generate_enrollment_report(self,course_id):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''SELECT s.student_id, s.name, se.enrollment_date 
                FROM students s
                JOIN student_enrollment se ON s.student_id = se.student_id
                WHERE se.course_id = ?'''
        cursor.execute(query, (course_id,))
        results = cursor.fetchall()
        connection.close()

        report = f"Enrollment Report for Course ID: {course_id}\n"
        for result in results:
            report += f"Student ID: {result[0]}, Name: {result[1]}, Enrollment Date: {result[2]}\n"
        
        return report



    def generate_faculty_assignment_report(self,faculty_id):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''SELECT c.course_id, c.name, fa.semester
                FROM courses c
                JOIN faculty_assignment fa ON c.course_id = fa.course_id
                WHERE fa.faculty_id = ?'''
        cursor.execute(query, (faculty_id,))
        results = cursor.fetchall()
        connection.close()

        report = f"Assignment Report for Faculty ID: {faculty_id}\n"
        for result in results:
            report += f"Course ID: {result[0]}, Course Name: {result[1]}, Semester: {result[2]}\n"
        
        return report
    

    def calculate_graduation_rate(self):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''SELECT COUNT(*) FROM students WHERE graduation_date IS NOT NULL'''
        cursor.execute(query)
        graduated = cursor.fetchone()[0]
        
        query = '''SELECT COUNT(*) FROM students'''
        cursor.execute(query)
        total_students = cursor.fetchone()[0]
        
        connection.close()

        if total_students == 0:
            return 0
        return (graduated / total_students) * 100
    

    def calculate_retention_rate(self):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        
        # Assume retention means students who continue in the next semester
        query = '''SELECT COUNT(DISTINCT student_id) FROM student_enrollment WHERE enrollment_date LIKE '2023%' '''
        cursor.execute(query)
        students_2023 = cursor.fetchone()[0]
        
        query = '''SELECT COUNT(DISTINCT student_id) FROM student_enrollment WHERE enrollment_date LIKE '2024%' '''
        cursor.execute(query)
        students_2024 = cursor.fetchone()[0]
        
        connection.close()

        if students_2023 == 0:
            return 0
        return (students_2024 / students_2023) * 100
    
    def update_financial_record(self,student_id, tuition_fee, scholarship_amount, payment_status):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''UPDATE financial_records 
                SET tuition_fee = ?, scholarship_amount = ?, payment_status = ?
                WHERE student_id = ?'''
        cursor.execute(query, (tuition_fee, scholarship_amount, payment_status, student_id))
        connection.commit()
        connection.close()

class User:
    def __init__(self, username, role):
        username = username
        role = role

    def main_menu(self):
        while True:
            print("==== University Management System ====".center(150))
            print("1. Student Management")
            print("2. Course Management")
            print("3. Faculty Management")
            print("4. Timetable Management")
            print("5. Examination Management")
            print("6. Administrative Reports")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.student_menu()
            elif choice == "2":
                self.course_menu()
            elif choice == "3":
                self.faculty_menu()
            elif choice == "4":
                self.timetable_menu()
            elif choice == "5":
                self.examination_menu()
            elif choice == "6":
                self.administration_menu()
            elif choice == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.\n")

    def student_menu(self):
        student = Student(None, None, None)
        while True:
            print("\n==== Student Management ====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Update Attendance")
            print("4. Update Academic Progress")
            print("5. Delete Student")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                student.insert_student()
            elif choice == "2":
                student.fetch_students()
            elif choice == "3":
                student.update_student_attendance()
            elif choice == "4":
                student.update_student_progress()
            elif choice == "5":
                student.delete_student()
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.\n")

    def course_menu(self):
        course = Course(None, None, None)
        while True:
            print("\n==== Course Management ====")
            print("1. Add Course")
            print("2. Modify Course")
            print("3. Delete Course")
            print("4. Assign Faculty to Course")
            print("5. Enroll Student in Course")
            print("6. Remove Student from Course")
            print("7. View Course Details")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                course.create_course()
            elif choice == "2":
                course.modify_course()
            elif choice == "3":
                course.delete_course()
            elif choice == "4":
                course.assign_faculty_to_course()
            elif choice == "5":
                course.enroll_student_in_course()
            elif choice == "6":
                course.remove_student_from_course()
            elif choice == "7":
                course.view_course_details()
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.\n")

    def faculty_menu(self):
        faculty = Faculty(None, None, None)
        while True:
            print("\n==== Faculty Management ====")
            print("1. Add Faculty")
            print("2. Modify Faculty")
            print("3. Delete Faculty")
            print("4. View Faculty Details")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                faculty.add_faculty()
            elif choice == "2":
                faculty.modify_faculty()
            elif choice == "3":
                faculty.delete_faculty()
            elif choice == "4":
                faculty.view_faculty_details()
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.\n")

    def timetable_menu(self):
        timetable = Timetable()
        while True:
            print("\n==== Timetable Management ====")
            print("1. Add/Update Timetable")
            print("2. View Course Timetable")
            print("3. View Faculty Timetable")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                timetable.add_update_timetable()
            elif choice == "2":
                timetable.view_course_timetable()
            elif choice == "3":
                timetable.view_faculty_timetable()
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.\n")

    def examination_menu(self):
        exam = Examination()
        while True:
            print("\n==== Examination Management ====")
            print("1. Add Exam Result")
            print("2. Update Exam Result")
            print("3. Calculate GPA")
            print("4. Generate Report")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                student_id = input("Enter Student ID: ")
                subject_id = input("Enter Subject ID: ")
                score = input("Enter Score: ")
                grade = input("Enter Grade: ")
                exam.insert_exam_result(student_id, subject_id, score, grade)
            elif choice == "2":
                student_id = input("Enter Student ID: ")
                subject_id = input("Enter Subject ID: ")
                score = input("Enter New Score: ")
                grade = input("Enter New Grade: ")
                exam.update_exam_result(student_id, subject_id, score, grade)
            elif choice == "3":
                student_id = input("Enter Student ID: ")
                gpa = exam.calculate_gpa(student_id)
                print(f"GPA for Student ID {student_id}: {gpa}")
            elif choice == "4":
                student_id = input("Enter Student ID: ")
                report = exam.generate_report(student_id)
                print(report)
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.\n")

    def administration_menu(self):
        admin = Administration()
        while True:
            print("\n==== Administration ====")
            print("1. Generate Enrollment Report")
            print("2. Generate Faculty Assignment Report")
            print("3. Calculate Graduation Rate")
            print("4. Calculate Retention Rate")
            print("0. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == "1":
                course_id = input("Enter Course ID: ")
                report = admin.generate_enrollment_report(course_id)
                print(report)
            elif choice == "2":
                faculty_id = input("Enter Faculty ID: ")
                report = admin.generate_faculty_assignment_report(faculty_id)
                print(report)
            elif choice == "3":
                rate = admin.calculate_graduation_rate()
                print(f"Graduation Rate: {rate}%")
            elif choice == "4":
                rate = admin.calculate_retention_rate()
                print(f"Retention Rate: {rate}%")
            elif choice == "0":
                break
            else:
                print("Invalid choice, please try again.\n")

    def has_access(self, feature):
        role_features = {
            'admin': ['manage_users', 'view_all_reports', 'update_financial_records'],
            'student': ['view_profile', 'track_progress'],
            'faculty': ['view_assigned_courses', 'update_grades'],
        }
        
        if feature in role_features.get(self.role, []):
            return True
        else:
            return False

# Function to manage users (add, remove, view users)
    def manage_users(self):
        while True:
            print("\nManage Users:")
            print("1. Add User")
            print("2. Remove User")
            print("3. View All Users")
            print("4. Go Back")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.remove_user()
            elif choice == '3':
                self.view_users()
            elif choice == '4':
                break
            else:
                print("Invalid option!")

# Add new user to the system
    def add_user(self):
        username = input("Enter username: ")
        role = input("Enter role (admin, student, faculty): ")

        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''INSERT INTO users (username, role) VALUES (?, ?)'''
        cursor.execute(query, (username, role))
        connection.commit()
        connection.close()
        print(f"User {username} added successfully!")

    # Remove user from the system
    def remove_user(self):
        username = input("Enter username to remove: ")

        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''DELETE FROM users WHERE username = ?'''
        cursor.execute(query, (username,))
        connection.commit()
        connection.close()
        print(f"User {username} removed successfully!")

    # View all users in the system
    def view_users(self):
        connection = sqlite3.connect('finalproject.db')
        cursor = connection.cursor()
        query = '''SELECT username, role FROM users'''
        cursor.execute(query)
        users = cursor.fetchall()
        connection.close()

        print("\nList of Users:")
        for user in users:
            print(f"Username: {user[0]}, Role: {user[1]}")


testing = User(None, None)
testing.main_menu()

# user1 = User('Muhib', 'Admin')
# user1.manage_users()
