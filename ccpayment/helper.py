"""
file 주석
luhn 10 알고리즘으로 카드 번호가 유효한지 check한 결과를 return
"""


def card_luhn_checksum_is_valid(card_number):
    """ the card passes a luhn mod-10 checksum """
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for count in range(0, num_digits):
        digit = int(card_number[count])

        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9

        sum = sum + digit

    return ( (sum % 10) == 0 )

