a = r'''foo[abc] # comment'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
foo           : source.sage, string.regexp.quoted.multi.python
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.sage, string.regexp.quoted.multi.python
a             : constant.character.set.regexp, meta.character.set.regexp, source.sage, string.regexp.quoted.multi.python
b             : constant.character.set.regexp, meta.character.set.regexp, source.sage, string.regexp.quoted.multi.python
c             : constant.character.set.regexp, meta.character.set.regexp, source.sage, string.regexp.quoted.multi.python
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage, string.regexp.quoted.multi.python
 comment      : comment.line.number-sign.python, source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
