a[1] = b'''
multiline 'binary' string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
'''




a             : meta.indexed-name.python, meta.item-access.python, source.sage
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.sage
1             : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.sage
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
b             : source.sage, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.multi.python
multiline 'binary' string  : source.sage, string.quoted.binary.multi.python
\             : constant.language.python, source.sage, string.quoted.binary.multi.python
              : source.sage, string.quoted.binary.multi.python
              : source.sage, string.quoted.binary.multi.python
\xf1          : constant.character.escape.python, source.sage, string.quoted.binary.multi.python
 \u1234aaaa \U1234aaaa : source.sage, string.quoted.binary.multi.python
              : source.sage, string.quoted.binary.multi.python
    \N{BLACK SPADE SUIT} : source.sage, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.binary.multi.python
