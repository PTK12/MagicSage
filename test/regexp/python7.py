a = r'('
1

a = r"(?="
1

a = r"""(?:
"""
1

a = r'''[
'''
1



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.single.python
(             : punctuation.parenthesis.begin.regexp, source.sage, string.regexp.quoted.single.python, support.other.parenthesis.regexp
'             : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.single.python
1             : constant.numeric.dec.python, source.sage
              : source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.single.python
(             : keyword.operator.lookahead.regexp, punctuation.parenthesis.lookahead.begin.regexp, source.sage, string.regexp.quoted.single.python
?=            : keyword.operator.lookahead.regexp, source.sage, string.regexp.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.single.python
1             : constant.numeric.dec.python, source.sage
              : source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
(?:           : punctuation.parenthesis.non-capturing.begin.regexp, source.sage, string.regexp.quoted.multi.python, support.other.parenthesis.regexp
"""           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
1             : constant.numeric.dec.python, source.sage
              : source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
1             : constant.numeric.dec.python, source.sage
