a = b"bad \\ string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

def foo(a=1): pass




a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
b             : source.sage, storage.type.string.python, string.quoted.binary.single.python
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.binary.single.python
bad           : source.sage, string.quoted.binary.single.python
\\            : constant.character.escape.python, source.sage, string.quoted.binary.single.python
 string       : source.sage, string.quoted.binary.single.python
              : invalid.illegal.newline.python, source.sage, string.quoted.binary.single.python
foo           : source.sage
              : source.sage
\             : keyword.operator.arithmetic.python, source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\"            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\a            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\b            : constant.character.escape.python, source.sage, string.quoted.single.python
 \c           : source.sage, string.quoted.single.python
\f            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\n            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\r            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\t            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\v            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\5            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\55           : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\555          : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\05           : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
\005          : constant.character.escape.python, source.sage, string.quoted.single.python
"             : source.sage, string.quoted.single.python
              : invalid.illegal.newline.python, source.sage, string.quoted.single.python
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
