# FacebookBlock-for-Windows
Facebook block is a script that runs in the background in Windows OS, blocking facebook from 08:00 to 16:00 on your PC time. Script is currenty set to run on test file because of your potential lack of knowledge of how things work.
If you want it to work as a facebook blocker on your PC, open the website_blocker.pyw file in your editor and read the comments and follow the instructions.

hosts file in this repository is a test file for website_blocker.pyw script.

ATTENTION:
- if you make the changes in the following script by following the comments in it, it will make changes in your hosts file in "C:\Windows\System32\drivers\etc\". To correct that, and exit the app, firstly go to Task Manager, and in processes "end task" on "pythonw.exe"  and after that in "C:\Windows\System32\drivers\etc\hosts" delete the lines if they exist: 
 127.0.0.1 www.facebook.com
 127.0.0.1 facebook.com  
- as those were added if you ran the app between 08:00 to 16:00, and save the file.

- if you like the script after following the comments in it, and actually want to implement it on your PC, i advise you to use it with Scheduled Tasks.
