#!/usr/bin/python

#UPD 27/12/2020

#coded by qwadoh svchost

#Нужные модули
import argparse
import requests, json
import sys
from sys import argv
import os

#Аргументы и парсинг

parser = argparse.ArgumentParser()

parser.add_argument ("-v", help= "Цель/IP", type=str, dest='target', required=True )

args = parser.parse_args()

#Цвета
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#Баннер
print (red+"""
  _____                    _____            __         
 |_   _|                  |_   _|          / _|        
   | |    _ __    ______    | |    _ __   | |_    ___  
   | |   | '_ \  |______|   | |   | '_ \  |  _|  / _ \ 
  _| |_  | |_) |           _| |_  | | | | | |   | (_) |
 |_____| | .__/           |_____| |_| |_| |_|    \___/ 
         | |                                           
         |_|                                           
                                                      v 1.0
"""+red)
print (lgreen+bold+"         with love @qwadoh <3 \n"+clear)
print (yellow+bold+"   search my channel in telegram: @svchost_link <3 \n"+clear)


ip = args.target

api = "https://ipinfo.io/json"

try:
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold+"[$]"
        b = cyan+bold+"[$]"
        print (a, "[Жертва]:", data['ip'])
        print(red+"/////////////////"+red)
        print (b, "[Провайдер]:", data['hostname'])
        print(red+"/////////////////"+red)
        print (a, "[Организация]:", data['org'])
        print(red+"/////////////////"+red)
        print (a, "[Страна]:", data['country'])
        print(red+"/////////////////"+red)
        print (b, "[Город]:", data['city'])
        print(red+"/////////////////"+red)
        print (a, "[Регион]:", data['region'])
        print(red+"/////////////////"+red)
        print (b, "[Локация]:", data['loc'])
        print(red+"/////////////////"+red)
        print (b, "[Часовой пояс]:", data['timezone'])
        print(red+"/////////////////"+red)
        print (a, "[Почтовый индекс]:", data['postal'])
        print (" "+yellow)

except KeyboardInterrupt:
        print ('Был рад познакомиться, до скорых встреч'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+" проверьте интернет соединение!"+clear)
sys.exit(1)