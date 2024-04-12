class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.track_listened = [] 
        
    def find_islistened(self, track_list):
        listened = []
        for track in track_list:
            if True in track:
                listened.append(track)
        return listened
        #return self.track_listened.append(track)
    
    
        # Parameters:
        #   tracklist
        # list by Artist name and song title [[artist, title, false] , [artist, title, true]]
        # returns a list of tracks listened
    
    def add_listened_tracks(self, track_list):
        filtered_list = self.find_islistened(track_list)
        self.track_listened.append(filtered_list)

        # Parameters:
        # Returns:
        #   nothing
        # Side-effects
        # add list of _islistened tracks
        # No code here yet

    def see_listened_tracklist(self):
        return self.track_listened
    
        # Returns:
        #   The current list of tracks
        # Side-effects:
        #   None
        # No code here yet