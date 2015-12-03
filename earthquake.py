"""Earthquake Trends"""
import csv
with open('thailand_earthquake_stat_database.csv', 'r') as database:
    data = csv.reader(database)
    #Get the data from database
    dict_city = {}
    for i in data:
        dict_city[i[0]] = dict_city.get(i[0], [])+[i[1::]]
    #print(dict_city)

    #Retrieval of data to use and Test data, Print detail follow input--Location
    city = input()
    detail = dict_city[city]
    for i in detail:
        lat_lon = [float(a) for a in i[1].split(', ')]
        lat, lon = lat_lon
        popup1 = """City: %s <br> \
Latitude: %s, Longitude: %s <br> \
Date: %s <br> \
Time: %s <br> \
M/I: %s <br> \
Detail: %s""" % (i[0], lat, lon, i[1], i[2], i[3], i[4])
        print('Location:', i[0])
        print('Epicenter: %s, %s' %(lat, lon))
        print('Date:', i[1])
        print('Time:', i[2])
        print('Magnitude/Intensity:', i[3])
        print('Detail:', i[4])
        print('')
    #Create map from latitude and longtitude
    map_osm = folium.Map(location=[lat, lon], zoom_start=5)
    map_osm.simple_marker(location=[lat, lon], popup=popup1)
    map_osm.create_map(path='thailandmap.html')