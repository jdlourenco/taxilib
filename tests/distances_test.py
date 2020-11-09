from taxilib.distances import haversine

def test_haversine():
	## computing distances betweeen same location
	# location 1
	lon1 = 12
	lat1 = 21

	# location 1
	lon2 = 12
	lat2 = 21
	assert haversine(lon1, lat1, lon2, lat2) == 0