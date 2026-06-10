class Song :
    def __init__ (self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.prev = None
        
class Main_Player :
    def __init__ (self):
        self.head = None
        self.temp = None
        self.current_song = None
    
    def add_song (self, title, artist):
        
        new_song = Song (title, artist)
        new_song.title = title
        new_song.artist = artist
        new_song.next = None
        new_song.prev = None
        
        if ((self.head) == None):
            self.head = new_song
            self.temp = new_song
        else :
            (self.temp).next = new_song
            new_song.prev = self.temp
        self.temp = new_song
        print ("Song added to the playlist")
    
    def show_playlist (self):
        self.temp = self.head
        count = 1
        
        if ((self.head) == None):
            print ("\nPlaylist is empty !")
        else :
            max_title_len = len("Title")
            max_artist_len = len("Artist")
            
            while ((self.temp) != None):
                if len((self.temp).title) > max_title_len:
                    max_title_len = len((self.temp).title)
                if len((self.temp).artist) > max_artist_len:
                    max_artist_len = len((self.temp).artist)
                self.temp = (self.temp).next
            
            title_width = max_title_len + 4
            artist_width = max_artist_len + 4
            format_template = "{:<6}{:<" + str(title_width) + "}{:<" + str(artist_width) + "}"
            print(format_template.format("No.", "Title", "Artist"))
            
            self.temp = self.head
            while ((self.temp) != None):
                print(format_template.format(count, (self.temp).title, (self.temp).artist))
                self.temp = (self.temp).next
                count += 1
    
    def delete_song (self, number):
        self.temp = self.head
        current_count = 1
        
        if ((self.temp) == None):
            print ("\nSong %s not found" %((self.temp).title))
        
        while ((self.temp) != None and number != current_count):
            self.temp = (self.temp).next
            current_count += 1
            
        if (number == current_count):
            if (self.temp == self.head):
                self.head = (self.temp).next
            if ((self.temp).next != None):
                ((self.temp).next).prev = (self.temp).prev
            if ((self.temp).next == None):
                ((self.temp).prev).next = None
            if ((self.temp).prev != None):
                ((self.temp).prev).next = (self.temp).next
            if ((self.temp).prev == None):
                ((self.temp).next).prev = None
            print ("\nSong %s deleted" %((self.temp).title))
        del self.temp
        
        if ((self.head) != None):
            self.temp = self.head
            while ((self.temp).next != None):
                self.temp = (self.temp).next
        else :
            self.temp = None
    
    def play_song (self, number):
        self.temp = self.head
        song_num = 1
        
        if ((self.head) == None):
            print ("\nPlaylist is empty !")
        
        while ((self.temp) != None):
            if (number == song_num):
                print ("\nPlaying song '%s' by - '%s'" %(((self.temp).title), ((self.temp).artist)))
                self.current_song = self.temp
                break
            self.temp = (self.temp).next
            song_num += 1
            if ((self.temp) == None):
                print ("\nSong does not exist in playlist!")
        if ((self.head) != None):
            self.temp = self.head
            while ((self.temp).next != None):
                self.temp = (self.temp).next
    
    def play_all_songs (self):
        self.temp = self.head
        
        if ((self.head) == None):
            print ("\nPlaylist is empty !")
        
        while ((self.temp) != None):
            print ("\nPlaying %s by - %s" %((self.temp.title), (self.temp.artist)))
            self.temp = (self.temp).next
            self.current_song = self.temp
            continue
    
    def play_next_song (self):
        self.temp = self.head
        
        if ((self.head) == None):
            print ("\nPlaylist is empty !")
        
        if ((self.current_song) == None):
            self.current_song = self.head
            print ("\nPlaying song '%s' by - '%s'" %(((self.temp).title), ((self.temp).artist)))
            
        while ((self.current_song) != None):
            if ((self.current_song).next == None):
                print ("\nPlaylist end !")
                break
            self.current_song = (self.current_song).next
            print ("\nPlaying song '%s' by - '%s'" %(((self.current_song).title), ((self.current_song).artist)))
            break
    
    def play_prev_song (self):
        self.temp = self.head
        
        if ((self.head) == None):
            print ("\nPlaylist is empty !")
        
        if ((self.current_song) == None):
            self.current_song = self.head
            print ("\nPlaying song '%s' by - '%s'" %(((self.temp).title), ((self.temp).artist)))
        
        while ((self.current_song) != None):
            if ((self.current_song).prev == None):
                print ("\nThis is the first song of the playlist !")
                break
            self.current_song = (self.current_song).prev
            print ("\nPlaying song '%s' by - '%s'" %(((self.current_song).title), ((self.current_song).artist)))
            break


my_playlist = Main_Player ()
#write your own code here
'''
my_playlist.add_song ("Closer", "Chainsmokers")
my_playlist.add_song ("Me And The Rhythm", "Selena Gomez")
my_playlist.add_song ("Love Yourself", "Justin Bieber")
my_playlist.add_song ("Shape Of You", "Ed Sheran")
my_playlist.add_song ("Steal My Girl", "One Direction")
my_playlist.add_song ("Night Changes", "One Direction")
my_playlist.add_song ("Espresso", "Sabrina Carpenter")
my_playlist.show_playlist ()
'''
