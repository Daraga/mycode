#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard library
# import webbrowser

## define some constants
date = input("Input the date you what to look up in this format YYYY-MM-DD: ")
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=TclK5r91ZoLQftpJDCFh2hbIal1ifR8IXTw6ap5h&date=' + date ## this is our api key

#https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2020-05-27
## pretty print json
def main():
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json
  #  print(nasaread) # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty print in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
#    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))
    print("Link to the APOD:", nasaread.get('hourl',))



    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

main()

