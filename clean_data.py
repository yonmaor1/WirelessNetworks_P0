# Open the file capture.txt and read its lines
with open('capture.txt', 'r') as file:
    lines = file.readlines()

data = []
data_header = "No.     Time           Source                Destination           Protocol Length Info"

curr_line = 0
curr_data_index = -1
for line in lines:
    if data_header in line:
        curr_data_index += 1
        data.append([])
        continue
    
    data[curr_data_index].append(line)

print(data[0])