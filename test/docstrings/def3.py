def foo():
    'TE\'ST'

def foo():
    r'TE\'ST'

def foo():
    R'TE\'ST'

def foo():
    u'TEST'

def foo():
    U'TEST'

def foo():
    b'TEST'

def foo():
    B'TEST'



def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
TE            : source.sage, string.quoted.docstring.single.python
\'            : constant.character.escape.python, source.sage, string.quoted.docstring.single.python
ST            : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.single.python
TE            : source.sage, string.quoted.docstring.raw.single.python
\'            : source.sage, string.quoted.docstring.raw.single.python
ST            : source.sage, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.single.python
TE            : source.sage, string.quoted.docstring.raw.single.python
\'            : source.sage, string.quoted.docstring.raw.single.python
ST            : source.sage, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
u             : source.sage, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
TEST          : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
U             : source.sage, storage.type.string.python, string.quoted.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
TEST          : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
b             : source.sage, storage.type.string.python, string.quoted.binary.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.single.python
TEST          : source.sage, string.quoted.binary.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.binary.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
B             : source.sage, storage.type.string.python, string.quoted.binary.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.single.python
TEST          : source.sage, string.quoted.binary.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.binary.single.python
