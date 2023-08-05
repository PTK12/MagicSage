a = r"foo#not a comment"
a = r"""
    (?x)        # multi-line regexp
        foo     # comment
"""
a = R"""
    (?x)        # not a
        foo     # comment
"""



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.single.python
foo#not a comment : source.sage, string.regexp.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.single.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
(?x)          : source.sage, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage, string.regexp.quoted.multi.python
 multi-line regexp : comment.line.number-sign.python, source.sage, string.regexp.quoted.multi.python
        foo      : source.sage, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage, string.regexp.quoted.multi.python
 comment      : comment.line.number-sign.python, source.sage, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.multi.python
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
    (?x)        # not a : source.sage, string.quoted.raw.multi.python
        foo     # comment : source.sage, string.quoted.raw.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.raw.multi.python
