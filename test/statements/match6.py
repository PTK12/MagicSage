match (foo + bar):
    ... # cases
match [foo, bar]:
    ... # cases
match {foo, bar}:
    ... # cases




match         : keyword.control.flow.python, source.sage
              : source.sage
(             : punctuation.parenthesis.begin.python, source.sage
foo           : source.sage
              : source.sage
+             : keyword.operator.arithmetic.python, source.sage
              : source.sage
bar           : source.sage
)             : punctuation.parenthesis.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
foo           : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
bar           : source.sage
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
{             : punctuation.definition.dict.begin.python, source.sage
foo           : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
bar           : source.sage
}             : punctuation.definition.dict.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage