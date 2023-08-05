def myfunc(self,            # gotta have self
           param1="value",  # values are cool
           param2=True,     # or False, whatever
           **kwargs):       # you never know
    pass



def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
myfunc        : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
self          : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python, variable.parameter.function.language.special.self.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 gotta have self : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
param1        : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
"             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
value         : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
"             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 values are cool : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
param2        : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
True          : constant.language.python, meta.function.parameters.python, meta.function.python, source.sage
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 or False, whatever : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
**            : keyword.operator.unpacking.parameter.python, meta.function.parameters.python, meta.function.python, source.sage
kwargs        : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 you never know : comment.line.number-sign.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
