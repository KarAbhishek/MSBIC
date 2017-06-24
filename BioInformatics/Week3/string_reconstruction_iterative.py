def attach_with_later_cards(my_card, all_cards_except_mine, return_list):
    controller_stack = [[my_card, all_cards_except_mine]]
    while len(controller_stack) != 0:
        [my_card, all_cards_except_mine] = controller_stack.pop()
        if len(all_cards_except_mine) == 0:
            break
        for matcher_idx, matcher_card in enumerate(all_cards_except_mine):
            if my_card[-(len(my_card)-1):] == matcher_card[:(len(my_card)-1)]:
                return_list.append(matcher_card)
                controller_stack.append([matcher_card, all_cards_except_mine[:matcher_idx] + all_cards_except_mine[
                                                                                                   matcher_idx + 1:]])
    return return_list


list_of_strings = ['AAT', 'ATG', 'GTT', 'TAA', 'TGT']
for idx, i in enumerate(list_of_strings):
    return_list = [i]
    attach_with_later_cards(i, list_of_strings[:idx] + list_of_strings[idx + 1:], return_list)
    if len(return_list) == len(list_of_strings):
        print(return_list)
