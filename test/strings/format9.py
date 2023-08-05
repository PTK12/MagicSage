a = 'blah {foo-bar %d'
a = 'blah {foo-bar %d}'
a = 'blah {foo-bar %d //insane {}}'
a = '{}blah {foo-bar %d //insane {}}'



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
blah {foo-bar  : source.sage, string.quoted.single.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
blah          : source.sage, string.quoted.single.python
{foo-bar      : source.sage, string.quoted.single.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
}             : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
blah          : source.sage, string.quoted.single.python
{foo-bar      : source.sage, string.quoted.single.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
 //insane {}} : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
{}            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
blah          : source.sage, string.quoted.single.python
{foo-bar      : source.sage, string.quoted.single.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
 //insane {}} : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
