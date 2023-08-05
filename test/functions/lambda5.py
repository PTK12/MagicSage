anon = lambda -> qqq[None]: None
def f(): return 1 # this line should not break



anon          : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
lambda        : meta.lambda-function.python, source.sage, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.lambda-function.python, source.sage
->            : invalid.illegal.annotation.python, meta.function.lambda.parameters.python, meta.lambda-function.python, source.sage
 qqq[None]    : meta.function.lambda.parameters.python, meta.lambda-function.python, source.sage
:             : meta.lambda-function.python, punctuation.section.function.lambda.begin.python, source.sage
              : source.sage
None          : constant.language.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
f             : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
return        : keyword.control.flow.python, source.sage
              : source.sage
1             : constant.numeric.dec.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 this line should not break : comment.line.number-sign.python, source.sage
