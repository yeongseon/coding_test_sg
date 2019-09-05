from ccpayment.command_parser import Parser
from ccpayment.command_processor import Processor
import sys

parser = Parser()
processor = Processor()


def main():
    commands = []
    if len(sys.argv) > 1:
        file = open(sys.argv[1])
        lines = file.readlines()
        commands = parser.get_commands(lines)
    else:
        commands = parser.get_commands(sys.stdin)

    result = processor.process(commands)
    processor.print_result(result)

if __name__ == '__main__':
    main()
