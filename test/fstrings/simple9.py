f'foo {{{bar}}}'




f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
foo           : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.sage
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
bar           : meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
}}            : constant.character.escape.python, meta.fstring.python, source.sage
'             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
