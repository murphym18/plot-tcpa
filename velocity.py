import numpy as np
import nvector as nv
import sys

def make_pvec(lat, lon, alt):
    wgs84 = nv.FrameE(name='WGS84')
    tmp = wgs84.GeoPoint(latitude=float(lat), longitude=float(lon), z=-float(alt), degrees=True)
    return tmp.to_ecef_vector().pvector.ravel()

start = make_pvec(sys.argv[1], sys.argv[2], sys.argv[3])
end = make_pvec(sys.argv[4], sys.argv[5], sys.argv[6])
speed = float(sys.argv[7])
delta = np.array(end) - np.array(start)
u = delta * 1/np.sqrt(delta.dot(delta))
v = u * speed
s = ",".join(["%.90f" % c for c in v])
print(s)
5.0213228394939157794851780636236071586608886718750000000000000000000000000000000000000000000000000000