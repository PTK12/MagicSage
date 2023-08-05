match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis are in the list.")
    case _:
        print("Something else is found in the list.")



match         : keyword.control.flow.python, source.sage
              : source.sage
points        : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
No points in the list. : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
The origin is the only point in the list. : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
A single point is in the list. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
[             : punctuation.definition.list.begin.python, source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y1            : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y2            : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
]             : punctuation.definition.list.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
Two points on the Y axis are in the list. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
_             : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
Something else is found in the list. : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
