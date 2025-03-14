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
while 1:
    logic_type = input("Would you like to use lists or sets? (L/S): ").lower()
    if logic_type == "l": # I love walrus operators omg
        print("[Using Lists] Input:")
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

        print("\nOutput Using Lists:")
        for villager in range(1, n + 1):
            if songs_known[villager] == total_songs:
                print(villager)
        exit()        

    # Was told to also do it with sets... Here is that:
    elif logic_type == "s":
        print("[Using Sets] Input:")
        n = int(input())
        e = int(input())
        songs_known = {}  # Dict to track songs known by each villager
        total_songs = 0

        for _ in range(e):
            attendees = [int(x) for x in input().split()]
            num_attendees = attendees[0]
            attendees = set(attendees[1:num_attendees+1])
            
            if 1 in attendees:
                total_songs += 1
                for villager in attendees:
                    songs_known[villager] = songs_known.get(villager, 0) + 1
            else:
                max_songs = max((songs_known.get(v, 0) for v in attendees), default=0)
                for villager in attendees:
                    songs_known[villager] = max_songs

        print("\nOutput Using Sets:")

        for villager in range(1, n + 1):
            if songs_known.get(villager, 0) == total_songs:
                print(villager)
                
        exit()

    else:
        print("Invalid input. Please enter 'L' or 'S'")

"""
Edge Cases:
Input:
5 
3 
3 1 2 3
2 1 2
3 1 2 3
Output:
1
2
3
    
Input:
5
3
3 1 2 3
2 2 3
3 1 2 4
Output:
1
2
3
    
Input:
5
4
2 1 2
3 2 3 4
2 3 5
3 4 5 1
Output:
1
4
5
    
Input:
5
3
2 1 2
2 1 3
2 1 4
Output:
1
    
Input:
5
5
1 1
1 1
1 1
1 1
1 1
Output:
1
    
Input:
5
1
5 1 2 3 4 5
Output:
1
2
3
4
5
    
Input:
7
5
3 1 2 3
3 3 4 5
3 1 5 6
3 2 6 7
3 4 5 7
Output:
1
4
5
7
"""