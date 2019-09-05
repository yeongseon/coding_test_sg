from unittest import TestCase
from ccpayment.command_processor import Processor

class TestProcessor(TestCase):

    def test_process(self):
        commands = [{'command': 'Add', 'name': 'Jane', 'card_no': '4111111111111111', 'limit': 1000.0},
         {'command': 'Add', 'name': 'Evan', 'card_no': '5454545454545454', 'limit': 3000.0},
         {'command': 'Add', 'name': 'Daniel', 'card_no': '1234567890123456', 'limit': 2000.0},
         {'command': 'Charge', 'name': 'Jane', 'amount': 500.0}, {'command': 'Charge', 'name': 'Jane', 'amount': 800.0},
         {'command': 'Charge', 'name': 'Evan', 'amount': 7.0}, {'command': 'Credit', 'name': 'Evan', 'amount': 100.0},
         {'command': 'Credit', 'name': 'Daniel', 'amount': 200.0}]

        processor = Processor()
        result = processor.process(commands)
        print(result)
        self.assertEqual(result['Jane']['amount'], 500.0)
        self.assertEqual(result['Evan']['amount'], -93.0)
        self.assertEqual(result['Daniel']['amount'], 0.0)

