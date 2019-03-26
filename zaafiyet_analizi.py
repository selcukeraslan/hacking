#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zaafiyet Analizi")

print(""" 
Zaafiyet Analizi Aracina Hosgeldiniz!

Created by Leg0raX
""")


hedefip = raw_input("Hedef IP Giriniz:")
os.system("nikto -h " + hedefip)
