# termcolor_test

### What is it

This is a pretty simple tool/toy which colorizes its input and prints result to
the ``STDOUT``. Coloring rules are pretty simple: one char - one color.
A ``char->color`` mapping can be easily customized through environment variable.

This project was heavily inspired by [this post](http://eax.me/python-termcolor/)
from @afiskon.

### Usage

Just install one prerequisite - [termcolor](https://pypi.python.org/pypi/termcolor)
library and then run:

```shell
$ python termcolor_test.py map.txt
...
```

Of course you can do some piping:

```shell
$ cat map.txt | python termcolor_test.py -
...
```

Program was tested with Python 2.7 and Python 3.4 and works fine with both. You can test
it with your version of interpreter. Just do:

```shell
$ TEST=true python termcolor_test.py
```

If no warnings or errors appeared then everything is OK :)

### "Pallete" customization

A mapping ``char->color`` can be customized in a way:

```shell
$ export TERMCOLOR_PALETTE="x=red : o=white+"
$ echo -e "xox\nxxo\nooo" | python termcolor_test.py -
```

Each item of palette (``o=white+`` for example) contains:

1. A char to color ``o``
1. Equality sign ``=``
1. Color name. Possible values:
   - ``grey``
   - ``red``
   - ``green``
   - ``yellow``
   - ``blue``
   - ``magenta``
   - ``cyan``
   - ``white``
1. Optional color modifier. Here ``+`` means "bright" (``bold`` in
ANSI Terminal lexicon) and ``-`` means "dark".

### Contribution

You can freely use all of the stuff in this repo. And any kind of
PRs and proposals is welcomed.
