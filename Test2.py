from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import image
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
m = Basemap(width=5000000,height=4100000,projection='lcc',
            resolution=None,lat_1=90,lat_2=90,lat_0=18.9,lon_0=99)
m.bluemarble()
lat,lon = 18.9,99
x,y = m(lon,lat)

#Show Text on Lat Lon
plt.text(x,y+500000,repr("asd"),fontsize=14,ha='center',va='top',color='b',bbox = dict(boxstyle="square",ec='None',fc=(1,1,1,0.5)))

#Show Point
m.plot(x,y,'ro')

plt.show()
