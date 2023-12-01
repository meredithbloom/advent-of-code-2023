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

# print(start)

test_vals = open('test.txt', 'r')

split_test = test_vals.read().split('\n')
print(split_test)
# PART 2
# steps:
# need to check for regular digits
# need to check for string versions of numbers 
# array of digits and string versions, grab first and last in array? or
# create dictionary for each line - key is index, value is string/int

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

num_string_vals = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def find_words(string):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    vals = {}
    for num_word in numbers:
        if (num_word in string):
            ind = string.find(num_word)
            vals[ind] = num_word
            #vals[ind] = num_string_vals[num_word]
    return vals

def find_digits(string):
    vals = {}
    for i in range(len(string)):
        if (string[i].isdigit()):
            vals[i] = int(string[i])
    return vals

part2_sum = 0

for line in split_test:
    print(line)
    combined = {**find_words(line), **find_digits(line)}
    print(combined)
    sorted_keys = sorted(combined.keys())
    #print(sorted_keys)
    #first, last = str(combined[sorted_keys[0]]), str(combined[sorted_keys[-1]])
    #print(first+last)
    #val = int(first+last)
    #part2_sum = part2_sum + val

print(part2_sum)