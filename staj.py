# -*- coding: utf-8 -*-
"""
Created on Sun May 22 20:31:08 2022

@author: ebru1
"""

sayilar=[]
sayac=0
while sayac<5:
    sayi=int(input("sayi giriniz:"))
    sayilar.append(sayi)
    sayac=sayac+1
print("girilen sayilar",sayilar)
min=min(sayilar)
max=max(sayilar)
top_min=sum(sayilar)-max
top_max=sum(sayilar)-min
print(top_min)
print(top_max)