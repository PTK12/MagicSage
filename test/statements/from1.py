from ... import foo as bar
raise Exception('done') from exc
yield from foo




from          : keyword.control.import.python, source.sage
              : source.sage
...           : punctuation.separator.period.python, source.sage
              : source.sage
import        : keyword.control.import.python, source.sage
              : source.sage
foo           : source.sage
              : source.sage
as            : keyword.control.import.python, source.sage
              : source.sage
bar           : source.sage
raise         : keyword.control.flow.python, source.sage
              : source.sage
Exception     : meta.function-call.python, source.sage, support.type.exception.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
done          : meta.function-call.arguments.python, meta.function-call.python, source.sage, string.quoted.single.python
'             : meta.function-call.arguments.python, meta.function-call.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
from          : keyword.control.flow.python, source.sage
              : source.sage
exc           : source.sage
yield from    : keyword.control.flow.python, source.sage
              : source.sage
foo           : source.sage
