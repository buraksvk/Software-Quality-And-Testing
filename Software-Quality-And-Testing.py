from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
browser = webdriver.Chrome()
def backtohome():
    print("Girmek istediğiniz Yeri seçiniz")
    print("[0] ÇIKIŞ")
    print("[1] SIGN-ON")
    print("[2] REGISTER")
    print("[3] SUPPORT")
    print("[4] CONTACT")
    print("[5] HOME")
    print("[6] FLIGHTS")
    print("[7] HOTELS")
    print("[8] CAR_RENTALS")
    print("[9] CRUISES")
    print("[10] DESTINATIONS")
    print("[11] VACATIONS")
    sayi = int(input())
    while(sayi != 0):
        if(sayi==0):
            browser.close()
        elif(sayi==1):
            signon = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a")
            signon.click()
        elif(sayi==2):
            register = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a")
            register.click()
        elif(sayi==3):
            support = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/a")
            support.click()
        elif(sayi==4):
            contact = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[4]/a")
            contact.click()
        elif(sayi==5):
            home = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/font/a")
            home.click()
        elif(sayi==6):
            flights = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a")
            flights.click()
        elif(sayi==7):
            hotels = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/a")
            hotels.click()
        elif(sayi==8):
            car_rentals = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[4]/td[2]/font/a")
            car_rentals.click()
        elif(sayi==9):
            cruises = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[5]/td[2]/a")
            cruises.click()
        elif(sayi==10):
            destinations = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td[2]/a")
            destinations.click()
        elif(sayi==11):
            vacations = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[7]/td[2]/a")
            vacations.click()
        else:
            print("baska bir sayi girin")
            sayi = int(input())           
        sayi = int(input())
    browser.close()
def SıgnIn():
    browser.get("http://newtours.demoaut.com/mercurysignon.php")
    time.sleep(2)
    username = browser.find_element_by_name("userName")
    username.send_keys("buraksvk")
    password = browser.find_element_by_name("password")
    password.send_keys("1234")
    tikla = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[4]/td/input")
    time.sleep(2)
    tikla.click()
    time.sleep(2)

SıgnIn()

browser.get("http://newtours.demoaut.com/mercuryreservation.php")
type = int(input("1 ile 2 arasında sayı giriniz"))
if(type==1):
    radio1=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[1]")
    radio1.click()
elif(type==2):
    radio1=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[2]/td[2]/b/font/input[2]")
    radio1.click()

passengers=input("1 ile 4 arasında sayı giriniz")
select = Select(browser.find_element_by_name("passCount"))
select.select_by_value(passengers)

departingFrom=input("Departing from giriniz")
select = Select(browser.find_element_by_name("fromPort"))
select.select_by_visible_text(departingFrom)

on=input("1 ile 12 arası")
select = Select(browser.find_element_by_name("fromMonth"))
select.select_by_value(on)

onday=input("1 ile 31 arası")
select = Select(browser.find_element_by_name("fromDay"))
select.select_by_value(onday)

arrivingIn=input("arriving in giriniz")
select = Select(browser.find_element_by_name("toPort"))
select.select_by_visible_text(arrivingIn)

returning=input("1 ile 12 arası")
select = Select(browser.find_element_by_name("toMonth"))
select.select_by_value(returning)

returningDay=input("1 ile 31 arası")
select = Select(browser.find_element_by_name("toDay"))
select.select_by_value(returningDay)

serviceClass = int(input("1 ile 3 arasında sayı giriniz"))
if(serviceClass==1):
    radio2=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/input")
    radio2.click()
elif(serviceClass==2):
    radio2=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[1]")
    radio2.click()
elif(serviceClass==3):
    radio2=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]")
    radio2.click()
Continue=browser.find_element_by_name("findFlights")
Continue.click()

outFlight = int(input("1 ile 4 arasında sayı giriniz"))
if(outFlight==1):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[3]/td[1]/input")
    radio.click()
elif(outFlight==2):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input")
    radio.click()
elif(outFlight==3):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[7]/td[1]/input")
    radio.click()
elif(outFlight==4):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[9]/td[1]/input")
    radio.click()

inFlight = int(input("1 ile 4 arasında sayı giriniz"))
if(inFlight==1):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[3]/td[1]/input")
    radio.click()
elif(inFlight==2):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input")
    radio.click()
elif(inFlight==3):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[7]/td[1]/input")
    radio.click()
elif(inFlight==4):
    radio=browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[9]/td[1]/input")
    radio.click()
Continue=browser.find_element_by_name("reserveFlights")
Continue.click()

for i in range(0,int(passengers),1):
    passFirst="passFirst"+str(i)
    passLast="passLast"+str(i)
    firstName=browser.find_element_by_name(passFirst)
    lastName=browser.find_element_by_name(passLast)

    firstName.send_keys("burak")
    lastName.send_keys("sıvık")

    meal=input("Meal giriniz")
    passMeal="pass."+str(i)+(".meal")
    select = Select(browser.find_element_by_name(passMeal))
    select.select_by_visible_text(meal)

creditCard=input("Credit card giriniz")
select = Select(browser.find_element_by_name("creditCard"))
select.select_by_visible_text(creditCard)

number=browser.find_element_by_name("creditnumber")
number.send_keys("123")


expiration1=input("1 ile 12 arasında sayı giriniz")
if(int(expiration1)<10):
    expiration1=str(0)+expiration1
select = Select(browser.find_element_by_name("cc_exp_dt_mn"))
select.select_by_visible_text(expiration1)

expiration2=input("2000 ile 2010 arasında sayı giriniz")
select = Select(browser.find_element_by_name("cc_exp_dt_yr"))
select.select_by_visible_text(expiration2)

cFirstName=browser.find_element_by_name("cc_frst_name")
cMiddle=browser.find_element_by_name("cc_mid_name")
clast=browser.find_element_by_name("cc_last_name")

cFirstName.send_keys("brk")
cMiddle.send_keys("can")
clast.send_keys("svk")

browser.find_element_by_name("ticketLess").click()
browser.find_element_by_name("billAddress1").send_keys("xxxxxxxxxxx")
browser.find_element_by_name("billAddress2").send_keys("xxxxx")
browser.find_element_by_name("billCity").send_keys("Istanbul")
browser.find_element_by_name("billState").send_keys("Bebek")
browser.find_element_by_name("billZip").send_keys("34000")
select = Select(browser.find_element_by_name("billCountry"))
select.select_by_value('207')
time.sleep(2)

browser.find_element_by_name("ticketLess").click()
browser.find_element_by_name("delAddress1").send_keys("seyit nizam caddesi")
browser.find_element_by_name("delAddress2").send_keys("gir sokak")
browser.find_element_by_name("delCity").send_keys("Istanbul")
browser.find_element_by_name("delState").send_keys("Bakırkoy")
browser.find_element_by_name("delZip").send_keys("34000")
select = Select(browser.find_element_by_name("delCountry"))
select.select_by_value('207')
time.sleep(4)

secure_purchase=browser.find_element_by_name("buyFlights")
secure_purchase.click()
time.sleep(3)

back_to_home = browser.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[7]/td/table/tbody/tr/td[2]/a/img")
back_to_home.click()
backtohome()

