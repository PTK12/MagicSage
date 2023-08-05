''' foo bar XXX baz '''

def foo():
    ''' foo FIXME baz '''



'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
 foo bar      : source.sage, string.quoted.docstring.multi.python
XXX           : keyword.codetag.notation.python, source.sage, string.quoted.docstring.multi.python
 baz          : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
 foo          : source.sage, string.quoted.docstring.multi.python
FIXME         : keyword.codetag.notation.python, source.sage, string.quoted.docstring.multi.python
 baz          : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
