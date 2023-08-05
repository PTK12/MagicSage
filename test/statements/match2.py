match point:
    case Point(x=0, y=0):
        print("Origin is the point's location.")
    case Point(x=0, y=y):
        print(f"The point is on the y-axis.")
    case Point(x=x, y=0):
        print(f"The point is on the x-axis.")
    case Point():
        print("The point is located somewhere else on the plane.")
    case _:
        print("Not a point")



match         : keyword.control.flow.python, source.sage
              : source.sage
point         : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
Origin is the point's location. : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
The point is on the y-axis. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
The point is on the x-axis. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
The point is located somewhere else on the plane. : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
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
Not a point   : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
