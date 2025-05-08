import json

dir_file = open(r'ASSIGNMENTS\EXAM3 - PREP\example.json', 'r')
directory_data = json.load(dir_file)

def analyze_directory(directory):
    total_size = 0
    file_count = {}
    for key, value in directory.items():
        if type(value) is dict:
            sub_size, sub_count = analyze_directory(value)
            total_size += sub_size
            for ext, count in sub_count.items():
                file_count[ext] = file_count.get(ext, 0) + count
        else:
            total_size += value
            ext = key.split('.')[-1]
            file_count[ext] = file_count.get(ext, 0) + 1
    return total_size, file_count

total_size, file_count = analyze_directory(directory_data)

result = {"total_size": total_size, "file_count": file_count}

out_file = open(r'ASSIGNMENTS\EXAM3 - PREP\output.json', 'w')
json.dump(result, out_file)
print(json.dumps(result))