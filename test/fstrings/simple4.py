a = f'''hello { foo("bar")/23 !r:f} times'''




a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.multi.python
hello         : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
foo           : meta.fstring.python, meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
bar           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
/             : keyword.operator.arithmetic.python, meta.fstring.python, source.sage
23            : constant.numeric.dec.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
!r            : meta.fstring.python, source.sage, storage.type.format.python
:f            : meta.fstring.python, source.sage, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
 times        : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.multi.python
