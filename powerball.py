import requests
# my numbers + powerball as last
myNums = [21, 37, 52, 53, 58, 5]

drawings = eval(requests.get(
    "https://www.powerball.com/api/v1/numbers/powerball/recent?_format=json").content)

lastDrawing = list(map(int, drawings[0].get(
    'field_winning_numbers').split(',')))

numMatched = 0
for index, i in enumerate(lastDrawing):
    if(lastDrawing[index] == myNums[index]):
        numMatched += 1

matchedPowerball = lastDrawing[-1] == myNums[-1]

print("""
Date: %s
Winning Numbers: %s
My Numbers: %s
# Matched: %i
Matched Powerball: %r
    """ % (drawings[0].get('field_draw_date'), lastDrawing, myNums, numMatched, matchedPowerball))
