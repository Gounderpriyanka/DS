use music_streaming_app;

select * from playlist;
-- Task 1
create table Playlist(
	id int primary key,
    song_name varchar(100),
    artist varchar(100),
    duration int 
);

insert into playlist value(1,"Unstoppable","Sia",217);

-- Task 2
insert into playlist values
(2,"Believer","Imagine Dragons",204),
(3,"Hall of Fame","The Script",203),
(4,"The Climb","Miley Cyrus",216);

-- Task 3
update playlist
set song_name = "Hall"
where  id = 3;

-- Task 4

SET SQL_SAFE_UPDATES = 0;
delete from playlist where duration<120;
SET SQL_SAFE_UPDATES = 1;

-- Task 5 
SET SQL_SAFE_UPDATES = 0;
update playlist
set song_name = concat(song_name,"Remix")
where artist = "The Script" and duration > 120;
SET SQL_SAFE_UPDATES = 1;

