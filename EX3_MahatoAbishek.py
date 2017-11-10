import datetime
import time


name=input("enter your name:")
age=int(input("enter your age:"))


def func1(name,age):
    """
    Mahato Abishek
    Metropolia University of Applied Sciences
    01.02.2017
    """
    favourite_colour=input("enter your favourite color:")
    tup1=(name,age,favourite_colour)
    now=datetime.datetime.now()
    hour=now.hour
    luckynum=(age-now.month)%now.hour
    print("Hi, my name is %s, I'm %d years old, and I like %s.\nToday is %s.\nMy lucky number is %d."%(tup1[0],tup1[1],tup1[2],time.strftime("%d/%m/%Y"),luckynum))


func1(name,age)