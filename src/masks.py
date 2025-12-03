from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Функция, которая маскирует номер карты."""
    mask_card = str(card_number)
    masked_number = f"{mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}"

    return masked_number


def get_mask_account(account_number: Union[int, str]) -> str:
    """Функция, которая маскирует номер счета."""
    mask_account = str(account_number)
    masked_account = f"**{mask_account[-4:]}"

    return masked_account
