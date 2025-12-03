def mask_account_card(type_account_card: str) -> str:
    string_account_card = type_account_card.split()
    if len(string_account_card[-1]) == 20:
        mask_result = f'Счет **{string_account_card[-1][-4:]}'
    else:
        mask_result = f'{' '.join(string_account_card[:-1])} {string_account_card[-1][:4]} {string_account_card[-1][4:6]}** **** {string_account_card[-1][-4:]}'
    return mask_result

# Примеры входных данных для проверки функции
# print(mask_account_card('Счет 73654108430135874305'))
# print(mask_account_card('Maestro 1596837868705199'))
# print(mask_account_card('Счет 64686473678894779589'))
# print(mask_account_card('MasterCard 7158300734726758'))
# print(mask_account_card('Счет 35383033474447895560'))
# print(mask_account_card('Visa Classic 6831982476737658'))
# print(mask_account_card('Visa Platinum 8990922113665229'))
# print(mask_account_card('Visa Gold 5999414228426353'))
# print(mask_account_card('Счет 73654108430135874305'))