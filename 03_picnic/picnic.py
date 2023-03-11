#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Picnic Game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic Game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')


    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sort = args.sorted
    items = args.item

    if sort == True:
        items = sorted(items)

    if len(items) == 1:
        print(f"You are bringing {items[0]}.")
    elif len(items) == 2:
        print(f"You are bringing {items[0]} and {items[1]}.")
    elif len(items) == 0 :
        print(f"You should bring some food.")
    else:
        str_items=', '.join(items[:-1])
        print(f"You are bringing {str_items}, and {items[-1]}.")
    


# --------------------------------------------------
if __name__ == '__main__':
    main()
