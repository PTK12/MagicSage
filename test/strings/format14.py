a = R'''\n
{% for item in seq %}
    \n {{ item }} \n \N{BLACK SPADE SUIT}
{% endfor %}
'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
\n            : source.sage, string.quoted.raw.multi.python
{% for item in seq %} : source.sage, string.quoted.raw.multi.python
    \n {{ item }} \n \N{BLACK SPADE SUIT} : source.sage, string.quoted.raw.multi.python
{% endfor %}  : source.sage, string.quoted.raw.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.raw.multi.python
