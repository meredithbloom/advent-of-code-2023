all_cards = open('day-4-input.txt', 'r')
test_all_cards = open('test.txt', 'r')

cards = all_cards.read().split('\n')
test_cards = test_all_cards.read().split('\n')

print(test_cards[0])

def parse_card(card_string):
    card_num, only_nums = card_string.split(':')[0].strip(), card_string.split(':')[1].strip()
    winners, have = only_nums.split('|')
    print(winners)
    return winners, have


def compare_nums(winners, ):
    continue

parse_card(test_cards[0])