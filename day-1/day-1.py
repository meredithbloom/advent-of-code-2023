calibration_values = open('input-day-1.txt', 'r')

split_vals = calibration_values.read().split('\n')

# PART 1

def find_first(string):
    for i in range(len(string)):
        if (string[i].isdigit()):
            return string[i]

def find_last(string):
    for i in range(len(string)-1,-1,-1):
        if(string[i].isdigit()):
            return string[i]


# print(find_last(split_vals[1]))
start = 0

for subarray in split_vals:
    combined_num = int(str(find_first(subarray))+str(find_last(subarray)))
    start=start+combined_num

print(start)

# PART 2

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']