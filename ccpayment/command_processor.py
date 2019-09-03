from ccpayment.luhn import cardLuhnChecksumIsValid
class Processor():
    def process(self, commands):
        for command in commands:
            if command['command'] == "Add":
                cardLuhnChecksumIsValid(command['card_no'])
                print(command)
