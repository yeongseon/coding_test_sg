from ccpayment.command_parser import Parser
from ccpayment.command_processor import Processor
# import click 사용하기, command_parser 만들 필요 없음.
import sys

parser = Parser()
processor = Processor()

commands = []
if len(sys.argv) > 1:
    file = open(sys.argv[1])
    lines = file.readlines()
    commands = parser.get_commands(lines)
else:
    commands = parser.get_commands(sys.stdin)

result = processor.process(commands)
processor.print_result(result)

# def main() 만들 것
