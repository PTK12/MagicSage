replace = {'"' : R'\"',
           "'" : R'\'',
           '\\': R'\\'}



replace       : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
{             : punctuation.definition.dict.begin.python, source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
"             : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
:             : punctuation.separator.dict.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
\"            : source.sage, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.raw.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
'             : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
:             : punctuation.separator.dict.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
\'            : source.sage, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.raw.single.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
\\            : constant.character.escape.python, source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
:             : punctuation.separator.dict.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
\\            : source.sage, string.quoted.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.raw.single.python
}             : punctuation.definition.dict.end.python, source.sage
