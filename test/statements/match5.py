match command.split() if command else ['default']:
    ... # Other cases
    case ["north"] | ["go", "north"]:
        ... # handle case
    case ["get", obj] | ["pick", "up", *other] | ["pick", obj, "up"]:
        ... # handle case




match         : keyword.control.flow.python, source.sage
              : source.sage
command       : source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
split         : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.sage
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
if            : keyword.control.flow.python, source.sage
              : source.sage
command       : source.sage
              : source.sage
else          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
default       : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 Other cases  : comment.line.number-sign.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
north         : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.sage
              : source.sage
|             : keyword.operator.bitwise.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
go            : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
north         : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 handle case  : comment.line.number-sign.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
get           : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
obj           : source.sage
]             : punctuation.definition.list.end.python, source.sage
              : source.sage
|             : keyword.operator.bitwise.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
pick          : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
up            : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
*             : keyword.operator.arithmetic.python, source.sage
other         : source.sage
]             : punctuation.definition.list.end.python, source.sage
              : source.sage
|             : keyword.operator.bitwise.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
pick          : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
obj           : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
up            : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 handle case  : comment.line.number-sign.python, source.sage
