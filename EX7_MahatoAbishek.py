import bs4 as bs
import urllib,csv,os,datetime,urllib.request,re,sys,json



def func1():
    """
    Mahato Abishek
    Metropolia University of Applied Sciences
    Assignment 7: Internet
    22.03.2017
    no snow, no rain and no fog. the temperature ranged between 5-15 degrees
    """
    f = urllib.request.urlopen('http://api.wunderground.com/api/94127df53e899ea4/history_20000531/q/autoip.json')
    tob='11:00pm'
    
    # Automatically geolocate the connecting IP
    ff = urllib.request.urlopen('http://freegeoip.net/json/')
    json_string = ff.read()
    ff.close()
    location = json.loads(json_string)
    
    city =location['city']
    state = location['region_name']
    country = location['country_name']
    zip = location['zip_code']
    
    print("Your nearest Location:")
    print("1. country: %s ,state: %s"%(country,state))
    print("2. city: %s ,zip-code: %s"%(city,zip))
    print()
    json_string = f.read()
    parsed_json = json.loads(json_string)
    
    
    dailySummary=parsed_json['history']['dailysummary'][0]
    fog=dailySummary['fog']
    rain=dailySummary['rain']
    snow=dailySummary['snow']
    
    humidity=dailySummary['humidity']
    maxTemp=dailySummary['maxtempm']
    minTemp=dailySummary['mintempm']
    
    pressure=dailySummary['meanpressurem']
    
    print("my birth of year is 1991, but the data is unavailable. So, 2000AD was selected")
    print("The weather data is available from 1997 in this location!!!")
    print("#Weather data on 31 May 2000 at the location:")
    print("------------------------------")
    print()
    print("1. fog: %s ,rain: %s ,snow: %s"%(fog,rain,snow))
    print("2. humidity: %s ,pressure: %s"%(humidity,pressure))
    
    print("3. max-temperature: %s\u00b0C ,min-temperature: %s\u00b0C "%(maxTemp,minTemp))
    
    
    obs= parsed_json['history']['observations'][38]
    
    
    fog=obs['fog']
    rain=obs['rain']
    snow=obs['snow']
    
    humidity=obs['hum']
    Temp=obs['tempm']
    
    
    pressure=obs['pressurem']
    
    print()
    print("I was born roughly at 11 pm")
    print("#Weather data at that time on 31 May 2000 at the location:")
    print("------------------------------")
    print()
    print("1. fog: %s ,rain: %s ,snow: %s"%(fog,rain,snow))
    print("2. humidity: %s ,pressure: %s"%(humidity,pressure))
    
    print("3. temperature: %s\u00b0C"%(Temp))
    
    f.close()

func1()
