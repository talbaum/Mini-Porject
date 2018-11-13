import os

#get the current path
curr_path=os.getcwd()
dst = '"%USERPROFILE%\Start Menu\Programs\Startup"'

os.system('cd ' + curr_path)
os.system('copy test.txt ' + dst)

