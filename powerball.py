import requests
# my numbers + powerball as last
myNums = [1, 2, 3, 4, 5]
myPowerBall = 0

drawings = eval(requests.get(
    "https://www.powerball.com/api/v1/numbers/powerball/recent?_format=json").content)

lastDrawing = list(map(int, drawings[0].get(
    'field_winning_numbers').split(',')))
winningPowerball = lastDrawing.pop(-1)
print((winningPowerball))

numMatched = numMatched = len(set(myNums).intersection(lastDrawing))
matchedPowerball = winningPowerball == myPowerBall

print("""
Date: %s
Winning Numbers: %s, %i
My Numbers: %s
# Matched: %i
Matched Powerball: %r
    """ % (drawings[0].get('field_draw_date'), lastDrawing, winningPowerball, myNums, numMatched, matchedPowerball))
