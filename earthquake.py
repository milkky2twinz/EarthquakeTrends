"""Earthquake Trends"""
import csv
import folium
import webbrowser
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
    test = 0
    for i in detail:
        lat_lon = [float(a) for a in i[1].split(', ')]
        lat, lon = lat_lon
        popup1 = """Location: %s <br> \
Epicenter: %s, %s <br> \
Date: %s <br> \
Time: %s <br> \
Magnitude/Intensity: %s <br> \
Detail: %s""" % (i[0], lat, lon, i[2], i[3], i[4], i[5])
        print('Location:', i[0])
        print('Epicenter: %s, %s' %(lat, lon))
        print('Date:', i[2])
        print('Time:', i[3])
        print('Magnitude/Intensity:', i[4])
        print('Detail:', i[5])
        print('')
        if test == 0:
            #Create map from latitude and longtitude
            map_osm = folium.Map(location=[lat, lon], zoom_start=5)
            test = 1
        #Create marker on map point.
        map_osm.simple_marker(location=[lat, lon], popup=popup1)
        map_osm.circle_marker(location=[lat, lon], radius=10000,\
                              popup=False, line_color='#3186cc',\
                              fill_color='3186cc', fill_opacity=0.2)
    #Create map to file.html
    map_osm.create_map(path='thailandmap.html')
    #Open map to file.html
    webbrowser.open_new_tab('thailandmap.html')
