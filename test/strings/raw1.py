a = R"""
multiline "raw" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.multi.python
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
multiline "raw" string  : source.sage, string.quoted.raw.multi.python
\             : source.sage, string.quoted.raw.multi.python
              : source.sage, string.quoted.raw.multi.python
    \xf1 \u1234aaaa \U1234aaaa : source.sage, string.quoted.raw.multi.python
              : source.sage, string.quoted.raw.multi.python
    \N        : source.sage, string.quoted.raw.multi.python
{BLACK SPADE SUIT} : source.sage, string.quoted.raw.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.raw.multi.python
