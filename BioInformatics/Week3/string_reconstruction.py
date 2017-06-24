def attach_with_later_cards(my_card, all_cards_except_mine, return_list):
    if len(all_cards_except_mine) == 0:
        return return_list
    for matcher_idx, matcher_card in enumerate(all_cards_except_mine):
        if my_card[-(len(my_card)-1):] == matcher_card[:(len(my_card)-1)]:
            return_list.append(matcher_card)
            return attach_with_later_cards(matcher_card, all_cards_except_mine[:matcher_idx] + all_cards_except_mine[
                                                                                               matcher_idx + 1:],
                                           return_list)
    return []


list_of_strings = ['AAT',
                   'ATG',
                   'CAT',
                   'CCA',
                   'GAT',
                   'GCC',
                   'GGA',
                   'GGG',
                   'GTT',
                   'TAA',
                   'TGC',
                   'TGG',
                   'TGT']
for idx, i in enumerate(list_of_strings):
    return_list = [i]
    attach_with_later_cards(i, list_of_strings[:idx] + list_of_strings[idx + 1:], return_list)
    if len(return_list) == len(list_of_strings):
        print(return_list)
