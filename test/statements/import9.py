from . . . foo import \
    (
        # XXX: legal comment inside import
        time as bar,
        # another comment
        baz,
        datetime as ham
    )
raise Exception('!') from None




from          : keyword.control.import.python, source.sage
              : source.sage
.             : punctuation.separator.period.python, source.sage
              : source.sage
.             : punctuation.separator.period.python, source.sage
              : source.sage
.             : punctuation.separator.period.python, source.sage
              : source.sage
foo           : source.sage
              : source.sage
import        : keyword.control.import.python, source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
              : source.sage
(             : punctuation.parenthesis.begin.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
              : comment.line.number-sign.python, source.sage
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.sage
: legal comment inside import : comment.line.number-sign.python, source.sage
              : source.sage
time          : source.sage
              : source.sage
as            : keyword.control.import.python, source.sage
              : source.sage
bar           : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 another comment : comment.line.number-sign.python, source.sage
              : source.sage
baz           : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
datetime      : source.sage
              : source.sage
as            : keyword.control.import.python, source.sage
              : source.sage
ham           : source.sage
              : source.sage
)             : punctuation.parenthesis.end.python, source.sage
raise         : keyword.control.flow.python, source.sage
              : source.sage
Exception     : meta.function-call.python, source.sage, support.type.exception.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
!             : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
from          : keyword.control.flow.python, source.sage
              : source.sage
None          : constant.language.python, source.sage
