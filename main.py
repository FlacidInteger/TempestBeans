# Tyler Younger
# 02/20/2021


#Create a Python Application which asks the user for their zip code or city.
#Use the zip code or city name in order to obtain weather forecast data from: http://openweathermap.org/
#Display the weather forecast in a readable format to the user.
#Use comments within the application where appropriate in order to document what the program is doing.
#Use functions including a main function.
#Allow the user to run the program multiple times.
#Validate whether the user entered valid data. If valid data isn’t presented notify the user.
#Use the Requests library in order to request data from the webservice.
#Use try blocks when establishing connections to the webservice. You must print a message to the user indicating
# whether or not the connection was successful.

import requests

apikey = "6bbcee9facfa8d01a0d0477b18430baf"

def getLocation():
    # location = input("Enter zipcode or city ")
    # zip = input("Enter zip code:")
    loc = input("Enter city ")


getLocation()

try:
    url = 'http://api.openweathermap.org/data/2.5/weather?' + loc + '001' + "appid=" + apikey
    print(url)

    r = requests.get(zip_url)

except:

    print("Unexpected error:", sys.exc_info()[0])
    raise
