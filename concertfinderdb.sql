DROP TABLE IF EXISTS ticket;
DROP TABLE IF EXISTS review;
DROP TABLE IF EXISTS account;
DROP TABLE IF EXISTS performs_at;
DROP TABLE IF EXISTS organizer;
DROP TABLE IF EXISTS plays_at;
DROP TABLE IF EXISTS produces;
DROP TABLE IF EXISTS event;
DROP TABLE IF EXISTS venue;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS song;
DROP TABLE IF EXISTS artist;

create table artist(
	artist_name VARCHAR(70),
	debut_date DATE,
	artist_bio VARCHAR(150),
	primary key(artist_name)
);

create table song(
	song_name VARCHAR(50),
	genre VARCHAR(30),
	song_length INTEGER,
	song_desc VARCHAR(150),
	release_date DATE,
	primary key(song_name)
);

create table city(
	city_name VARCHAR(50),
	country VARCHAR(50),
	latitude DECIMAL(9, 6),
	longitude DECIMAL(9,6),
	primary key(city_name)
);

create table venue(
	venue_name VARCHAR(70),
	capacity INTEGER NOT NULL,
	street VARCHAR(100) NOT NULL,
	city_name VARCHAR(50) NOT NULL,
	primary key(venue_name),
	foreign key(city_name) references city(city_name)
);

create table event(
	event_name VARCHAR(70),
	date_time DATETIME NOT NULL,
	event_desc VARCHAR(150),
	venue_name VARCHAR(70) NOT NULL,
	primary key(event_name),
	foreign key(venue_name) references venue(venue_name)
);

create table produces(
	artist_name VARCHAR(70),
	song_name VARCHAR(50),
	primary key(artist_name, song_name),
	foreign key(artist_name) references artist(artist_name),
	foreign key(song_name) references song(song_name)
);

create table plays_at( 
	song_name VARCHAR(50),
	event_name VARCHAR(70),
	primary key(song_name, event_name),
	foreign key(song_name) references song(song_name),
	foreign key(event_name) references event(event_name)
);

create table organizer(
	event_name VARCHAR(70),
	org_name VARCHAR(70) NOT NULL,
	primary key(event_name),
	foreign key(event_name) references event(event_name)
);

create table performs_at(
	artist_name VARCHAR(70),
	event_name VARCHAR(70),
	primary key(artist_name, event_name),
	foreign key(artist_name) references artist(artist_name),
	foreign key(event_name) references event(event_name)
);


create table account(
	username VARCHAR(30) NOT NULL,
	acc_birth_date DATE NOT NULL,
	join_date DATE,
	acc_bio VARCHAR(150),
	city_name VARCHAR(50) NOT NULL,
	primary key(username),
	foreign key(city_name) references city(city_name)
);

create table review(
	review_id INTEGER NOT NULL AUTO_INCREMENT,
	score FLOAT NOT NULL,
	review_text VARCHAR(250), 
	review_date DATE NOT NULL,
	event_name VARCHAR(70),
	username VARCHAR(30) NOT NULL,
	primary key(review_id),
	foreign key(event_name) references event(event_name),
	foreign key(username) references account(username)
);

create table ticket(
	purchase_id INTEGER NOT NULL AUTO_INCREMENT,
	price DECIMAL(8, 2),
	purchase_date DATE,
	username VARCHAR(30) NOT NULL,
	event_name VARCHAR(70) NOT NULL,
	primary key(purchase_id),
	foreign key(username) references account(username),
	foreign key(event_name) references event(event_name)
);

-- ARTIST RELATION
-- ARTIST 1
insert into artist(debut_date, artist_name, artist_bio) values ("1973-01-01", "Lynyrd Skynyrd", "Popular rock band from the 1970s");

-- ARTIST 2
insert into artist(debut_date, artist_name, artist_bio) values ("2010-06-15", "Drake", "Popular rapper and certified lover boy");

-- ARTIST 3
insert into artist(debut_date, artist_name, artist_bio) values ("2006-10-24", "Taylor Swift", "World-famous singer and cult leader");

-- ARTIST 4
insert into artist(debut_date, artist_name, artist_bio) values ("2002-04-02", "Marcus", "hi im marcus");

-- ARTIST 5
insert into artist(debut_date, artist_name, artist_bio) values ("2024-05-18", "Ludwig von Beethoven's Reanimated Corpse", "he's coming.");

-- ARTIST 6
insert into artist(debut_date, artist_name, artist_bio) values ("2024-11-06", "Joe Biden", "Elderly gentleman, has leadership experience, makes a killer quiche");

-- SONG RELATION
-- SONG 1
insert into song(song_name, genre, song_length, song_desc, release_date) values ("Free Bird", "Rock", 548, "Hard rock song", "1973-08-13");

-- SONG 2
insert into song(song_name, genre, song_length, song_desc, release_date) values ("Master of Puppets", "Metal", 516, "Thrash metal song", "1986-03-03");

-- SONG 3
insert into song(song_name, genre, song_length, song_desc, release_date) values ("Wildest Dreams", "Pop", 220, "Upbeat pop song", "2014-10-27");

-- SONG 4
insert into song(song_name, genre, song_length, song_desc, release_date) values ("God's Plan", "Rap", 199, "Upbeat rap song", "2018-01-17");

-- SONG 5
insert into song(song_name, genre, song_length, song_desc, release_date) values ("Symphony No. 5", "Classical", 1800, "Certified Beethoven classic", "1808-12-22");

-- SONG 6
insert into song(song_name, genre, song_length, song_desc, release_date) values ("the song", "Rock", 154, "Soft rock song", "2024-04-18");

-- CITY RELATION
-- CITY 1
insert into city(city_name, country, latitude, longitude) values ("Washington, D.C.", "United States of America", 38.9072, -77.0369);

-- CITY 2
insert into city(city_name, country, latitude, longitude) values ("Richmond", "United States of America", 37.5407, -77.4360);

-- CITY 3
insert into city(city_name, country, latitude, longitude) values ("Rio De Janeiro", "Brazil", 22.9068, 43.1729);

-- CITY 4
insert into city(city_name, country, latitude, longitude) values ("Mogadishu", "Somalia", 2.0371, 45.3379);

-- CITY 5
insert into city(city_name, country, latitude, longitude) values ("Hibbert's Gore", "United States of America", 44.3258, -69.4275);

-- CITY 6
insert into city(city_name, country, latitude, longitude) values ("Reefville", "United States of America", -48.8766, -123.3933);

-- CITY 7
insert into city(city_name, country, latitude, longitude) values ("Frederick", "United States of America", 39.4143, 77.4105);

-- VENUE RELATION
-- VENUE 1
insert into venue(venue_name, capacity, street, city_name) values ("The 9:30 Club", 1200, "815 V St NW", "Washington, D.C.");

-- VENUE 2
insert into venue(venue_name, capacity, street, city_name) values ("The Canal Club", 500, "1545 E Cary St", "Richmond");

-- VENUE 3
insert into venue(venue_name, capacity, street, city_name) values ("The Ocean", 100000, "Pacific Ocean", "Reefville");

-- VENUE 4
insert into venue(venue_name, capacity, street, city_name) values ("The White House", 50000, "1600 Pennsylvania Avenue NW", "Washington, D.C.");

-- VENUE 5
insert into venue(venue_name, capacity, street, city_name) values ("Hood College", 2000, "401 Rosemont Ave", "Frederick");

-- VENUE 6
insert into venue(venue_name, capacity, street, city_name) values ("The Bathroom", 11, "10 Outhouse Avenue", "Richmond");

-- EVENT RELATION
-- EVENT 1
insert into event(event_name, date_time, event_desc, venue_name) values ("The Day of Reckoning", "2024-12-22 19:00:00", "Beethoven reanimates at the 9:30 Club", "The 9:30 Club");

-- EVENT 2
insert into event(event_name, date_time, event_desc, venue_name) values ("District of Columbiachella", "2024-4-12 10:00:00", "It’s like Coachella but even worse somehow", "The 9:30 Club");

-- EVENT 3
insert into event(event_name, date_time, event_desc, venue_name) values ("All-American Closed Mic", "2024-11-05 12:00:00", "This replaced the election, no one was voting anyways", "The White House");

-- EVENT 4
insert into event(event_name, date_time, event_desc, venue_name) values ("Eras Tour: Reefville", "2024-06-19 18:00:00", "Taylor Swift in her hometown!", "The Ocean");

-- EVENT 5
insert into event(event_name, date_time, event_desc, venue_name) values ("marcus' event", "2015-07-13 15:00:00", "hi im marcus", "The Canal Club");

-- EVENT 6
insert into event(event_name, date_time, event_desc, venue_name) values ("Hood College Class of 2024 Graduation", "2024-05-18 10:00:00", "Congratulations, graduates!", "Hood College");

-- PRODUCES RELATION
insert into produces(artist_name, song_name) values ("Lynyrd Skynyrd", "Free Bird");
insert into produces(artist_name, song_name) values ("Drake", "Master of Puppets");
insert into produces(artist_name, song_name) values ("Taylor Swift", "Wildest Dreams");
insert into produces(artist_name, song_name) values ("Drake", "God's Plan");
insert into produces(artist_name, song_name) values ("Joe Biden", "God's Plan");
insert into produces(artist_name, song_name) values ("Ludwig von Beethoven's Reanimated Corpse", "Symphony No. 5");
insert into produces(artist_name, song_name) values ("Marcus", "the song");

-- PLAYS_AT RELATION
insert into plays_at(song_name, event_name) values ("God's Plan", "Hood College Class of 2024 Graduation");
insert into plays_at(song_name, event_name) values ("Symphony No. 5", "The Day of Reckoning");
insert into plays_at(song_name, event_name) values ("the song", "marcus' event");
insert into plays_at(song_name, event_name) values ("Wildest Dreams", "Eras Tour: Reefville");
insert into plays_at(song_name, event_name) values ("God's Plan", "All-American Closed Mic");
insert into plays_at(song_name, event_name) values ("Wildest Dreams", "Hood College Class of 2024 Graduation");

-- ORGANIZER RELATION
insert into organizer(event_name, org_name) values ("The Day of Reckoning", "Johnson");
insert into organizer(event_name, org_name) values ("District of Columbiachella", "Sonjohn");
insert into organizer(event_name, org_name) values ("All-American Closed Mic", "Jonsohn");
insert into organizer(event_name, org_name) values ("Eras Tour: Reefville", "Sonnhoj");
insert into organizer(event_name, org_name) values ("marcus' event", "Hoj");
insert into organizer(event_name, org_name) values ("Hood College Class of 2024 Graduation", "Nhosnoj");

-- PERFORMS_AT RELATION
insert into performs_at(artist_name, event_name) values ("Drake", "Hood College Class of 2024 Graduation");
insert into performs_at(artist_name, event_name) values ("Joe Biden", "Hood College Class of 2024 Graduation");
insert into performs_at(artist_name, event_name) values ("Ludwig von Beethoven's Reanimated Corpse", "The Day of Reckoning");
insert into performs_at(artist_name, event_name) values ("Marcus", "marcus' event");
insert into performs_at(artist_name, event_name) values ("Taylor Swift", "Eras Tour: Reefville");
insert into performs_at(artist_name, event_name) values ("Joe Biden", "All-American Closed Mic");
insert into performs_at(artist_name, event_name) values ("Joe Biden", "District of Columbiachella");

-- ACCOUNT RELATION
insert into account(username, acc_birth_date, join_date, acc_bio, city_name) values ("achang04", "2004-08-12", "202-03-15", "hi", "Frederick");
insert into account(username, acc_birth_date, join_date, acc_bio, city_name) values ("bryced", "2004-09-09", "2019-11-12", "hello", "Frederick");
insert into account(username, acc_birth_date, join_date, acc_bio, city_name) values ("theGuy", "1994-03-08", "2009-09-09", "im he", "Richmond");
insert into account(username, acc_birth_date, join_date, acc_bio, city_name) values ("friendlyfella", "1958-11-14", "2008-12-10", "welcome 2 my profile :)", "Hibbert's Gore");
insert into account(username, acc_birth_date, join_date, acc_bio, city_name) values ("CONCERTMAN", "2013-08-10", "2018-08-10", "The worlds most OBJECTIVE concetr reveiwer", "Mogadishu");
insert into account(username, acc_birth_date, join_date, acc_bio, city_name) values ("Student15", "2002-01-02", "2015-07-23", "just a guy", "Washington, D.C.");

-- REVIEW RELATION
insert into review(score, review_date, review_text, event_name, username) values (1, "2024-05-19", "worst show i have EVER been too!", "Hood College Class of 2024 Graduation", "CONCERTMAN");
insert into review(score, review_date, review_text, event_name, username) values (2, "2024-06-12", "this is the SECONC worst show i have vever been two!", "Eras Tour: Reefville", "CONCERTMAN");
insert into review(score, review_date, review_text, event_name, username) values (4, "2022-03-13", NULL, "marcus' event", "bryced");
insert into review(score, review_date, review_text, event_name, username) values (3, "2024-12-05", "ok", "All-American Closed Mic", "CONCERTMAN");
insert into review(score, review_date, review_text, event_name, username) values (4, "2024-05-20", NULL, "Hood College Class of 2024 Graduation", "Student15");
insert into review(score, review_date, review_text, event_name, username) values (5, "2024-07-03", "really nice concert :)", "Eras Tour: Reefville", "friendlyfella");

-- TICKET RELATION
insert into ticket(price, purchase_date, username, event_name) values (10000.00, "2024-04-30", "bryced", "Eras Tour: Reefville");
insert into ticket(price, purchase_date, username, event_name) values (30.00, "2023-07-22", "friendlyfella", "District of Columbiachella");
insert into ticket(price, purchase_date, username, event_name) values (30.00, "2023-03-14", "Student15", "Hood College Class of 2024 Graduation");
insert into ticket(price, purchase_date, username, event_name) values (100.00, "2024-10-05", "Student15", "All-American Closed Mic");
insert into ticket(price, purchase_date, username, event_name) values (35.00, "2024-12-20", "theGuy", "The Day of Reckoning");
insert into ticket(price, purchase_date, username, event_name) values (3.00, "2014-10-28", "achang04", "marcus' event");
