
-- Task 1
use music_streaming_app;

create table MusicPlaylist(
	id int primary	key,
    song_name varchar(100),
    artist varchar(100),
    genre varchar(100),
    duration int 
);

insert into MusicPlaylist values
(1,"Believer","Imagine Dragons","Pop Rock",204),
(2,"Perfect","Ed Sheeran","Pop",263),
(3,"Counting Stars","OneRepublic","Pop Rock",257),
(4,"Shape of you","Ed Sheeran","Pop",234),
(5,"Faded","Alan Walker","Electronic",212);

Select * from MusicPlaylist;

-- Task 2

