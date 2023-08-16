-- Data Engineering
drop table if exists used_cars;

CREATE TABLE used_cars (
	price double precision NOT NULL,
	year int NOT NULL,
	manufacturer varchar(30) NOT NULL,
	condition varchar(20) NOT NULL,
	cylinders varchar(20) NOT NULL,
	fuel varchar(20) NOT NULL,
	odometer double precision NOT NULL,
	title_status varchar(200) NOT NULL,
	transmission varchar(200) NOT NULL,
	drive varchar(10) NOT NULL,
	size varchar(100) NOT NULL,
	type varchar(20) NOT NULL,
	paint_color varchar(30) NOT NULL,
	state varchar(2) NOT NULL,
	posting_date date NOT NULL
);

-- permissions issue
COPY used_cars
FROM '/private/tmp/project4Data/vehicles_clean.csv'
DELIMITER ','
CSV HEADER;

-- sanity check
select * from used_cars limit 5;