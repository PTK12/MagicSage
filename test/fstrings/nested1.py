f'''
    prefix {
        foo(f"""
            inner prefix
            { bar["q"] + f'insane{42 + 9000}stuff{def aaa(): pass}111'}
            inner suffix
        """)
    } suffix
'''




f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
    prefix    : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
              : meta.fstring.python, source.sage
foo           : meta.fstring.python, meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.multi.python
            inner prefix : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.multi.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
bar           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.indexed-name.python, meta.item-access.python, source.sage
[             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.begin.python, source.sage
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
q             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, source.sage, string.quoted.single.python
"             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.arguments.python, meta.item-access.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
]             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, meta.item-access.python, punctuation.definition.arguments.end.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
+             : keyword.operator.arithmetic.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
f             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
insane        : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
42            : constant.numeric.dec.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
+             : keyword.operator.arithmetic.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
9000          : constant.numeric.dec.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
stuff         : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
def           : keyword.control.flow.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
aaa           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.generic.python, meta.function-call.python, source.sage
(             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.colon.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
pass          : keyword.control.flow.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
111           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
}             : constant.character.format.placeholder.other.python, meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.multi.python
            inner suffix : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.multi.python
              : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, source.sage, string.interpolated.python, string.quoted.multi.python
"""           : meta.fstring.python, meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.multi.python
)             : meta.fstring.python, meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
 suffix       : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.multi.python
'''           : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.multi.python
