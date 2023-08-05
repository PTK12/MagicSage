if isinstance(t1, TypeVar): # type: ignore
    continue



if            : keyword.control.flow.python, source.sage
              : source.sage
isinstance    : meta.function-call.python, source.sage, support.function.builtin.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
t1            : meta.function-call.arguments.python, meta.function-call.python, source.sage
,             : meta.function-call.arguments.python, meta.function-call.python, punctuation.separator.arguments.python, source.sage
              : meta.function-call.arguments.python, meta.function-call.python, source.sage
TypeVar       : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, meta.typehint.comment.python, source.sage
type:         : comment.line.number-sign.python, comment.typehint.directive.notation.python, meta.typehint.comment.python, source.sage
              : comment.line.number-sign.python, meta.typehint.comment.python, source.sage
ignore        : comment.line.number-sign.python, comment.typehint.ignore.notation.python, meta.typehint.comment.python, source.sage
              : source.sage
continue      : keyword.control.flow.python, source.sage
