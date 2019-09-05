from ccpayment.luhn import cardLuhnChecksumIsValid
class Processor():
    cards = {}
    def process(self, commands):
        """ parsing된 commands를 처리한다 """
        for command in commands:
            if command['command'] == "Add":
                if self.cards.get(command['name']) is None:
                    command['validation_result'] = cardLuhnChecksumIsValid(command['card_no'])
                    command['amount'] = 0
                    self.cards[command['name']] = command
            if command['command'] == "Charge":
                # 잔액(amount)을 증가시킨다
                card = self.cards[command['name']]
                if card['validation_result'] == False:
                    print("{} {} {} validation result False".format(
                        command['name'], command['command'], command['amount']))
                    continue

                # 한도액을 넘어서면 결제 거부가 되고 무시됨
                if card['limit'] >= card['amount'] + command['amount']:
                    card['amount'] += command['amount']
                    print("{} {} {} ok".format(
                        card['name'], command['command'], command['amount']))
                else:
                    print("{} {} {} ignored limit:{}".format(
                        card['name'], command['command'], command['amount'], card['limit']))

            if command['command'] == "Credit":
                # 잔액을 감소 시킨다
                card = self.cards[command['name']]
                if card['validation_result'] == False:
                    print("{} {} {} validation result False".format(
                        command['name'], command['command'], command['amount']))
                    continue

                card['amount'] -= command['amount']
                print("{} {} {} ok".format(
                    card['name'], command['amount'], command['command']))

        return self.cards

    def print_result(self, result):
        print("-------------------------")
        for key, value in sorted(result.items()):
            if value['validation_result'] == False:
                print("{}:".format(value['name']), "error")
            else:
                print("{}:".format(value['name']), "${}".format(value['amount']))
