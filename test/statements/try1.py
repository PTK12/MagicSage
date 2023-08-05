try:
    1/0
except AbcError as ex:
    pass
except (ZeroDivisionError, GhiError) as ex:
    print(ex)
else:
    1
finally:
    2



try           : keyword.control.flow.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
1             : constant.numeric.dec.python, source.sage
/             : keyword.operator.arithmetic.python, source.sage
0             : constant.numeric.dec.python, source.sage
except        : keyword.control.flow.python, source.sage
              : source.sage
AbcError      : source.sage
              : source.sage
as            : keyword.control.flow.python, source.sage
              : source.sage
ex            : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
except        : keyword.control.flow.python, source.sage
              : source.sage
(             : punctuation.parenthesis.begin.python, source.sage
ZeroDivisionError : source.sage, support.type.exception.python
,             : punctuation.separator.element.python, source.sage
              : source.sage
GhiError      : source.sage
)             : punctuation.parenthesis.end.python, source.sage
              : source.sage
as            : keyword.control.flow.python, source.sage
              : source.sage
ex            : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
print         : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
ex            : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
else          : keyword.control.flow.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
1             : constant.numeric.dec.python, source.sage
finally       : keyword.control.flow.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
2             : constant.numeric.dec.python, source.sage
