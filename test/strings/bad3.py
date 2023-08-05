a = r"bad string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

def foo(a=1): pass # doesn't break!



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.single.python
"             : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.single.python
bad string    : source.sage, string.regexp.quoted.single.python
              : invalid.illegal.newline.python, source.sage, string.regexp.quoted.single.python
foo           : source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005" : invalid.illegal.line.continuation.python, source.sage
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
1             : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 doesn't break! : comment.line.number-sign.python, source.sage
