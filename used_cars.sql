-- Data Engineering
drop table if exists used_cars;

CREATE TABLE used_cars (
	price double precision,
	year int,
	manufacturer varchar(30) NOT NULL,
	condition varchar(20) ,
	cylinders varchar(20) ,
	odometer double precision,
	title_status varchar(200),
	transmission varchar(200),
	size varchar(100),
	state varchar(2),
	posting_date date
);

-- permissions issue
COPY used_cars
FROM '/private/tmp/project4Data/vehicles_clean.csv'
DELIMITER ','
CSV HEADER;

-- sanity check
select * from used_cars limit 5;
