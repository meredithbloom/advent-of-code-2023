all_cards = open('day-4-input.txt', 'r')
test_all_cards = open('test.txt', 'r')

cards = all_cards.read().split('\n')
test_cards = test_all_cards.read().split('\n')

#print(test_cards[0])

# PART 1

def parse_card(card_string):
    card_num, only_nums = card_string.split(':')[0].strip(), card_string.split(':')[1].strip()
    winners, have = only_nums.split('|')
    #print(only_nums)
    return only_nums


def compare_nums(nums):
    left, right = nums.split('|')[0].strip(), nums.split('|')[1].strip()
    left_nums = {int(x) for x in left.split()}
    right_nums = {int(x) for x in right.split()}
    overlap = left_nums.intersection(right_nums)
    if (len(overlap) > 0):
        return(calc_points(overlap))
    else:
        return 0

def calc_points(num_intersection):
    if (len(num_intersection) == 1):
        return 2**0
    elif (len(num_intersection) > 1):
        return 2**(len(num_intersection)-1)
    

total = 0
for c in cards:
    parsed = parse_card(c)
    to_add = compare_nums(parsed)
    total = total + to_add

def overlap_count(nums):
    left, right = nums.split('|')[0].strip(), nums.split('|')[1].strip()
    #print(left, right)
    left_nums = {int(x) for x in left.split()}
    right_nums = {int(x) for x in right.split()}
    overlap = left_nums.intersection(right_nums)
    #print('overlap is: ' + str(overlap))
    return len(overlap)

#print(total)

# PART 2
card_counter = {}
for c in range(len(cards)):
    index = c + 1
    card_counter[index] = 1
# building initial dictionary
#print(card_counter)


for i in range(len(cards)):
    cur_card = parse_card(cards[i])
    #print(cur_card)
    cur_card_num = i + 1
    # should initialize card in dictionary if the card has not been copied before
    if (cur_card_num not in card_counter):
        card_counter[cur_card_num] = 1
    num_copies = overlap_count(cur_card)
    #print(num_copies)
    last_card_to_copy = cur_card_num + num_copies
    #print('start card: '+ str(cur_card_num) + ' plus ' + str(num_copies) + ' = end card: ' + str(last_card_to_copy) )
    for x in range(cur_card_num+1, last_card_to_copy+1):
        #print(x)
        if (x > len(cards)):
            break
        else:
            sets_of_copies = card_counter[cur_card_num]
            card_counter[x] += sets_of_copies
    #print(card_counter)        


print(card_counter)
total_cards = 0
for val in card_counter.values():
    total_cards += val

print(total_cards)