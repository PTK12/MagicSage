@some_decorator # with comment
@some.class.decorator
@some_decorator(1)
@some.decorator   (1, 3)
@some_decorator(a=2, b={'q': 42}, **kwargs)
@classmethod
def decorated(a): pass



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
some_decorator : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 with comment : comment.line.number-sign.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
some          : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
class         : keyword.control.flow.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
decorator     : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
some_decorator : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
some          : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
.             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.separator.period.python, source.sage
decorator     : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
,             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
3             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
some_decorator : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
a             : meta.function-call.arguments.python, meta.function.decorator.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
2             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
,             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
b             : meta.function-call.arguments.python, meta.function.decorator.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
{             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.dict.begin.python, source.sage
'             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
q             : meta.function-call.arguments.python, meta.function.decorator.python, source.sage, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
:             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.dict.python, source.sage
              : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
42            : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
}             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.definition.dict.end.python, source.sage
,             : meta.function-call.arguments.python, meta.function.decorator.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
**            : keyword.operator.unpacking.arguments.python, meta.function-call.arguments.python, meta.function.decorator.python, source.sage
kwargs        : meta.function-call.arguments.python, meta.function.decorator.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
classmethod   : meta.function.decorator.python, source.sage, support.type.python
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
decorated     : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
