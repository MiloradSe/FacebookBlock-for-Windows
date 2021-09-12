import time
from datetime import datetime as dt

#change "hosts_temp" path with the path of your downloaded "hosts" file which
#is included in my repository - for testing the script
hosts_temp = r"D:\Python course\Website Blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

#if you want this program to actually block Facebook you have to replace all #"hosts_temp" with "hosts_path" from here on out and run the command prompt #as an administrator before running the app

while True:
    #if you wannt to change time when the Facebook is blocked, then change #"8", as from, and "16" ,as to, in the next line as in 24 hour range.
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours..")
        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        time.sleep(5)
    else:
        print("Free time..")
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        time.sleep(5)
