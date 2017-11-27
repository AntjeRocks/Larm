import time
import os
from smtplib import SMTP


def larm(description, value, soft_limit, hard_limit):
    if value < hard_limit:
        print("Everything is fine   :) \n")
    elif value > hard_limit:
        error(description, str(value))
    elif value > soft_limit:
        warn(description, str(value))

def error(description, value):
    log = log_line("Error  ", description, value)
    print(log)
    add_log_entry(log + "\n")
    send_mail(log)

def warn(description, value):
    log = log_line("Warning", description, value)
    print(log)
    add_log_entry(log + "\n")

def log_line(type, description, value):
    return "[" + get_time() + "] " + type + " |" + network_name() + "| " + description + ": " + str(value)

def add_log_entry(log):
    file = open('log.txt', 'a')
    file.write(log)
    file.close()

def send_mail(log):
    smtp = SMTP()
    smtp.connect('localhost', 1025)

    from_addr = "Cooler Admin <cooler@dmin.org>"
    to_addr = "chef <chef@firm.org>"
    subj = "Error"
    msg = "From: " + from_addr + "\nTo: " + to_addr +"\nSubject: " + subj + "\n\n" + log + "\n"

    smtp.sendmail(from_addr, to_addr, msg)
    smtp.quit()

def get_time():
    return time.strftime("%Y-%m-%d %H:%M")

def network_name():
    info = os.uname()
    hostname = info[1]
    return hostname
