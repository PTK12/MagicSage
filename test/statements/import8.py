try:
    import \
                    time as ham, \
                    datetime \
            # XXX: comment at the end of import
except Exception as exc:
    pass




try           : keyword.control.flow.python, source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
import        : keyword.control.import.python, source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
                     : source.sage
time          : source.sage
              : source.sage
as            : keyword.control.import.python, source.sage
              : source.sage
ham           : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
                     : source.sage
datetime      : source.sage
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
              : comment.line.number-sign.python, source.sage
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.sage
: comment at the end of import : comment.line.number-sign.python, source.sage
except        : keyword.control.flow.python, source.sage
              : source.sage
Exception     : source.sage, support.type.exception.python
              : source.sage
as            : keyword.control.flow.python, source.sage
              : source.sage
exc           : source.sage
:             : punctuation.separator.colon.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
