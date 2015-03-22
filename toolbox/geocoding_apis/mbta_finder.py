"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint
from pygeocoder import Geocoder

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib2.urlopen(url)
    return json.loads(f.read())


def get_lat_long(address):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    lat_long = Geocoder.geocode(address)
    return (lat_long[0].coordinates)


def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    url = MBTA_BASE_URL+'?api_key='+MBTA_DEMO_API_KEY+'&lat='+str(latitude)+'&lon='+str(longitude)+'&format=json'
    return get_json(url)


def find_stop_near(address):
    """
    Given a place name or address, print the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    lat,lon = get_lat_long(address)
    station_dict = get_nearest_station(lat,lon)
    # print station_dict.keys()
    nearest_station = station_dict[u'stop'][0]
    # print nearest_station.keys()
    print ('The nearest MBTA stop\n'+
            'Stop Name:\t'+nearest_station[u'stop_name']+
            '\nDistance:\t'+nearest_station[u'distance'])
    
    return (nearest_station[u'stop_name'],nearest_station[u'distance'])

# pprint (get_json('https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park'))
# print type(get_lat_long('Olin College'))
find_stop_near('Harvard Business School')
