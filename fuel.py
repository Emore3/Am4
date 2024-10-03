import re
import requests
import schedule
import time
from datetime import datetime, timedelta
from bs4 import BeautifulSoup


def contact():
    global session
    # Create a session object
    session = requests.Session()
    url = "https://airlinemanager.com/?gameType=app&device=android&version=11&uid=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&uid_token=8b3d0d4573072d3e07194d8b9ecf2929&android_account=vfeHTHBdgUIueO4rXpB0ANk4YHytTBLmcMwj%2BsYSewY%3D%0A%3AYmFycWtkNTcxMzQyMTUyNQ%3D%3D%0A&mail_token=8b3d0d4573072d3e07194d8b9ecf2929&FCM=eMC2qjqmQTeCVVxyXNrmZf:APA91bFWtIiYTxoPNpnltaMuysPBZopA6bu5reZVxbwnZ-8IffUmL29MLNtmr6kZcHW1xyVZiy8CtKDcgFW4NQtR6q2gnmUqnerjow2xpG5SHX3t-Tdvkb7lnmttI8jGDbdvdE8tfNGn"

    response = session.get(url=url)

    # print(response.text)
    print(f"Cookies : {session.cookies}")

def buyCO2(amount):
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
            print(f"Price : {co2_price_data}")

        tanks = soup.find_all("span", id ="remCapacity")
        for tank in tanks:
            tank_capacity_data = int(tank.text.replace(",", ""))
            print(f"Tank : {tank_capacity_data}")

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


def action():
    contact()
    time.sleep(2)
    getfuelprice()
    time.sleep(5)
    getCO2price()

def schdl():
    action()
    schedule.every(30).minutes.do(action)
    print("Fuel check action has been scheduled...")
    

if __name__ == "__main__":

    current_time = datetime.now()
    minute = datetime.now().strftime("%M")
    minute_int = int(datetime.now().strftime("%M"))
    hour = datetime.now().strftime("%H")
    hour_int = int(datetime.now().strftime("%H"))

    
    if minute_int < 30:
        print("First half of the hour")
        print(f" next check time is {hour}:30")
        schedule_time = f"{hour}:30"
    else:
        print("second half of hour")
        print(f" next check time is {(current_time + timedelta(hours=1)).strftime("%H")}:00")
        schedule_time = f"{(current_time + timedelta(hours=1)).strftime("%H")}:00"

    while True:
        # Get the current time in HH:MM format
        current_time = datetime.now().strftime("%H:%M")
        
        if current_time == schedule_time:
            schdl()
            break  # Exit the loop after the job is done
        
        time.sleep(1)  # Sleep for a second before checking the time again

    while True:
        schedule.run_pending()
        time.sleep(1)