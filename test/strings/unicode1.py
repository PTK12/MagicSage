a = """
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.multi.python
multiline "unicode" string  : source.sage, string.quoted.multi.python
\             : constant.language.python, source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
\xf1          : constant.character.escape.python, source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
\u1234        : constant.character.escape.python, source.sage, string.quoted.multi.python
aaaa          : source.sage, string.quoted.multi.python
\U1234aaaa    : constant.character.escape.python, source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, source.sage, string.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.multi.python
