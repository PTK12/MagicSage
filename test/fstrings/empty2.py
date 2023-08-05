rf"{} {  }"
rf"""{}
{  }
"""





rf            : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : invalid.illegal.brace.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
"             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
rf            : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.raw.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : invalid.illegal.brace.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
