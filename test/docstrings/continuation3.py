# not a docstring
a = \
r'>>> print(42)a[wer]'

b = \
# docstring
r'>>> print()a[wer]'



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 not a docstring : comment.line.number-sign.python, source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.single.python
>>> print     : source.sage, string.regexp.quoted.single.python
(             : punctuation.parenthesis.begin.regexp, source.sage, string.regexp.quoted.single.python, support.other.parenthesis.regexp
42            : source.sage, string.regexp.quoted.single.python
)             : punctuation.parenthesis.end.regexp, source.sage, string.regexp.quoted.single.python, support.other.parenthesis.regexp
a             : source.sage, string.regexp.quoted.single.python
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.sage, string.regexp.quoted.single.python
w             : constant.character.set.regexp, meta.character.set.regexp, source.sage, string.regexp.quoted.single.python
e             : constant.character.set.regexp, meta.character.set.regexp, source.sage, string.regexp.quoted.single.python
r             : constant.character.set.regexp, meta.character.set.regexp, source.sage, string.regexp.quoted.single.python
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.sage, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.single.python
              : source.sage
b             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 docstring    : comment.line.number-sign.python, source.sage
r             : source.sage, storage.type.string.python, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.single.python
>>> print()a[wer] : source.sage, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.single.python
