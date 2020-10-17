import requests
import notification
import console
# my numbers + mega as last
myNums = [1, 2, 3, 4, 5]
myMegaBall = 0

drawings = eval(requests.get(
    "https://data.ny.gov/resource/5xaw-6ayf.json").content)

lastDrawing = list(map(int, drawings[0].get(
    'winning_numbers').split(' ')))

numMatched = len(set(myNums).intersection(lastDrawing))

matchedMegaball = int(drawings[0].get('mega_ball')) == myMegaBall

body = """
Date: %s
Winning Numbers: %s, %i
My Numbers: %s
# Matched: %i
Matched Powerball: %r
    """ % (drawings[0].get('draw_date').replace('T00:00:00.000', ''), lastDrawing, int(drawings[0].get('mega_ball')), myNums, numMatched, matchedMegaball)

notification.schedule(body)
console.alert(body, button1="ok", hide_cancel_button=True)
