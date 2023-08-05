match 'prefix' + foo:
    ... # cases
match "prefix" + foo:
    ... # cases
match f'prefix{foo}':
    ... # cases
match f"prefix{foo}":
    ... # cases
match -foo:
    ... # cases
match not foo:
    ... # cases




match         : keyword.control.flow.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
prefix        : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
+             : keyword.operator.arithmetic.python, source.sage
              : source.sage
foo           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
prefix        : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
+             : keyword.operator.arithmetic.python, source.sage
              : source.sage
foo           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
'             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
prefix        : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
foo           : meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
'             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
f             : meta.fstring.python, source.sage, storage.type.string.python, string.interpolated.python, string.quoted.single.python
"             : meta.fstring.python, punctuation.definition.string.begin.python, source.sage, string.interpolated.python, string.quoted.single.python
prefix        : meta.fstring.python, source.sage, string.interpolated.python, string.quoted.single.python
{             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
foo           : meta.fstring.python, source.sage
}             : constant.character.format.placeholder.other.python, meta.fstring.python, source.sage
"             : meta.fstring.python, punctuation.definition.string.end.python, source.sage, string.interpolated.python, string.quoted.single.python
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
-             : keyword.operator.arithmetic.python, source.sage
foo           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage
match         : keyword.control.flow.python, source.sage
              : source.sage
not           : keyword.operator.logical.python, source.sage
              : source.sage
foo           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
...           : constant.other.ellipsis.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 cases        : comment.line.number-sign.python, source.sage