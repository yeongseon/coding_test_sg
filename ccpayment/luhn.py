"""
file 주석
luhn.py? 무슨뜻? -> 오히려 helper.py가 더 좋을 수도
"""

# 함수명 변경 card_luhn_check_sum... 이런식으로
def cardLuhnChecksumIsValid(card_number):
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

