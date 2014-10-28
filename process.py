import math, utm, os
from bson import json_util
from models import Crime, ShotSpotterEvent
from datetime import datetime, timedelta
from bx.intervals.intersection import Intersecter, Interval

JSON_OUT_PATH = 'static/json/matches.json'
BEFORE_TIME_PADDING = timedelta(minutes=30)
AFTER_TIME_PADDING = timedelta(minutes=30)
MINIMUN_PROXIMITY_METERS = 100

matches = []

start = datetime(2011, 1, 1, 0, 0)
end = datetime(2014, 1, 1, 0, 0)
shots = ShotSpotterEvent.m.find({'Date_Time': {'$gte': start, '$lte': end}})

tree = Intersecter()
for crime in Crime.m.find():
	report_time = crime.REPORTDATETIME
	start_ut = int((report_time - BEFORE_TIME_PADDING).strftime('%s'))
	end_ut = int((report_time + AFTER_TIME_PADDING).strftime('%s'))
	tree.add_interval(Interval(start_ut, end_ut, crime))

for shot in shots:
	shot_time_ut = int(shot.Date_Time.strftime('%s'))
	time_matches = tree.find(shot_time_ut, shot_time_ut + 1)
	for match in time_matches:
		crime = match.value
		dlat = shot.utm_lat - crime.utm_lat
		dlon = shot.utm_lon - crime.utm_lon
		dist = math.sqrt(dlat**2 + dlon**2)
		if dist < MINIMUN_PROXIMITY_METERS:
			shot.Date_Time = shot.Date_Time.strftime('%Y/%m/%d %H:%M:%S')
			crime.REPORTDATETIME = crime.REPORTDATETIME.strftime('%Y/%m/%d %H:%M:%S')
			matches.append((shot, crime))

with open(JSON_OUT_PATH, 'w') as f:
	f.write(json_util.dumps(matches))













