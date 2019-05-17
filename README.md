# Spotify-Keylogger - Learning University Project
Created a KeyLogger (= a tool that log the victim keyboard typing and use the private data) hide inside a spotify installation.

**Step1-**
Create a malicous Spotify installaion that runs Step2 secretly and then the original Spotify installation.
After runnig this exe, the keylogger will start logging the user's keyboard actions at each os boot,
as long as the user wont delete the windows welcome flie from the startup folder.

**Step2-**
Script that moves the "Windows Welcome" file(Keylogger) to the startup windows folder.

**Step3-**
Creating the keylogger itself. 
We created a file called "Windows Welcome" and changed it's icon to a windows icon.
This file will be moved to the windows startup folder , and activate the keylogger each time the OS is booting, 
so we tried to make this malicious file look inoocent as posisble.
The Keylogger will send an email to the attacker mail address with the victim keyboard typing( i.e bank passowrds, etc..).


