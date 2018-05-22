# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 16:19:28 2018

@author: Unalmed
"""

from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.basemap 
from mpl_toolkits.basemap import Basemap
import datetime
import matplotlib.colors


Waves= Dataset('nest03.200401.nc','r')



altura= np.array(Waves.variables['hs'][:])
direccion= np.array(Waves.variables['theta0'][:])
periodo= np.array(Waves.variables['tps'][:])
lat= np.array(Waves.variables['latitude'][:])
lon= np.array(Waves.variables['longitude'][:])
time= np.array(Waves.variables['time'][:]).astype(np.float)

altura[altura==-32768.0]=np.nan



fecha = np.array([datetime.datetime(1970,01,01)+\
datetime.timedelta(seconds = time[i]) for i in range(len(time))])

altmean=np.nanmean(altura[200:], axis=0)

##recorto el borde con datos anómalos


lon2=lon[3:]
datos=altura[:,:,3:]
datos[datos>=2.5]=np.nan


altmeandata=np.nanmean(datos[200:], axis=0)


#testime=np.where(fecha==datetime.datetime(2004, 1, 1, 11, 0))[0][0]

fig = plt.figure(figsize=(10,8))
ax  = fig.add_subplot(111)
# Basemap es el paquete que dibuja las líneas del mapa
m   = Basemap(llcrnrlat=np.min(lat),urcrnrlat=np.max(lat), \
              llcrnrlon=np.min(lon),urcrnrlon=np.max(lon),\
            rsphere=6371200.,resolution='l',area_thresh=10000)
ny  = lat.shape[0]; nx = lon.shape[0]
lons, lats = m.makegrid(nx, ny)
x,y = m(lons, lats)
cs  = m.contourf(x,y,np.flipud(altmean), cmap='YlGnBu',clevs=50, vmin=0, vmax=50)
m.colorbar(location='bottom',pad="10%")

m.drawparallels(np.arange(-90.,90,30.), labels=[1,0,0,0], size=11,linewidth=0.1)
m.drawmeridians(np.arange(0, 360, 30.),labels=[0,1,0,1], size=11, linewidth=0.1)



#m.fillcontinents(color='w')
m.drawcoastlines()
m.drawmapboundary()
#plt.savefig('Mapa.pdf')
plt.show()


#levels=np.linspace(0,2, 20)







#####se grafican los datos recortados


fig = plt.figure(figsize=(10,8))
ax  = fig.add_subplot(111)
# Basemap es el paquete que dibuja las líneas del mapa
m   = Basemap(llcrnrlat=np.min(lat),urcrnrlat=np.max(lat), \
              llcrnrlon=np.min(lon2),urcrnrlon=np.max(lon2),\
            rsphere=6371200.,resolution='l',area_thresh=10000)
ny  = lat.shape[0]; nx = lon2.shape[0]
lons, lats = m.makegrid(nx, ny)
x,y = m(lons, lats)
cs  = m.contourf(x,y,np.flipud(altmeandata), cmap='YlGnBu',clevs=10, vmin=0, vmax=2)
m.colorbar(location='bottom',pad="10%")

m.drawparallels(np.arange(-90.,90,30.), labels=[1,0,0,0], size=11,linewidth=0.1)
m.drawmeridians(np.arange(0, 360, 30.),labels=[0,1,0,1], size=11, linewidth=0.1)



#m.fillcontinents(color='w')
m.drawcoastlines()
m.drawmapboundary()
#plt.savefig('Mapa.pdf')


#levels=np.linspace(0,2, 20)