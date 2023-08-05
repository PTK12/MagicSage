def foo()
    -> notOK:
    pass



def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
              : source.sage
->            : invalid.illegal.annotation.python, source.sage
              : source.sage
notOK         : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
