a = f"""
multiline "unicode" string
    \N{BLACK SPADE SUIT} {foo+2}
"""



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
multiline "unicode" string : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
foo           : meta.fstring.python, source.sage
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.sage
2             : constant.numeric.dec.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.multi.python
