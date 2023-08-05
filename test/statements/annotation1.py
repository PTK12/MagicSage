some_number: int           # variable without initial value
some_list: List[int] = []  # variable with initial value




some_number   : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
int           : source.sage, support.type.python
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 variable without initial value : comment.line.number-sign.python, source.sage
some_list     : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
List          : meta.indexed-name.python, meta.item-access.python, source.sage
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.sage
int           : meta.item-access.arguments.python, meta.item-access.python, source.sage, support.type.python
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
]             : punctuation.definition.list.end.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 variable with initial value : comment.line.number-sign.python, source.sage
