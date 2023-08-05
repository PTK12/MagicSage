def foo():
    '>>> print("docstring")'
def foo():
    ">>> print('docstring')"



def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
>>> print("docstring") : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
>>> print('docstring') : source.sage, string.quoted.docstring.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
