import requests
import numpy as np
from bs4 import BeautifulSoup
import json

# https://www.powerball.com/api/v1/numbers/powerball/recent?_format=json
mynums = [12, 38, 48, 52, 63]
myredball = 10
# get
recent = json.loads(requests.get(
    "https://www.powerball.com/api/v1/numbers/powerball/recent?_format=json").content)
winningnums = np.fromstring(
    recent[0]["field_winning_numbers"], dtype=int, sep=",", count=5)
powerball = np.asarray(
    recent[0]["field_winning_numbers"].split(',')[-1], dtype=int)
date = recent[0]["field_draw_date"]
# check
matchingnum = sum(1 for i in (np.in1d(mynums, winningnums)) if i == True)
matchingred = myredball == powerball
body = """
Date %s
Winning 5 numbers:
%s
Powerball : %i
My 5 numbers: 
%s
My Powerball: %i
# of Matching numbers: %i
Powerball Match: %s
""" % (date, winningnums, powerball, mynums, myredball, matchingnum, matchingred)

print(body)
