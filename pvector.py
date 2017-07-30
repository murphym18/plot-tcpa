import numpy as np
import nvector as nv
import sys

lat = sys.argv[1]
lon = sys.argv[2]
alt = sys.argv[3]
wgs84 = nv.FrameE(name='WGS84')
point = wgs84.GeoPoint(latitude=float(lat), longitude=float(lon), z=-float(alt), degrees=True)
t = point.to_ecef_vector().pvector.ravel()
o = ",".join(["%.90f" % n for n in t])
print(o)
