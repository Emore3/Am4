import re
import requests
import schedule
import time
from bs4 import BeautifulSoup
from fuel import getCO2price, getfuelprice


def contact():
    global session
    # Create a session object
    session = requests.Session()
    url = "https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn"

    response = session.get(url=url)

    # print(response.text)
    print(f"Cookies : {session.cookies}")


def buyCO2(amount):
    contact()
    url = f"https://airlinemanager.com/co2.php?mode=do&amount={amount}&fbSig=false&_=1721640080690"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': f'airlinemanager.com/co2.php?mode=do&amount={amount}&fbSig=false&_=1721640080690',
        'scheme': 'https',
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"{response.status_code} : Error Occurred ")

def getCO2price():
    contact()
    url = "https://airlinemanager.com/co2.php?undefined&fbSig=false&_=1723184368664"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': 'https://airlinemanager.com/co2.php?undefined&fbSig=false&_=1723184368664',
        'scheme': 'https',
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        prices = soup.find_all("span", class_="text-danger")
        for price in prices:
            co2_price_data = int(price.text[2:].replace(",", ""))
            print(f"Price : {price.text[2:]}")

        tanks = soup.find_all("span", id ="remCapacity")
        for tank in tanks:
            tank_capacity_data = int(tank.text.replace(",", ""))
            print(f"Tank : {tank.text}")

        if (co2_price_data <= 200) and (tank_capacity_data > 0) :
            buyCO2(tank_capacity_data)
    else:
        print(f"{response.status_code} : Error Occurred ")

def buyfuel(amount):
    url = f"https://airlinemanager.com/fuel.php?mode=do&amount={amount}&fbSig=false&_=1721640080690"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': f'airlinemanager.com/fuel.php?mode=do&amount={amount}&fbSig=false&_=1721640080690',
        'scheme': 'https',
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"{response.status_code} : Error Occurred ")
    
def getfuelprice():
    contact()
    url = "https://airlinemanager.com/fuel.php?undefined&fbSig=false&_=17229400"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': 'https://airlinemanager.com/fuel.php?undefined&fbSig=false&_=17229400',
        'scheme': 'https',
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        prices = soup.find_all("span", class_="text-danger")
        for price in prices:
            fuel_price_data = int(price.text[2:].replace(",", ""))
            print(f"Price : {fuel_price_data}")

        tanks = soup.find_all("span", id ="remCapacity")
        for tank in tanks:
            tank_capacity_data = int(tank.text.replace(",", ""))
            print(f"Tank : {tank_capacity_data}")

        if (fuel_price_data <= 500) and (tank_capacity_data > 0) :
            buyfuel(tank_capacity_data)
    else:
        print(f"{response.status_code} : Error Occurred ")



def eco_marketing():
    url = "https://airlinemanager.com/marketing_new.php?type=5&mode=do&c=1"
    
    headers = {
        'authority' : 'airlinemanager.com',
        'method' : 'GET',
        'path': 'https://airlinemanager.com/marketing_new.php?type=5&mode=do&c=1',
        'scheme': 'https',
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

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
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

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
        'Cookie': f'device=app; deviceType=android; PHPSESSID={session.cookies.get("PHPSESSID")}',
        'Priority': 'u=1, i',
        'Referer': 'https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn',
    }

    response = session.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        soup.find_all()
        print("route departed")
        # print("------------------++++++++++-----------")
        # print(response.text)
    else:
        print(f"{response.status_code} : Error Occurred ")

def morning_departure():
    print("Morning depature event started...")
    # Your code here to send the morning departure event
    contact()
    time.sleep(10)
    # Economy Marketing Event 
    eco_marketing()
    time.sleep(10)

    # airline reputation Marketing Event
    rep_marketing()
    time.sleep(10)

    # depart all the planes
    # have to find a way to make the code depart all the flights at once 
    # the problem is that the api call only departs 20 flights at once 
    depart_all()
    time.sleep(10)
    depart_all()
    time.sleep(10)
    depart_all() 
    time.sleep(2)
    getCO2price()
    time.sleep(10)
    depart_all()



def evening_departure():
    print("Evening departure event started...")
    # Your code here to send the evening departure event
    contact()
    time.sleep(10)

    # airline reputation Marketing Event
    rep_marketing()
    time.sleep(10)

    # depart all the planes
    depart_all()
    time.sleep(10)
    depart_all()  
    time.sleep(10)
    depart_all() 
    time.sleep(2)
    getCO2price()
    time.sleep(10)
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
