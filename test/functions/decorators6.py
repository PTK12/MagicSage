@a.   b  .  \
   c.None.z(foo=BAR). \
       baz[1:2]
@foo.class.bar[]
@foo.ok '''
def foo(): pass




@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
a             : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
              : meta.function.decorator.python, source.sage
b             : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
              : meta.function.decorator.python, source.sage
\             : meta.function.decorator.python, punctuation.separator.continuation.line.python, source.sage
              : meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
c             : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
None          : keyword.illegal.name.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
z             : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
foo           : meta.function-call.arguments.python, meta.function.decorator.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
BAR           : constant.other.caps.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
. \           : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
              : source.sage
baz           : meta.indexed-name.python, meta.item-access.python, source.sage
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.sage
1             : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.sage
:             : meta.item-access.arguments.python, meta.item-access.python, punctuation.separator.slice.python, source.sage
2             : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.sage
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
class         : keyword.control.flow.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
[]            : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
ok            : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
'''           : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
