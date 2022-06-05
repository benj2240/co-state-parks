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
	Longitude DECIMAL NOT NULL,
	WikiLink NVARCHAR(150)
);
"""

# This data is scraped from Wikipedia; see scraper.js to see exactly how
populateParksTable = """
INSERT INTO Parks (ParkName, Latitude, Longitude, WikiLink)
	VALUES
		 ('Arkansas Headwaters Recreation Area', 38.538, 105.993, 'https://en.wikipedia.org/wiki/Arkansas_Headwaters_Recreation_Area')
		,('Barr Lake State Park', 39.938, 104.751, 'https://en.wikipedia.org/wiki/Barr_Lake_State_Park')
		,('Boyd Lake State Park', 40.435, 105.04, 'https://en.wikipedia.org/wiki/Boyd_Lake_State_Park')
		,('Castlewood Canyon State Park', 39.33, 104.739, 'https://en.wikipedia.org/wiki/Castlewood_Canyon_State_Park')
		,('Chatfield State Park', 39.537, 105.069, 'https://en.wikipedia.org/wiki/Chatfield_State_Park')
		,('Cherry Creek State Park', 39.631, 104.846, 'https://en.wikipedia.org/wiki/Cherry_Creek_State_Park')
		,('Cheyenne Mountain State Park', 38.734, 104.828, 'https://en.wikipedia.org/wiki/Cheyenne_Mountain_State_Park')
		,('Crawford State Park', 38.687, 107.596, 'https://en.wikipedia.org/wiki/Crawford_State_Park_(Colorado)')
		,('Eldorado Canyon State Park', 39.931, 105.292, 'https://en.wikipedia.org/wiki/Eldorado_Canyon_State_Park')
		,('Eleven Mile State Park', 38.936, 105.501, 'https://en.wikipedia.org/wiki/Eleven_Mile_State_Park')
		,('Elkhead Reservoir State Park', 40.561, 107.382, 'https://en.wikipedia.org/wiki/Elkhead_Reservoir_State_Park')
		,('Fishers Peak State Park', 37.098, 104.463, 'https://en.wikipedia.org/wiki/Fishers_Peak_State_Park')
		,('Golden Gate Canyon State Park', 39.831, 105.411, 'https://en.wikipedia.org/wiki/Golden_Gate_Canyon_State_Park')
		,('Harvey Gap State Park', 39.614, 107.656, 'https://en.wikipedia.org/wiki/Harvey_Gap_State_Park')
		,('Highline Lake State Park', 39.27, 108.837, 'https://en.wikipedia.org/wiki/Highline_Lake_State_Park')
		,('Jackson Lake State Park', 40.383, 104.092, 'https://en.wikipedia.org/wiki/Jackson_Lake_State_Park_(Colorado)')
		,('James M. Robb - Colorado River State Park', 39.058, 108.461, 'https://en.wikipedia.org/wiki/James_M._Robb_-_Colorado_River_State_Park')
		,('John Martin Reservoir State Park', 38.075, 102.931, 'https://en.wikipedia.org/wiki/John_Martin_Reservoir_State_Park')
		,('Lake Pueblo State Park', 38.255, 104.732, 'https://en.wikipedia.org/wiki/Lake_Pueblo_State_Park')
		,('Lathrop State Park', 37.603, 104.833, 'https://en.wikipedia.org/wiki/Lathrop_State_Park')
		,('Lone Mesa State Park', 37.75, 108.45, 'https://en.wikipedia.org/wiki/Lone_Mesa_State_Park')
		,('Lory State Park', 40.59, 105.184, 'https://en.wikipedia.org/wiki/Lory_State_Park')
		,('Mancos State Park', 37.4, 108.27, 'https://en.wikipedia.org/wiki/Mancos_State_Park')
		,('Mueller State Park', 38.88, 105.181, 'https://en.wikipedia.org/wiki/Mueller_State_Park')
		,('Navajo State Park', 37.009, 107.409, 'https://en.wikipedia.org/wiki/Navajo_State_Park')
		,('North Sterling State Park', 40.789, 103.265, 'https://en.wikipedia.org/wiki/North_Sterling_State_Park')
		,('Paonia State Park', 38.983, 107.346, 'https://en.wikipedia.org/wiki/Paonia_State_Park')
		,('Pearl Lake State Park', 40.787, 106.891, 'https://en.wikipedia.org/wiki/Pearl_Lake_State_Park')
		,('Ridgway State Park', 38.213, 107.734, 'https://en.wikipedia.org/wiki/Ridgway_State_Park')
		,('Rifle Falls State Park', 39.674, 107.7, 'https://en.wikipedia.org/wiki/Rifle_Falls_State_Park')
		,('Rifle Gap State Park', 39.635, 107.755, 'https://en.wikipedia.org/wiki/Rifle_Gap_State_Park')
		,('Roxborough State Park', 39.43, 105.069, 'https://en.wikipedia.org/wiki/Roxborough_State_Park')
		,('Spinney Mountain State Park', 39.002, 105.631, 'https://en.wikipedia.org/wiki/Spinney_Mountain_State_Park')
		,('St. Vrain State Park', 40.168, 104.984, 'https://en.wikipedia.org/wiki/St._Vrain_State_Park')
		,('Stagecoach State Park', 40.288, 106.862, 'https://en.wikipedia.org/wiki/Stagecoach_State_Park')
		,('State Forest State Park', 40.511, 106.01, 'https://en.wikipedia.org/wiki/State_Forest_State_Park')
		,('Staunton State Park', 39.517, 105.4, 'https://en.wikipedia.org/wiki/Staunton_State_Park')
		,('Steamboat Lake State Park', 40.809, 106.953, 'https://en.wikipedia.org/wiki/Steamboat_Lake_State_Park')
		,('Sweetwater Lake State Park', 39.799, 107.165, 'https://en.wikipedia.org/wiki/Sweetwater_Lake_State_Park')
		,('Sweitzer Lake State Park', 38.712, 108.041, 'https://en.wikipedia.org/wiki/Sweitzer_Lake_State_Park')
		,('Sylvan Lake State Park', 39.544, 106.755, 'https://en.wikipedia.org/wiki/Sylvan_Lake_State_Park')
		,('Trinidad Lake State Park', 37.146, 104.57, 'https://en.wikipedia.org/wiki/Trinidad_Lake_State_Park')
		,('Vega State Park', 39.224, 107.793, 'https://en.wikipedia.org/wiki/Vega_State_Park')
		,('Yampa River State Park', 40.491, 107.313, 'https://en.wikipedia.org/wiki/Yampa_River_State_Park');
"""

connection = sqlite3.connect('parks.db')

cursor = connection.cursor()
cursor.execute(dropParksTable)
cursor.execute(createParksTable)
cursor.execute(populateParksTable)

connection.commit()
connection.close()
