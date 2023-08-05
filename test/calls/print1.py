print "is", 2*2
print("is", 2*2)
print x,
print(x, end=" ")
print
print()
print >>sys.stderr, "er"
print("er", file=sys.stderr)
print (x, y)
print((x, y))




print         : source.sage, support.function.builtin.python
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
is            : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
2             : constant.numeric.dec.python, source.sage
*             : keyword.operator.arithmetic.python, source.sage
2             : constant.numeric.dec.python, source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
is            : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
2             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
*             : keyword.operator.arithmetic.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
2             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
print         : source.sage, support.function.builtin.python
              : source.sage
x             : source.sage
,             : punctuation.separator.element.python, source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
end           : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
              : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
print         : source.sage, support.function.builtin.python
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
print         : source.sage, support.function.builtin.python
              : source.sage
>>            : keyword.operator.bitwise.python, source.sage
sys           : source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
stderr        : meta.attribute.python, meta.member.access.python, source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
er            : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
er            : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
file          : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
sys           : meta.function-call.arguments.python, meta.function-call.python, source.sage
.             : meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, punctuation.separator.period.python, source.sage
stderr        : meta.attribute.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
              : meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
(             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.element.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
y             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.arguments.python, meta.function-call.python, punctuation.parenthesis.end.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
