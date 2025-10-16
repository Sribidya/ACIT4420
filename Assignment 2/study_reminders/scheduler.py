#scheduler.py
import schedule
import time
from datetime import datetime

def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger):
    """Schedule reminder delivery for each student at their preferred time."""

    for student in students_manager.get_students():
        reminder = reminder_generator(student['name'], student['course'])

        preferred_time = student['preferred_time'].strip()
        try:
            # Convert AM/PM to 24-hour for schedule
            if preferred_time[-2:].upper() in ("AM", "PM"):
                preferred_time_24 = datetime.strptime(preferred_time, "%I:%M%p").strftime("%H:%M")
            else:
                # Assume 24-hour format, convert to AM/PM and store back
                preferred_time_dt = datetime.strptime(preferred_time, "%H:%M")
                student['preferred_time'] = preferred_time_dt.strftime("%I:%M%p")  # store AM/PM
                preferred_time_24 = preferred_time_dt.strftime("%H:%M")  # 24-hour for schedule
        except ValueError:
            print(f"Invalid time format for {student['name']}: {preferred_time}")
            continue

        schedule.every().day.at(preferred_time_24).do(
            lambda s=student, r=reminder: (
                reminder_sender(s['email'], r),
                logger(s, r)
                )
            )

    while True:
        schedule.run_pending()
        time.sleep(60) # Check every minute