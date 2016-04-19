'''
RHPCOpattern - Exploit Pattern Tool
rakkapriccio@gmail.com
twitter: @rhpco
'''
import argparse
import os
import sys
import textwrap
from string import uppercase, lowercase, digits
MAX_PATTERN_LENGTH = 20280

def CommandLine():
    parser = argparse.ArgumentParser(
          prog='RHPCOpattern.py',
          usage='\n%(prog)s generate  100 \n%(prog)s search  0x41346141',
          formatter_class=argparse.RawDescriptionHelpFormatter,
          description=textwrap.dedent('''\
      ______ _   _ ______  _____ _____
      | ___ \ | | || ___ \/  __ \  _  |
      | |_/ / |_| || |_/ /| /  \/ | | |
      |    /|  _  ||  __/ | |   | | | |
      | |\ \| | | || |    | \__/\ \_/ /
      \_| \_\_| |_/\_|     \____/\___/ pattern
                  Exploit Pattern Tool
                  Pattern generator and searcher like
                  metasploit-framework/tools/pattern_create.rb
                      ''')
    )
    subparsers = parser.add_subparsers()
    parser.add_argument('generate', nargs='?', help='generate pattern length')
    parser.add_argument('search',  nargs='?', help='search pattern position')

    generate_parser = subparsers.add_parser('generate')
    generate_parser.add_argument('length')
    generate_parser.set_defaults(func=generate)

    search_parser = subparsers.add_parser('search')
    search_parser.add_argument('pattern')
    search_parser.set_defaults(func=search)
    return parser

def generate(args):
    pattern = pattern_generator(args.length)
    print pattern
def pattern_generator(length):
    length = int(length)
    if length >= MAX_PATTERN_LENGTH:
        print 'ERROR: Pattern length exceeds maximum of %d' % MAX_PATTERN_LENGTH
        sys.exit(1)
    result = ''
    for upper in uppercase:
        for lower in lowercase:
            for digit in digits:
                if len(result) < length:
                    result += upper+lower+digit
                else:
                    return result[:length]

def search(args):
    result = pattern_searcher(args.pattern)
    print('Pattern %s found at position %d' %(args.pattern, result))
def pattern_searcher(search_pattern):
    needle = search_pattern
    try:
        if needle.startswith('0x'):
            # Strip off '0x', convert to ASCII and reverse
            needle = needle[2:].decode('hex')
            needle = needle[::-1]
    except TypeError as e:
        print 'Error convert hex:', e
        sys.exit(1)
    haystack = ''
    for upper in uppercase:
        for lower in lowercase:
            for digit in digits:
                haystack += upper+lower+digit
                found_at = haystack.find(needle)
                if found_at > -1:
                    return found_at
                    
if __name__ == '__main__':
    parser = CommandLine()
    if len(sys.argv) < 2:
        parser.print_help()
        exit()
    else:
        args = parser.parse_args()
        args.func(args)
