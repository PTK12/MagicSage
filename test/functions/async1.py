@foo
async def foo():
    a = 1
    async for a, b, c in b:
        async with b as d, c:
            await func(a, b=1)



@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
async         : meta.function.python, source.sage, storage.type.function.async.python
              : meta.function.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
1             : constant.numeric.dec.python, source.sage
              : source.sage
async         : keyword.control.flow.python, source.sage
              : source.sage
for           : keyword.control.flow.python, source.sage
              : source.sage
a             : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
b             : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
c             : source.sage
              : source.sage
in            : keyword.control.flow.python, source.sage
              : source.sage
b             : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
async         : keyword.control.flow.python, source.sage
              : source.sage
with          : keyword.control.flow.python, source.sage
              : source.sage
b             : source.sage
              : source.sage
as            : keyword.control.flow.python, source.sage
              : source.sage
d             : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
c             : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
await         : keyword.control.flow.python, source.sage
              : source.sage
func          : meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
a             : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
b             : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
