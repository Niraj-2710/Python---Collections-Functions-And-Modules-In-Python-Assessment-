import json
import logging

logging.basicConfig(filename="student_management.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

students = {}

while True:
    print("\nMain Menu:\n1. Add Student\n2. Remove Student\n3. View All Students\n4. View Specific Student\n5. Add Marks\n6. Exit")
    choice = input("Enter choice: ")

    if choice == '1':  # Add Student
        serial_number = input("Enter Serial Number: ")
        student_id = input("Enter a role Id: ")
        if student_id in students:
            print("Student ID already exists!")
            continue
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        contact = input("Enter Contact Number: ")
        while not contact.isdigit():
            print("Invalid contact number. Please enter again.")
            contact = input("Enter Contact Number: ")
        faculty = input("Enter Faculty Name: ")
        
        subjects = {}
        while True:
            subject = input("Enter Subject Name (or type 'done' to finish): ")
            if subject.lower() == 'done':
                break
            marks = input(f"Enter Marks for {subject}: ")
            fees = input(f"Enter Fees for {subject}: ")
            subjects[subject] = {"marks": marks, "fees": fees}

        students[student_id] = {
            "serial_number": serial_number, 
            "first_name": first_name, 
            "last_name": last_name, 
            "contact": contact, 
            "faculty": faculty, 
            "subjects": subjects
        }
        logging.info(f"Added Student: {student_id} - {first_name} {last_name}, Faculty: {faculty}, Subjects: {subjects}")
        print("Student added successfully!")

    elif choice == '2':  # Remove Student
        student_id = input("Enter Student ID to remove: ")
        if student_id in students:
            confirm = input("Are you sure you want to delete? (y/n): ")
            if confirm.lower() == 'y':
                del students[student_id]
                logging.info(f"Removed Student: {student_id}")
                print("Student removed successfully!")
        else:
            print("Student ID not found!")

    elif choice == '3':  # View All Students
        if not students:
            print("No students available.")
        else:
            for student_id, details in students.items():
                print(f"Serial: {details['serial_number']}, ID: {student_id}, Name: {details['first_name']} {details['last_name']}, Contact: {details['contact']}, Faculty: {details['faculty']}, Subjects: {details['subjects']}")

    elif choice == '4':  # View Specific Student
        student_id = input("Enter Student ID to view: ")
        if student_id in students:
            print(json.dumps(students[student_id], indent=4))
        else:
            print("Student ID not found!")

    elif choice == '5':  # Add Marks
        student_id = input("Enter Student ID to add marks: ")
        if student_id in students:
            subject = input("Enter Subject Name: ")
            marks = input("Enter Marks: ")
            fees = input("Enter Fees: ")
            students[student_id]["subjects"][subject] = {"marks": marks, "fees": fees}
            logging.info(f"Added Marks for {student_id}: {subject} - Marks: {marks}, Fees: {fees}")
            print("Marks added successfully!")
        else:
            print("Student ID not found!")

    elif choice == '6':  # Exit
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Try again.....")