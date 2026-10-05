# Week 1.2, Session 1: Task 6

from pprint import pprint

# Create music database, as a dictionary of strings mapped to lists
# (keys are artist names, values are lists of album names)
music ={
    "artist1":["a1","a2","a3","a4"],
    "artist2":["b1","b2","b3"],
    "artist3":["c1","c2","c3","c4","c5"],
}
# Pretty-print the data structure
pprint(music)
# Display details of one album recorded by a specific artist
print(music.get("artist1"))