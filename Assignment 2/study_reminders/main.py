#main.py

from students_manager import StudentsManager
from reminder_generator import generate_reminder
from reminder_sender import send_reminder
from logger import log_reminder
from scheduler import schedule_reminders





if __name__ == "__main__":
    manager = StudentsManager()
    students = manager.get_students()

    if not students:
        print("No students found in the system.")

    else:

        for student in students:
            
            reminder = generate_reminder(student['name'], student['course'])
            send_reminder(student['email'], reminder)
            log_reminder(student, reminder)
            print(f"Reminder generated and sent to {student['name']} at {student['email']}")


    """Starting scheduler for daily automation"""
    for student in students:
        print(f"Scheduling daily reminder for {student['name']} at {student['preferred_time']}")

    """Sending reminders at preferred times"""
    schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)