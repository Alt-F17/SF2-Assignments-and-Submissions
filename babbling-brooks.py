### SETUP
stream_num = int(input()) # INPUT: number of streams
streams = []
global keep_running
keep_running = True

for _ in range(stream_num):
    streams.append(int(input())) # INPUT: all next inputs for the stream 

### FUNCTIONS
def split(streams):
    pass

def merge(streams):
    pass

def end():
    keep_running = False

### MAIN LOOP
while keep_running:
    current_command = int(input()) # INPUT: current command
    if current_command == 99: split(streams)
    elif current_command == 88: merge(streams)
    elif current_command == 77: end(keep_running)

### EXIT PRINT STATEMENT
'''
print(f"{} {}")
'''