# Bard:

# Every evening villagers in a small village gather around a big fire and sing songs.

# A prominent member of the community is the bard. Every evening if the bard is present, 
# he sings a brand new song that no villager has heard before, and no other song is sung 
# that night. In the event that the bard isnt present, other villagers sing without him 
# and exchange all songs that they know. (NOTE: villagers can only learn new songs from the bard)

# Given the list of villagers present for E consecutive evenings, output all villagers 
# that know all songs sung during that period.

# INPUT:

#     first line is an integer N, number of villagers

#     2nd line is an integer E, number of evenings

#     next E lines contain the list of villagers present on each of the E evenings. 
# Each line begins with a positive integer K, the number of villagers present during 
# that evening followed by K integers seperated by spaces representing the villagers.

#     No villager will appear twice in one night and the bard will appear at least 
# once across all nights. Villager number 1 is the bard

# OUTPUT: 

#     all villagers that know all songs, including the vard, one integer per line in ascending order



n = int(input())
e = int(input())
songs_known = [0] * (n + 1) 
total_songs = 0

for _ in range(e):
    attendees = [int(x) for x in input().split()]
    num_attendees = attendees[0]
    attendees = attendees[1:num_attendees+1]
    
    if 1 in attendees:
        total_songs += 1
        for villager in attendees:
            songs_known[villager] += 1
    else:
        max_songs = max(songs_known[villager] for villager in attendees)
        for villager in attendees:
            songs_known[villager] = max_songs

for villager in range(1, n + 1):
    if songs_known[villager] == total_songs:
        print(villager)