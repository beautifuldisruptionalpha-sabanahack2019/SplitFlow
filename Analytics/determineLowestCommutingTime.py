import googlemaps
from datetime import datetime
import time

gmaps = googlemaps.Client(key='AIzaSyAK7bhwFBja9fm9I78AJ8pfpfnCP4xf2cM')
arrTime = int(datetime(2019, 8, 5, 7, 0, 0).timestamp())
destination = 'Universidad De Los Andes, Bogota Colombia'

direction = 'Cr 50 # 106-06, Bogota Colombia'


start_time = time.time()
loc = gmaps.geocode(direction)
print(loc)

print(loc)

def timeToWork(direction):
    return googlemaps.distance_matrix.distance_matrix(
        client=gmaps, origins=direction, destinations=destination, departure_time=arrTime)