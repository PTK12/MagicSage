def foo():
    '''>>> print("""docstring""")'''
def foo():
    """>>> print('''docstring''')"""



def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
>>>           : keyword.control.flow.python, source.sage, string.quoted.docstring.multi.python
print("""docstring""") : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
>>>           : keyword.control.flow.python, source.sage, string.quoted.docstring.multi.python
print('''docstring''') : source.sage, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
