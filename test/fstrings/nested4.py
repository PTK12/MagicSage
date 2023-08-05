f"""result: {value:{60}.{16!s:2}{'qwerty'
[2]}}"""
def foo(): pass




f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.multi.python
result:       : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
value         : meta.fstring.python, source.sage
:             : meta.fstring.python, source.sage, storage.type.format.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
60            : constant.numeric.dec.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
.             : meta.fstring.python, source.sage
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
16            : constant.numeric.dec.python, meta.fstring.python, source.sage
!s            : meta.fstring.python, source.sage, storage.type.format.python
:2            : meta.fstring.python, source.sage, storage.type.format.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
qwerty        : meta.fstring.python, source.sage, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
[             : meta.fstring.python, punctuation.definition.list.begin.python, source.sage
2             : constant.numeric.dec.python, meta.fstring.python, source.sage
]             : meta.fstring.python, punctuation.definition.list.end.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.multi.python
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
