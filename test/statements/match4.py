match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")




match         : keyword.control.flow.python, source.sage
              : source.sage
point         : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
if            : keyword.control.flow.python, source.sage
              : source.sage
x             : source.sage
              : source.sage
==            : keyword.operator.comparison.python, source.sage
              : source.sage
y             : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
The point is located on the diagonal Y=X. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
Point         : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
Point is not on the diagonal. : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
