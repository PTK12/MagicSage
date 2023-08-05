->
def f(): pass
$
?
a=$('.class').fuuuu(baz=1)
# we recover just fine
b = !some_ruby?
# hey ;)




->            : invalid.illegal.annotation.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
f             : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
$             : invalid.illegal.operator.python, source.sage
?             : invalid.illegal.operator.python, source.sage
a             : source.sage
=             : keyword.operator.assignment.python, source.sage
$             : invalid.illegal.operator.python, source.sage
(             : punctuation.parenthesis.begin.python, source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
.class        : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : punctuation.parenthesis.end.python, source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
fuuuu         : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.sage
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.sage
baz           : meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage
)             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.end.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 we recover just fine : comment.line.number-sign.python, source.sage
b             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
!             : invalid.illegal.operator.python, source.sage
some_ruby     : source.sage
?             : invalid.illegal.operator.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 hey ;)       : comment.line.number-sign.python, source.sage
