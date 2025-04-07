# Felix Egan -- 2431927

def toCelcius(faren_temp:str) -> float:
    return round((float(faren_temp) - 32)*(5/9), 2)

def avgTempYear(cel_year_data, year):
    try: 
        total = 0
        target_year = cel_year_data[year]
        for temp in target_year:
            total += temp
        return round(total/len(target_year), 2)
    except KeyError:
        print('Invalid Year. Please Enter Valid Year and Try Again.')

def topThreeYears(temp_dict):
    avg_set = set()
    top_three = []
    for year in temp_dict:
        avg_set.add(avgTempYear(temp_dict, year))
    for _ in range(3):
        top_three.append(max(avg_set))
        avg_set.remove(max(avg_set))
    return top_three

def avgTempMonth(temp_dict, month):
    month = month.lower()
    month_dict = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
    month_idx = month_dict[month]
    total = 0
    for year in temp_dict:
        total += temp_dict[year][month_idx-1]
    return round(total/len(temp_dict), 2)

data = open("data.txt", "r")

lines = data.readlines()[4:]

temp_dict = {}
for line in lines:
    line = line.split()
    temp_dict[int(line[0])] = list(map(toCelcius, line[1:]))

print('Temp_Dict:', temp_dict)
print()
print('Avg Year 1964:', avgTempYear(temp_dict, 1964))
print()
print('Top Three Years:', topThreeYears(temp_dict))
print()
print('Avg Temp February:', avgTempMonth(temp_dict, 'FEB'))
print()
print('Error Test:') 
print('Returns:', avgTempYear(temp_dict, 1946))

data.close()