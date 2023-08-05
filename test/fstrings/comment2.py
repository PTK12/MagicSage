f'''
    prefix{10
    + 32} suffix'''




f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
    prefix    : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
10            : constant.numeric.dec.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
32            : constant.numeric.dec.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
 suffix       : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.multi.python
