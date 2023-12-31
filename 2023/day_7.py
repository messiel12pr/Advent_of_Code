from collections import defaultdict

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def insert_hand_sorted(hand, bid, hand_type_list):
    for idx, tpl in enumerate(hand_type_list):
        hand_2 = tpl[0]
        bid_2 = tpl[1]
        for ch in range(len(hand)):
            if cards.index(hand[ch]) < cards.index(hand_2[ch]):
                hand_type_list[idx] = (hand, bid)
                hand = hand_2
                bid = bid_2
                break

            elif cards.index(hand[ch]) > cards.index(hand_2[ch]):
                break

    hand_type_list.append((hand, bid))
    return hand_type_list


'''
    1 -> Five of a kind
    2 -> Four of a kind
    3 -> Full house
    4 -> Three of a kind
    5 -> Two pair
    6 -> One pair
    7 -> High card
'''
def calculate_type(hand_freq):
    max_card_freq = max(hand_freq)

    if max_card_freq == 5:
        return 1

    elif max_card_freq == 4:
        return 2

    elif max_card_freq == 3:
        hand_freq[hand_freq.index(max_card_freq)] -= 3

        if max(hand_freq) == 2:
            return 3

        else:
            return 4

    elif max_card_freq == 2:
        hand_freq[hand_freq.index(max_card_freq)] -= 2

        if max(hand_freq) == 2:
            return 5

        else:
            return 6

    else:
        return 7  

def count_freq_cards(hand):
    freq = [0] * 13

    for ch in hand:
        freq[cards.index(ch)] += 1

    return freq

def part_a():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        hand_type_map = defaultdict(list)
        total_winnings = 0
        ctr = len(input)

        for line in input:
            hand, bid = line.split(' ')
            hand_freq = count_freq_cards(hand)
            hand_type = calculate_type(hand_freq)

            if hand_type in hand_type_map:
                hand_type_map[hand_type] = insert_hand_sorted(hand, bid, hand_type_map[hand_type])

            else:
                hand_type_map[hand_type].append((hand, bid))

        for hand_type in range(0, 8):
            if hand_type not in hand_type_map:
                continue

            for hand, bid in hand_type_map[hand_type]:
                total_winnings += int(bid) * ctr
                ctr -= 1

        print(total_winnings)

part_a()

cards_b = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def insert_hand_sorted_b(hand, bid, hand_type_list):
    for idx, tpl in enumerate(hand_type_list):
        hand_2 = tpl[0]
        bid_2 = tpl[1]
        for ch in range(len(hand)):
            if cards_b.index(hand[ch]) < cards_b.index(hand_2[ch]):
                hand_type_list[idx] = (hand, bid)
                hand = hand_2
                bid = bid_2
                break

            elif cards_b.index(hand[ch]) > cards_b.index(hand_2[ch]):
                break

    hand_type_list.append((hand, bid))
    return hand_type_list 

def find_max_freq_idx(freq):
    max_freq = max(freq)
    for idx, f in enumerate(freq):
        if f == max_freq:
            return idx

def find_min_freq_idx(freq):
    min_freq = min_non_zero = min(filter(lambda x: x != 0, freq))
    for idx, f in enumerate(freq):
        if f == min_freq:
            return idx

def count_freq_cards_b(hand):
    freq = [0] * 13
    
    for ch in hand:
        freq[cards_b.index(ch)] += 1

    max_idx = find_max_freq_idx(freq)
    min_idx = find_min_freq_idx(freq)

    idx_J = cards_b.index('J')
    if freq[idx_J] > 0:
        if freq[max_idx] == freq[idx_J]:
            freq[find_max_freq_idx(freq[:-1])] += freq[idx_J]
            freq[idx_J] = 0

        else:
            freq[max_idx] += freq[idx_J]
            freq[idx_J] = 0

    return freq

def part_b():
    with open('input.txt', 'r') as file:
        input = file.read().splitlines()
        hand_type_map = defaultdict(list)
        total_winnings = 0
        ctr = len(input)

        for line in input:
            hand, bid = line.split(' ')
            hand_freq = count_freq_cards_b(hand)
            hand_type = calculate_type(hand_freq)

            if hand_type in hand_type_map:
                hand_type_map[hand_type] = insert_hand_sorted_b(hand, bid, hand_type_map[hand_type])

            else:
                hand_type_map[hand_type].append((hand, bid))

        for hand_type in range(0, 8):
            if hand_type not in hand_type_map:
                continue

            for hand, bid in hand_type_map[hand_type]:
                total_winnings += int(bid) * ctr
                ctr -= 1

        print(total_winnings)

part_b()