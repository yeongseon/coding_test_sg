import unittest
from ccpayment.command_parser import Parser

class CommandParserTest(unittest.TestCase):
    def test_parse(self):
        parser = Parser()
        commands = parser.get_commands("./input.txt")
        self.assertEqual(commands[0]['command'], "Add")
        self.assertEqual(commands[0]['name'], "Jane")

    def test_not_support_cmd(self):
        parser = Parser()
        commands = parser.get_commands("./test_not_support_input.txt")
        self.assertEqual(commands, [])




