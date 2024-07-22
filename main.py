import re
import requests
import schedule
import time

def eco_marketing():
    url = "https://airlinemanager.com/marketing_new.php?type=5&mode=do&c=1"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': 'https://airlinemanager.com/marketing_new.php?type=5&mode=do&c=1',
        'scheme': 'https',
        'Cookie': 'device=app; deviceType=android; PHPSESSID=i1trnogv2v47aj8ft19fm98sig',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"{response.status_code} : Error Occurred ")

def rep_marketing():
    url = "https://airlinemanager.com/marketing_new.php?type=1&c=4&mode=do&d=1"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': 'https://airlinemanager.com/marketing_new.php?type=1&c=4&mode=do&d=1',
        'scheme': 'https',
        'Cookie': 'device=app; deviceType=android; PHPSESSID=i1trnogv2v47aj8ft19fm98sig',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"{response.status_code} : Error Occurred ")

def depart_all():
    url = "https://airlinemanager.com/route_depart.php?mode=all&ids=x"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': 'https://airlinemanager.com/route_depart.php?mode=all&ids=x',
        'scheme': 'https',
        'Cookie': 'device=app; deviceType=android; PHPSESSID=i1trnogv2v47aj8ft19fm98sig',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"{response.status_code} : Error Occurred ")

def morning_departure():
    print("Morning depature event started...")
    # Your code here to send the morning departure event
    # Economy Marketing Event 
    eco_marketing()
    # airline reputation Marketing Event
    rep_marketing()
    # depart all the planes
    # have to find a way to make the code depart all the flights at once 
    # the problem is that the api call only departs 20 flights at once 
    depart_all()
    depart_all()



def evening_departure():
    print("Evening departure event started...")
    # Your code here to send the evening departure event
    # airline reputation Marketing Event
    rep_marketing()
    # depart all the planes
    depart_all()
    depart_all()  

# Schedule the request to run at a specific time every day
schedule_time_1 = "09:00"  # 24-hour format, adjust as needed
schedule_time_2 = "19:00"  # 24-hour format, adjust as needed
schedule.every().day.at(schedule_time_1).do(morning_departure)
schedule.every().day.at(schedule_time_2).do(evening_departure)

print(f"Scheduled request at {schedule_time_1} and {schedule_time_2} every day.")

print("Server is running....")

while True:
    schedule.run_pending()
    time.sleep(1)