rf'fo{{2}}'
rf"fo{{2}}"
rf'''fo{{2}}'''
rf"""fo{{2}}"""




rf            : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
fo            : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.sage
2             : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
}}            : constant.character.escape.python, meta.fstring.python, source.sage
'             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
rf            : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.raw.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
fo            : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
{{            : constant.character.escape.python, meta.fstring.python, source.sage
2             : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
}}            : constant.character.escape.python, meta.fstring.python, source.sage
"             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.raw.single.python
rf            : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.raw.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
fo            : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
{{            : constant.character.escape.python, meta.fstring.python, source.sage
2             : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
}}            : constant.character.escape.python, meta.fstring.python, source.sage
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
rf            : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.raw.multi.python
"""           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
fo            : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
{{            : constant.character.escape.python, meta.fstring.python, source.sage
2             : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
}}            : constant.character.escape.python, meta.fstring.python, source.sage
"""           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.raw.multi.python
