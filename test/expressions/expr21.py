while chunk := file.read(8192):
   process(chunk)
   y0 = (y1 := f(x))



while         : keyword.control.flow.python, source.sage
              : source.sage
chunk         : source.sage
              : source.sage
:=            : keyword.operator.assignment.python, source.sage
              : source.sage
file          : source.sage, variable.legacy.builtin.python
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
read          : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.sage
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.sage
8192          : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage
)             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
process       : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
chunk         : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
y0            : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
(             : punctuation.parenthesis.begin.python, source.sage
y1            : source.sage
              : source.sage
:=            : keyword.operator.assignment.python, source.sage
              : source.sage
f             : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
x             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
)             : punctuation.parenthesis.end.python, source.sage
