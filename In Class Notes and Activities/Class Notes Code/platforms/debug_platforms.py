# # # # # # # # # # # 
# HOURS WASTED: 8!h #
# # # # # # # # # # #

def covers(platform, horizontal_pos):
    '''
    :param platform: a platform as defined by the input of the question
    :param horizonal_pos: an integer
    :return : True if platform covers horizontal_post; False otherwise. 
    '''
    return platform[1] < horizontal_pos < platform[2]


def pillar_from(platforms, height, horizontal_pos):
    '''
    :param platforms: a list of platforms (as lists)
    :param height: vertical position
    :param horizontal_pos: horizontal position
    :return : minimum length of pillar from heigh and horizontal_pos to the platform/ground below
    '''
    bottom = 0
    for platform in platforms:
        if (bottom < platform[0] < height and covers(platform, horizontal_pos)):
            bottom = platform[0]
    return height - bottom


n = int(input("Number of Pillars: "))

platforms = []

for i in range(n):
    platform = input("Platform Details (height x1 x2): ").split()
    platforms.append([int(b) for b in platform])

print(platforms)

total = 0

for platform in platforms:    
    total += pillar_from(platforms, platform[0], platform[1])
    total += pillar_from(platforms, platform[0], platform[2])

print(total)