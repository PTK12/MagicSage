class F:
    def __init__(self, a, b=1):
        self.a = a
        self.b = b
        print(self)
        self()
        a.self = 1
        a.self.bar = 2
        self[123]




class         : meta.class.python, source.sage, storage.type.class.python
              : meta.class.python, source.sage
F             : entity.name.type.class.python, meta.class.python, source.sage
:             : meta.class.python, punctuation.section.class.begin.python, source.sage
              : meta.function.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
__init__      : meta.function.python, source.sage, support.function.magic.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
self          : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python, variable.parameter.function.language.special.self.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
b             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
1             : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
self          : source.sage, variable.language.special.self.python
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
a             : meta.attribute.python, meta.member.access.python, source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
a             : source.sage
              : source.sage
self          : source.sage, variable.language.special.self.python
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
b             : meta.attribute.python, meta.member.access.python, source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
b             : source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
self          : meta.function-call.arguments.python, meta.function-call.python, source.sage, variable.language.special.self.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
self          : meta.function-call.python, source.sage, variable.language.special.self.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
a             : source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
self          : meta.attribute.python, meta.member.access.python, source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
1             : constant.numeric.dec.python, source.sage
              : source.sage
a             : source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
self          : meta.attribute.python, meta.member.access.python, source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
bar           : meta.attribute.python, meta.member.access.python, source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
2             : constant.numeric.dec.python, source.sage
              : source.sage
self          : meta.item-access.python, source.sage, variable.language.special.self.python
[             : meta.item-access.python, punctuation.definition.arguments.begin.python, source.sage
123           : constant.numeric.dec.python, meta.item-access.arguments.python, meta.item-access.python, source.sage
]             : meta.item-access.python, punctuation.definition.arguments.end.python, source.sage
