def foo():
    '''TE\'''ST'''

def foo():
    r'''TE\'''ST'''

def foo():
    R'''TE\'''ST'''

def foo():
    u'''TEST'''

def foo():
    U'''TEST'''

def foo():
    b'''TEST'''

def foo():
    B'''TEST'''



def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
TE            : source.sage, string.quoted.docstring.multi.python
\'            : constant.character.escape.python, source.sage, string.quoted.docstring.multi.python
''ST          : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.multi.python
TE            : source.sage, string.quoted.docstring.raw.multi.python
\'            : source.sage, string.quoted.docstring.raw.multi.python
''ST          : source.sage, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.multi.python
TE            : source.sage, string.quoted.docstring.raw.multi.python
\'            : source.sage, string.quoted.docstring.raw.multi.python
''ST          : source.sage, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
u             : source.sage, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.multi.python
TEST          : source.sage, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
U             : source.sage, storage.type.string.python, string.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.multi.python
TEST          : source.sage, string.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
b             : source.sage, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.multi.python
TEST          : source.sage, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.binary.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
B             : source.sage, storage.type.string.python, string.quoted.binary.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.multi.python
TEST          : source.sage, string.quoted.binary.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.binary.multi.python
