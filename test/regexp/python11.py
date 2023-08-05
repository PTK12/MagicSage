a = r"""
    (?x)        # multi-XXXline XXX regexp
        foo     (?# comm TODOent TODO)
        foo     # type: int
        foo     (?# type: int)
"""



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
 multi-XXXline  : comment.line.number-sign.python, source.sage, string.regexp.quoted.multi.python
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.sage, string.regexp.quoted.multi.python
 regexp       : comment.line.number-sign.python, source.sage, string.regexp.quoted.multi.python
        foo      : source.sage, string.regexp.quoted.multi.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.sage, string.regexp.quoted.multi.python
 comm TODOent  : comment.regexp, source.sage, string.regexp.quoted.multi.python
TODO          : comment.regexp, keyword.codetag.notation.python, source.sage, string.regexp.quoted.multi.python
)             : comment.regexp, punctuation.comment.end.regexp, source.sage, string.regexp.quoted.multi.python
        foo      : source.sage, string.regexp.quoted.multi.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage, string.regexp.quoted.multi.python
 type: int    : comment.line.number-sign.python, source.sage, string.regexp.quoted.multi.python
        foo      : source.sage, string.regexp.quoted.multi.python
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.sage, string.regexp.quoted.multi.python
 type: int    : comment.regexp, source.sage, string.regexp.quoted.multi.python
)             : comment.regexp, punctuation.comment.end.regexp, source.sage, string.regexp.quoted.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
