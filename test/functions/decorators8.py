@deco().abc  # SyntaxError: invalid syntax
def foo(): pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
deco          : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
.abc          : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 SyntaxError: invalid syntax : comment.line.number-sign.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
