' foo bar XXX baz '

def foo():
    ' foo FIXME baz '



'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
 foo bar      : source.sage, string.quoted.docstring.single.python
XXX           : keyword.codetag.notation.python, source.sage, string.quoted.docstring.single.python
 baz          : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
 foo          : source.sage, string.quoted.docstring.single.python
FIXME         : keyword.codetag.notation.python, source.sage, string.quoted.docstring.single.python
 baz          : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
