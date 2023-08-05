@ f . bar (baz = 1)
def foo(): pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
f             : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
              : meta.function.decorator.python, source.sage
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
baz           : meta.function-call.arguments.python, meta.function.decorator.python, source.sage, variable.parameter.function-call.python
              : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
              : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
