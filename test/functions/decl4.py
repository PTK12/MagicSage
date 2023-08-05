# testing annotations split over multiple lines
def some_func(a:
                 lambda x=None:
                    {key: val
                        for key, val in
                            (x if x is not None else [])
                    }=42):




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 testing annotations split over multiple lines : comment.line.number-sign.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
some_func     : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.sage
                  : meta.function.parameters.python, meta.function.python, source.sage
lambda        : meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.sage, storage.type.function.lambda.python
              : meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.sage
x             : meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.sage
None          : constant.language.python, meta.function.lambda.parameters.python, meta.function.parameters.python, meta.function.python, meta.lambda-function.python, source.sage
:             : meta.function.parameters.python, meta.function.python, meta.lambda-function.python, punctuation.section.function.lambda.begin.python, source.sage
                     : meta.function.parameters.python, meta.function.python, source.sage
{             : meta.function.parameters.python, meta.function.python, punctuation.definition.dict.begin.python, source.sage
key           : meta.function.parameters.python, meta.function.python, source.sage
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.dict.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
val           : meta.function.parameters.python, meta.function.python, source.sage
                         : meta.function.parameters.python, meta.function.python, source.sage
for           : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
key           : meta.function.parameters.python, meta.function.python, source.sage
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.element.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
val           : meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
in            : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.sage
                             : meta.function.parameters.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.begin.python, source.sage
x             : meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
if            : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
x             : meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
is            : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
not           : keyword.operator.logical.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
None          : constant.language.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
else          : keyword.control.flow.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
[             : meta.function.parameters.python, meta.function.python, punctuation.definition.list.begin.python, source.sage
]             : meta.function.parameters.python, meta.function.python, punctuation.definition.list.end.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.parenthesis.end.python, source.sage
                     : meta.function.parameters.python, meta.function.python, source.sage
}             : meta.function.parameters.python, meta.function.python, punctuation.definition.dict.end.python, source.sage
=             : keyword.operator.assignment.python, meta.function.parameters.python, meta.function.python, source.sage
42            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
