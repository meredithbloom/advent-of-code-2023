all_cards = open('day-4-input.txt', 'r')
test_all_cards = open('test.txt', 'r')

cards = all_cards.read().split('\n')
test_cards = test_all_cards.read().split('\n')

#print(test_cards[0])

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

print(total)