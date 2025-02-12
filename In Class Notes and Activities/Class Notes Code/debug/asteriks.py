# Print one to ten "*", then 10 to one, 
# then 10 to one but with spaces, then 1 to ten but with 

star_num = 0
for i in range(10):
    star_num += 1
    print("*"*star_num)
print("")
for i in range(10):
    print("*"*star_num)
    star_num -= 1
print("")
star_num = 10
for i in range(10):
    print(" "*(10-star_num) + "*"*star_num)
    star_num-=1
print("")
for i in range(10):
    star_num += 1
    print(" "*(10-star_num) + "*"*star_num)
print("")

print("-------------------------------------------------------------------------------")