import sys
from ccpayment.command_parser import Parser


def usage():
    print("""
    
   """)

class OptionTrigger():
    def parse_arg(self, args):
        print(args)



def main():
    optionTrigger = OptionTrigger()
    if len(sys.argv) <= 1:
        usage()
        return 0
    print(sys.argv)

    # 여기서 기능이 실행 되어야 함
