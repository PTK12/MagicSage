'TEST'

class Foo:
    # comment
    R'TEST'

    def foo(self, a:'TEST') -> 'TEST': #ok
        r'TEST'
        with bar:
            pass

    def bar(self, a:'TEST') -> 'TEST': pass
        'TEST' # additional docstring
        with bar:
            pass



'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
TEST          : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
class         : meta.class.python, source.sage, storage.type.class.python
              : meta.class.python, source.sage
Foo           : entity.name.type.class.python, meta.class.python, source.sage
:             : meta.class.python, punctuation.section.class.begin.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 comment      : comment.line.number-sign.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.single.python
TEST          : source.sage, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.single.python
              : source.sage
              : meta.function.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
self          : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python, variable.parameter.function.language.special.self.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.sage
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
TEST          : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
              : meta.function.python, source.sage
->            : meta.function.python, punctuation.separator.annotation.result.python, source.sage
              : meta.function.python, source.sage
'             : meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
TEST          : meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
ok            : comment.line.number-sign.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.single.python
TEST          : source.sage, string.quoted.docstring.raw.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.single.python
              : source.sage
with          : keyword.control.flow.python, source.sage
              : source.sage
bar           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
              : source.sage
              : meta.function.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
bar           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
self          : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python, variable.parameter.function.language.special.self.python
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
:             : meta.function.parameters.python, meta.function.python, punctuation.separator.annotation.python, source.sage
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
TEST          : meta.function.parameters.python, meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.parameters.python, meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
              : meta.function.python, source.sage
->            : meta.function.python, punctuation.separator.annotation.result.python, source.sage
              : meta.function.python, source.sage
'             : meta.function.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
TEST          : meta.function.python, source.sage, string.quoted.single.python
'             : meta.function.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
TEST          : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 additional docstring : comment.line.number-sign.python, source.sage
              : source.sage
with          : keyword.control.flow.python, source.sage
              : source.sage
bar           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
