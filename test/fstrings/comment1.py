f'prefix{10 # comment, making the string technically illegal
def foo(): pass




f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
prefix        : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
10            : constant.numeric.dec.python, meta.fstring.python, source.sage
 #            : meta.fstring.python, source.sage
comment       : meta.fstring.python, source.sage
,             : meta.fstring.python, punctuation.separator.element.python, source.sage
              : meta.fstring.python, source.sage
making        : meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
the           : meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
string        : meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
technically   : meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
illegal       : meta.fstring.python, source.sage
              : invalid.illegal.newline.python, meta.fstring.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
