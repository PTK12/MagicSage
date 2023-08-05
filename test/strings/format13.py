a = '''\n
{% for item in seq %}
    \n {{ item }} \n \N{BLACK SPADE SUIT}
{% endfor %}
'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.multi.python
\n            : constant.character.escape.python, source.sage, string.quoted.multi.python
{% for item in seq %} : source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
\n            : constant.character.escape.python, source.sage, string.quoted.multi.python
 {{ item }}   : source.sage, string.quoted.multi.python
\n            : constant.character.escape.python, source.sage, string.quoted.multi.python
              : source.sage, string.quoted.multi.python
\N{BLACK SPADE SUIT} : constant.character.escape.python, source.sage, string.quoted.multi.python
{% endfor %}  : source.sage, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.multi.python
