import sqlite3

# This script will (re)create our SQLite database from scratch.

dropParksTable = """
DROP TABLE IF EXISTS Parks;
"""

createParksTable = """
CREATE TABLE Parks (
	ParkId INTEGER PRIMARY KEY AUTOINCREMENT,
	ParkName NVARCHAR(100) UNIQUE NOT NULL,
	Latitude DECIMAL NOT NULL,
	Longitude DECIMAL NOT NULL
);
"""

# This data is scraped from Wikipedia; see scraper.js to see exactly how
populateParksTable = """
INSERT INTO Parks (ParkName, Latitude, Longitude)
	VALUES
		 ('Arkansas Headwaters Recreation Area', 38.538, 105.993)
		,('Barr Lake State Park', 39.938, 104.751)
		,('Boyd Lake State Park', 40.435, 105.04)
		,('Castlewood Canyon State Park', 39.33, 104.739)
		,('Chatfield State Park', 39.537, 105.069)
		,('Cherry Creek State Park', 39.631, 104.846)
		,('Cheyenne Mountain State Park', 38.734, 104.828)
		,('Crawford State Park', 38.687, 107.596)
		,('Eldorado Canyon State Park', 39.931, 105.292)
		,('Eleven Mile State Park', 38.936, 105.501)
		,('Elkhead Reservoir State Park', 40.561, 107.382)
		,('Fishers Peak State Park', 37.098, 104.463)
		,('Golden Gate Canyon State Park', 39.831, 105.411)
		,('Harvey Gap State Park', 39.614, 107.656)
		,('Highline Lake State Park', 39.27, 108.837)
		,('Jackson Lake State Park', 40.383, 104.092)
		,('James M. Robb - Colorado River State Park', 39.058, 108.461)
		,('John Martin Reservoir State Park', 38.075, 102.931)
		,('Lake Pueblo State Park', 38.255, 104.732)
		,('Lathrop State Park', 37.603, 104.833)
		,('Lone Mesa State Park', 37.75, 108.45)
		,('Lory State Park', 40.59, 105.184)
		,('Mancos State Park', 37.4, 108.27)
		,('Mueller State Park', 38.88, 105.181)
		,('Navajo State Park', 37.009, 107.409)
		,('North Sterling State Park', 40.789, 103.265)
		,('Paonia State Park', 38.983, 107.346)
		,('Pearl Lake State Park', 40.787, 106.891)
		,('Ridgway State Park', 38.213, 107.734)
		,('Rifle Falls State Park', 39.674, 107.7)
		,('Rifle Gap State Park', 39.635, 107.755)
		,('Roxborough State Park', 39.43, 105.069)
		,('Spinney Mountain State Park', 39.002, 105.631)
		,('St. Vrain State Park', 40.168, 104.984)
		,('Stagecoach State Park', 40.288, 106.862)
		,('State Forest State Park', 40.511, 106.01)
		,('Staunton State Park', 39.517, 105.4)
		,('Steamboat Lake State Park', 40.809, 106.953)
		,('Sweetwater Lake State Park', 39.799, 107.165)
		,('Sweitzer Lake State Park', 38.712, 108.041)
		,('Sylvan Lake State Park', 39.544, 106.755)
		,('Trinidad Lake State Park', 37.146, 104.57)
		,('Vega State Park', 39.224, 107.793)
		,('Yampa River State Park', 40.491, 107.313);
"""

connection = sqlite3.connect('parks.db')

cursor = connection.cursor()
cursor.execute(dropParksTable)
cursor.execute(createParksTable)
cursor.execute(populateParksTable)

connection.commit()
connection.close()
