import unittest
from ccpayment.command_parser import Parser
lines = [
    "Add Jane 4111111111111111 $1000",
    "Add Evan 5454545454545454 $3000",
    "Add Daniel 1234567890123456 $2000",
    "Charge Jane $500",
    "Charge Jane $800",
    "Charge Evan $7",
    "Credit Evan $100",
    "Credit Daniel $200"
]
class CommandParserTest(unittest.TestCase):
    def test_parse(self):
        parser = Parser()
        commands = parser.get_commands(lines)
        print("=>", commands)
        self.assertEqual(commands[0]['command'], "Add")
        self.assertEqual(commands[0]['name'], "Jane")

    def test_not_support_cmd(self):
        parser = Parser()
        commands = parser.get_commands("./test_not_support_input.txt")
        self.assertEqual(commands, [])




