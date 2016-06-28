#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Program for tesing of the terminal's coloring capabilities
"""

from __future__ import print_function

import os
import sys
import re
import doctest

import termcolor


def parse_palette(input_str):
    """Builds a palette from string

    Typical usage:

    >>> [parse_palette('R=red-:G=green:B=blue+')[k] for k in 'RGB']
    [('red', ('dark',)), ('green', ()), ('blue', ('bold',))]

    Spaces in input must be ignored:
    >>> parse_palette('   R = red   +')
    {'R': ('red', ('bold',))}

    Input must be well-formed:

    >>> parse_palette(':::')
    Traceback (most recent call last):
        ...
    AssertionError
    >>> parse_palette('a=')
    Traceback (most recent call last):
        ...
    AssertionError
    >>> parse_palette('red=red')
    Traceback (most recent call last):
        ...
    AssertionError
    >>> parse_palette('=blue')
    Traceback (most recent call last):
        ...
    AssertionError

    Color must be presented in termcolor.COLORS:

    >>> bool(parse_palette('a=red'))
    True
    >>> parse_palette('a=redd')
    Traceback (most recent call last):
        ...
    AssertionError
    """
    re_item = re.compile(r'\s*(.)\s*=\s*([a-z]+)\s*([+-])?\s*')
    parse_attr = {'+': ('bold',), '-': ('dark',)}.get

    result = {}
    for item in input_str.split(':'):
        match = re_item.match(item)
        assert match
        char, color, attr_char = match.groups()
        assert color in termcolor.COLORS
        result[char] = (color, parse_attr(attr_char) or ())
    return result


DEFAULT_PALETTE = '~=blue : .=white : #=green : O=white+ : ^=red- : ==red-'

UNDEFINED = ('red', ['bold', 'blink'])


def colorize(palette, char):
    """Returns a colorized char (according to palette)

    >>> pal = {'a': ('red', ['dark'])}
    >>> colorize(pal, 'a') == termcolor.colored('a', 'red', attrs=['dark'])
    True
    >>> colorize(pal, 'b') == (
    ...    termcolor.colored('b', UNDEFINED[0], attrs=UNDEFINED[1]))
    True

    Newlines stay uncolored:

    >>> colorize({}, '\\n') == '\\n'
    True
    """
    if char == '\n':
        return char
    color, attrs = palette.get(char, UNDEFINED)
    return termcolor.colored(char, color, attrs=attrs)


def main(files):
    """Runs a module as a program
    """
    if not files:
        print('Usage:\n  termcolor_test.py <file>[ <file>[ ...]]')
    else:
        palette = parse_palette(
            os.environ.get('TERMCOLOR_PALETTE', DEFAULT_PALETTE))

        def process(readable):
            """Colorizes one file-like object"""
            print(''.join(colorize(palette, ch) for ch in readable.read()))

        for fname in files:
            if fname == '-':
                process(sys.stdin)
            else:
                with open(fname) as input_file:
                    process(input_file)


if __name__ == '__main__':
    if os.environ.get('TEST'):
        doctest.testmod()
    else:
        sys.exit(main(sys.argv[1:]) or 0)
