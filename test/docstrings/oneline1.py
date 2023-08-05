'''>>> print("""docstring""")'''
async
""">>> print('''docstring''')"""
await
"""\n>>> print('''docstring''')"""
await
"""   >>> print('''docstring''')"""
await
""" 1  >>> print('''docstring''')"""
await



'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
>>>           : keyword.control.flow.python, source.sage, string.quoted.docstring.multi.python
print("""docstring""") : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
async         : keyword.control.flow.python, source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
>>>           : keyword.control.flow.python, source.sage, string.quoted.docstring.multi.python
print('''docstring''') : source.sage, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
await         : keyword.control.flow.python, source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
\n            : constant.character.escape.python, source.sage, string.quoted.docstring.multi.python
>>> print('''docstring''') : source.sage, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
await         : keyword.control.flow.python, source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
              : source.sage, string.quoted.docstring.multi.python
>>>           : keyword.control.flow.python, source.sage, string.quoted.docstring.multi.python
print('''docstring''') : source.sage, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
await         : keyword.control.flow.python, source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
 1  >>> print('''docstring''') : source.sage, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
await         : keyword.control.flow.python, source.sage
