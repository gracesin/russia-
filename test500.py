#This file will use the google distance matrix api to load travel time and distance to a file

import googlemaps
import csv

gmaps = googlemaps.Client(key='---')


input1= open('origin city.csv', 'r') #file that will be read for data---origin/destination
input2= open('destination city.csv', 'r') 
output= open('distance mat.csv', 'w') #file that will have the final data

reader1= csv.reader(input1)
reader2= csv.reader(input2)
writer=csv.writer(output)

for row in list(reader1):
    city_origin=row
    print(city_origin)
   
for row in list(reader2):
    city_destination=row
    print(city_destination)

for i in city_origin:   
    my_distance= gmaps.distance_matrix(i, city_destination, mode="driving", units="metric")
    print(my_distance)
    writer.writerow((city_origin, city_destination, my_distance,))


input1.close()
input2.close()
output.close()
