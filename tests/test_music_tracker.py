from lib.music_tracker import *

def test_see_an_empty_list():
    tracker = MusicTracker()
    assert tracker.track_listened == []

"""
We want to see a list of only tacks listened
"""
def test_to_find_list_of_tracks_listened():
    tracker = MusicTracker()
    track_list = [["artist", "title" ,False] , ["artist", "title", True]]
    assert tracker.find_islistened(track_list) == [["artist", "title", True]]
"""
Given the tracks filtered form _islistened
We want to add them to the track_listened list
"""
def test_add_listened_tracks_to_list():
    tracker = MusicTracker()
    track_list = [["artist", "title" ,False] , ["artist", "title", True]]
    #filtered_list = tracker.find_islistened(track_list)
    tracker.add_listened_tracks(track_list) 
    assert tracker.track_listened == [[["artist", "title", True]]]
    
"""
Given the track listened
We want to now see the tracklist of tracks we have listened to
"""
def test_see_all_tracks_listened():
    tracker = MusicTracker()
    assert tracker.see_listened_tracklist() == tracker.track_listened