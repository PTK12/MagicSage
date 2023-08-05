def foo(status):
    match status:
        case 404:
            return "Not found"
        case 401 | 403:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"




def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
status        : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
status        : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
404           : constant.numeric.dec.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
return        : keyword.control.flow.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
Not found     : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
401           : constant.numeric.dec.python, source.sage
              : source.sage
|             : keyword.operator.bitwise.python, source.sage
              : source.sage
403           : constant.numeric.dec.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
return        : keyword.control.flow.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
Not allowed   : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
case          : keyword.control.flow.python, source.sage
              : source.sage
_             : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
return        : keyword.control.flow.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
Something's wrong with the internet : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
