### SETUP
stream_num = int(input()) # INPUT: number of streams
streams = []
keep_running = True

for _ in range(stream_num):
    streams.append(int(input())) # INPUT: all next inputs for the stream 

### FUNCTIONS
def split(streams):
    ssi = int(input())-1 #splitting_stream_index
    lsf = streams[ssi]*int(input())/100 #left_stream_flow
    rsf = streams[ssi]-lsf #right_stream_flow
    streams[ssi] = rsf
    streams.insert(ssi, lsf)
    return streams

def merge(streams):
    msi = int(input())-1 #merge_stream_index
    streams[msi] += streams[msi+1]
    streams.pop(msi+1)
    return streams

### MAIN LOOP
while keep_running:
    current_command = int(input()) # INPUT: current command
    if current_command == 99: streams = split(streams)
    elif current_command == 88: streams = merge(streams)
    elif current_command == 77: keep_running = False

### EXIT PRINT STATEMENT
print(" ".join(str(round(stream)) for stream in streams))