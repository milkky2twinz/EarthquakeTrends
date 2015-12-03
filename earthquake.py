import csv
with open('thailand_earthquake_stat_database.csv', 'r') as database:
    data = csv.reader(database)
    #Get the data from database
    dict_city = {}
    for i in data:
        dict_city[i[0]] = dict_city.get(i[0], [])+[i[1::]]
    print(dict_city)
