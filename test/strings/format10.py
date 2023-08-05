a = '''blah {foo-bar %d
       blah {foo-bar %d}
       blah {foo-bar %d //insane {}}
       {}blah {foo-bar %d //insane {}}'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.multi.python
blah {foo-bar  : source.sage, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.multi.python
       blah   : source.sage, string.quoted.multi.python
{foo-bar      : source.sage, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.multi.python
}             : source.sage, string.quoted.multi.python
       blah {foo-bar  : source.sage, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.multi.python
 //insane {}} : source.sage, string.quoted.multi.python
       {}blah {foo-bar  : source.sage, string.quoted.multi.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.multi.python
 //insane {}} : source.sage, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.multi.python
