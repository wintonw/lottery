import requests
import numpy as np
from bs4 import BeautifulSoup
import json
mynums = [12, 38, 48, 52, 63]
myredball = 10
# get data
# https://www.megamillions.com/cmspages/utilservice.asmx/GetLatestDrawData
soup = BeautifulSoup(requests.get("https://www.megamillions.com/cmspages/utilservice.asmx/GetLatestDrawData").content,
                     "html.parser")
recent = json.loads(soup.get_text())
# load
winningnums = []
for i in range(1, 6):
    key = "N%i" % (i)
    winningnums.append(recent["Drawing"][key])
megaball = recent["Drawing"]["MBall"]
date = recent["Drawing"]["PlayDate"].split("T")[0]
# check
matchingnum = sum(1 for i in (np.in1d(mynums, winningnums)) if i == True)
matchingred = myredball == megaball
body = """MegaMillion
Date: %s
Winning 5 numbers:
%s
MegaBall : %i
My 5 numbers: 
%s
My MegaBall: 
%i
# of Matching numbers: 
%i
Powerball Match: 
%s
""" % (date, winningnums, megaball, mynums, myredball, matchingnum, matchingred)

print(body)
