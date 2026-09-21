use music_streaming_app;

-- Task 1
create table Playlist(
	id int primary key,
    song_name varchar(100),
    artist varchar(100),
    duartion int 
);

insert into playlist value(1,"Unstoppable","Sia",217)