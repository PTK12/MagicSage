a = '''
{{ before detection }}
{# jinja comment #}
{{ after detection }}
'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.multi.python
{{            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.multi.python
 before detection  : source.sage, string.quoted.multi.python
}}            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.multi.python
{# jinja comment #} : source.sage, string.quoted.multi.python
{{ after detection }} : source.sage, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.multi.python
