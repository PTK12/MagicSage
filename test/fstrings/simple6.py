f'insane{42 + 9000}stuff{def aaa(): pass}'
# def aaa() must not be parsed as a valid declaration




f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
insane        : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
42            : constant.numeric.dec.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
+             : keyword.operator.arithmetic.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
9000          : constant.numeric.dec.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
stuff         : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
def           : keyword.control.flow.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
aaa           : meta.fstring.python, meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : meta.fstring.python, punctuation.separator.colon.python, source.sage
              : meta.fstring.python, source.sage
pass          : keyword.control.flow.python, meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
'             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 def aaa() must not be parsed as a valid declaration : comment.line.number-sign.python, source.sage
