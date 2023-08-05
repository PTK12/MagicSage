# testing annotations split over multiple lines
def foo(a:('abc' 'def')==123, boo: 'abc'

                         'def' == foo(n(m=0)))



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 testing annotations split over multiple lines : comment.line.number-sign.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.begin.python, source.sage
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
abc           : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.sage
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
def           : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.end.python, source.sage
==            : keyword.operator.comparison.python, meta.function.parameters.python, meta.function.python, source.sage
123           : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
boo           : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
abc           : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.sage
                          : meta.function.parameters.python, meta.function.python, source.sage
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
def           : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : meta.function.parameters.python, meta.function.python, source.sage
==            : keyword.operator.comparison.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
foo           : meta.function-call.generic.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.sage
(             : meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.begin.python, source.sage
n             : meta.function-call.arguments.python, meta.function-call.generic.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.sage
(             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.begin.python, source.sage
m             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.sage
0             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, source.sage
)             : meta.function-call.arguments.python, meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.end.python, source.sage
)             : meta.function-call.python, meta.function.parameters.python, meta.function.python, punctuation.definition.arguments.end.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
