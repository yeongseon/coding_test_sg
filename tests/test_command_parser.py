import unittest
from ccpayment.command_parser import Parser
import sys

class CommandParserTest(unittest.TestCase):
    def test_parse(self):
        parser = Parser()
        file = open(sys.path[1] + "/inputs/input.txt")
        commands = parser.get_commands(file.readlines())
        print("=>", commands)
        self.assertEqual(commands[0]['command'], "Add")
        self.assertEqual(commands[0]['name'], "Jane")

    def test_not_support_cmd(self):
        parser = Parser()
        commands = parser.get_commands("./test_not_support_input.txt")
        self.assertEqual(commands, [])




