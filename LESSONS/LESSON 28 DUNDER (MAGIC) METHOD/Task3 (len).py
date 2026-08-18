# Create a Playlist class that stores a list of song names internally (e.g. self.songs).
#  Implement __len__ so that len(my_playlist) returns the number of songs it contains.

class Playlist:
    def __init__(self,songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)
        # return 10

my_playlist = Playlist(["Song A", "Song B", "Song C"])
print(len(my_playlist))


