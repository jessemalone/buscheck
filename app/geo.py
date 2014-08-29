from math import cos, acos, radians, degrees

## bounding_box on a sphere
#  define a box with edges a given distance away from a point in meters
# @param SphericalCoord point - spherical coordinates to a point
# @param distance in meters for the box edges
def bounding_box(point, distance):

    r = float(point.radius)
    d = float(distance)
    # we'll denote latitude as phi and longitude as lambda
    
    # derived from the haversine formula we have
    #
    # lambda2 = arccos(1 + (cos(d/r)-1/cos^2(phi1)) + lambda1
    # phi2 = phi1 + d/r

    (lat1,long1) = (point.latitude,point.longitude)
    (phi1,lambda1) = (radians(lat1),radians(long1))

    lambda2 = acos(1 + (cos(d/r)-1)/cos(phi1)**2) + lambda1
    phi2 = phi1 + d/r

    print (phi1, lambda1)
    print (phi2, lambda2)

    point2 = EarthCoord(degrees(phi2),degrees(lambda2))

    return BoundingBox(\
        point2.latitude,
        point.latitude - (point2.latitude - point.latitude),
        point2.longitude,
        point.longitude - (point2.longitude - point.longitude))


class BoundingBox:
    
    edge_north = 0.0
    edge_south = 0.0
    edge_east = 0.0
    edge_west = 0.0

    def __init__(self,n,s,e,w):
        self.edge_north = n
        self.edge_south = s
        self.edge_east = e
        self.edge_west = w

class SphericalCoord:

    latitude = 0.0
    longitude = 0.0
    radius = 0

    def __init__(self,lat,long,r):
        self.latitude = lat
        self.longitude = long
        self.radius = r
        return self

class EarthCoord(SphericalCoord):
    
    radius = 6371000

    def __init__(self,lat,long):
        self.latitude = lat
        self.longitude = long
    
