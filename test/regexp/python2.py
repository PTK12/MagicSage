a = r'
    (?x)
        foo
'
# comment



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.single.python
              : invalid.illegal.newline.python, source.sage, string.regexp.quoted.single.python
              : source.sage
(             : punctuation.parenthesis.begin.python, source.sage
?             : invalid.illegal.operator.python, source.sage
x             : source.sage
)             : punctuation.parenthesis.end.python, source.sage
              : source.sage
foo           : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
              : invalid.illegal.newline.python, source.sage, string.quoted.docstring.single.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 comment      : comment.line.number-sign.python, source.sage
