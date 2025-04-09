# Felix Egan -- 2431927

def toCelcius(faren_temp:str) -> float:
    return round((float(faren_temp) - 32)*(5/9), 2)

def belowFreezing(temp_dict):
    month_dict = {0:'January', 1:'February', 2:'March', 3:'April', 4:'May', 5:'June', 6:'July', 7:'August', 8:'September', 9:'October', 10:'November', 11:'December'}
    below_freeze_months = []
    for year, temps in temp_dict.items():
        for month_idx in range(len(temps)):
            temp = temps[month_idx]
            if temp < 0:
                if month_dict[month_idx] not in below_freeze_months:
                    below_freeze_months.append(month_dict[month_idx])
    return below_freeze_months

data = open("data.txt", "r")
data_lines = data.readlines()
lines = data_lines[4:]

temp_dict = {}
for line in lines:
    line = line.split()
    temp_dict[int(line[0])] = list(map(toCelcius, line[1:]))

print(belowFreezing(temp_dict))

data_celcius = open("data_celcius.txt", "w")
for line in data_lines[:4]:
    data_celcius.write(line)

# For meh formatting, run this:


for year, temps in temp_dict.items():
    data_celcius.write(str(year) + "    " + "    ".join(map(str, temps)) + "\n")

# Or for better formatting, uncomment and run this:


# for year, temps in temp_dict.items():
#     formatted_temps = "  ".join(["{:<6}".format(str(temp)) for temp in temps])
#     data_celcius.write(str(year) + "    " + formatted_temps + "\n")
