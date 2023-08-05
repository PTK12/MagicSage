# testing comments in function definition
def foo(    # before args
    a=42,   # between
            # args
    b=      # in args
      24,
    d       # before '='
     =99,
    e
    )       # incomplete definition, missing COLON, you're probably typing it
    # pre docstring
    '''Docstring'''
    # post docstring

def bar(): return 1




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 testing comments in function definition : comment.line.number-sign.python, source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
foo           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 before args  : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
a             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
42            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 between      : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 args         : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
b             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 in args      : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
24            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
d             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
              : meta.function.parameters.python, meta.function.python, source.sage
#             : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, punctuation.definition.comment.python, source.sage
 before '='   : comment.line.number-sign.python, meta.function.parameters.python, meta.function.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
=             : keyword.operator.python, meta.function.parameters.python, meta.function.python, source.sage
99            : constant.numeric.dec.python, meta.function.parameters.python, meta.function.python, source.sage
,             : meta.function.parameters.python, meta.function.python, punctuation.separator.parameters.python, source.sage
              : meta.function.parameters.python, meta.function.python, source.sage
e             : meta.function.parameters.python, meta.function.python, source.sage, variable.parameter.function.language.python
              : meta.function.parameters.python, meta.function.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
              : meta.function.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 incomplete definition, missing COLON, you're probably typing it : comment.line.number-sign.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 pre docstring : comment.line.number-sign.python, source.sage
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
Docstring     : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 post docstring : comment.line.number-sign.python, source.sage
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
bar           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
return        : keyword.control.flow.python, source.sage
              : source.sage
1             : constant.numeric.dec.python, source.sage
