#:
    @asd
    def foo():
        pass



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
:             : comment.line.number-sign.python, source.sage
              : meta.function.decorator.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
asd           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
