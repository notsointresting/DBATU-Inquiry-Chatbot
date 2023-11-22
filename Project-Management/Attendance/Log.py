#// Print today's date along with day name
import datetime
import calendar

def getDate():

    today = datetime.date.today()
    return calendar.day_name[today.weekday()]



def log_work_and_attendance():

    current_date = datetime.date.today()

    work_done = input("Enter the type of work done: ")
    attendance = input("Enter Your Username: ")

    log_entry = f"{current_date}, {getDate()}: Work Done - {work_done}, Attendance - {attendance}\n"

    log_file_path = "work_log.txt"
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)

    print("Log entry added successfully.")

log_work_and_attendance()


