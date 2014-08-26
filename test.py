#!/usr/bin/python

import sys
from lib import gtfs_realtime_pb2

message = gtfs_realtime_pb2.FeedMessage()

f = open(sys.argv[1],"rb")
message.ParseFromString(f.read())
f.close()

for entity in message.entity:
    print entity.vehicle

