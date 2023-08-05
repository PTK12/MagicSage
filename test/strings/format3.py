a = '%i' % 42
a = "%(language)s has %(number)03d quote types."
a = b"%(language)s has %(number)03d quote types."
a = R"%(language)s has %(number)03d quote types."



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
%i            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
%             : keyword.operator.arithmetic.python, source.sage
              : source.sage
42            : constant.numeric.dec.python, source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
%(language)s  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
 has          : source.sage, string.quoted.single.python
%(number)03d  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
 quote types. : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
b             : source.sage, storage.type.string.python, string.quoted.binary.single.python
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.single.python
%(language)s  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.binary.single.python
 has          : source.sage, string.quoted.binary.single.python
%(number)03d  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.binary.single.python
 quote types. : source.sage, string.quoted.binary.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.binary.single.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.single.python
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.single.python
%(language)s  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.raw.single.python
 has          : source.sage, string.quoted.raw.single.python
%(number)03d  : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.raw.single.python
 quote types. : source.sage, string.quoted.raw.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.raw.single.python
