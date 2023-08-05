a = "normal {{ normal }} normal {10!r} normal {fo.__add__!s}".format(fo=1)




a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
normal        : source.sage, string.quoted.single.python
{{            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
 normal       : source.sage, string.quoted.single.python
}}            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
 normal       : source.sage, string.quoted.single.python
{10           : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
!r            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, storage.type.format.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
 normal       : source.sage, string.quoted.single.python
{fo.__add__   : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
!s            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, storage.type.format.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
format        : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.sage
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.sage
fo            : meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage, variable.parameter.function-call.python
=             : keyword.operator.assignment.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage
1             : constant.numeric.dec.python, meta.function-call.arguments.python, meta.function-call.python, meta.member.access.python, source.sage
)             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.end.python, source.sage
