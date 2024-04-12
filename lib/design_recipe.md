# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

# Nouns
- music listening
- tracks - that I've listened to
- list of tracks

# Verbs
- keep- track
- add - tracks I've listened to
- see - list of listened tracks


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    # User-facing properties:
    #   name: string

    def __init__(self):
       self.track_listened = [] 
        
    def find_islistened(self, track_list):
        # Parameters:
        #   tracklist
        # list by Artist name and song title [[artist, title, false] , [artist, title, true]]
        # returns a list of tracks listened

    def add_listened_tracks(self):
        # Parameters:
        # Returns:
        #   nothing
        # Side-effects
        # add list of _islistened tracks
        pass # No code here yet

    def see_listened_tracklist(self):
        # Returns:
        #   The current list of tracks
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Initially, we want to check that when we create an instance
We set an empty list
"""

tracker = MusicTracker()
assert tracker.track_listened == []
# tracker.add_listened_tracks([]) == []
# track_listened = []

# reminder = Reminder("Kay")
# reminder.remind_me_to("Walk the dog")
# reminder.remind() # => "Walk the dog, Kay!"

"""
We want to see a list of only tacks listened
"""
tracker = MusicTracker()
track_list = [[artist, title ,False] , [artist, title, True]]
assert tracker.find_islistened(track_list) == [[artist, title, True]]

"""
Given the tracks filtered form _islistened
We want to add them to the track_listened list
"""
tracker = MusicTracker()
track_list = [[artist, title ,False] , [artist, title, True]]
filtered_list = tracker.find_islistened(track_list)
add_listened_tracks(filtered_list) 
assert tracker.track_listened == [artist, title, True]
# reminder = Reminder("Kay")
# reminder.remind_me_to("")
# reminder.remind() # => ", Kay!"
# ```
"""
Given the track listened
We want to now see the tracklist of tracks we have listened to
"""

tracker = MusicTracker()
islistened_tracklist = track_listened
assert tracker.see_listened_tracklist == tracker.track_listened

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
