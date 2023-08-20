-- Data Engineering
DROP TABLE IF EXISTS used_cars;

CREATE TABLE used_cars (
	price double PRECISION NOT NULL,
	YEAR int NOT NULL,
	manufacturer varchar(30) NOT NULL,
	CONDITION varchar(20) NOT NULL,
	cylinders varchar(20) NOT NULL,
	fuel varchar(20) NOT NULL,
	odometer double PRECISION NOT NULL,
	title_status varchar(200) NOT NULL,
	transmission varchar(200) NOT NULL,
	drive varchar(10) NOT NULL,
	SIZE varchar(100) NOT NULL,
	TYPE varchar(20) NOT NULL,
	paint_color varchar(30) NOT NULL,
	state varchar(2) NOT NULL,
	posting_date date NOT NULL,
	id serial PRIMARY KEY
);
-- permissions issue
COPY used_cars
FROM
'/private/tmp/project4Data/vehicles_clean.csv'
DELIMITER ','
CSV HEADER;

-- sanity check
SELECT * FROM used_cars LIMIT 5;