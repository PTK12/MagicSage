from.foo import d
from.import a

foo.import

raise Exception from Foo

def bar():
    yield from baz




from          : keyword.control.import.python, source.sage
.             : punctuation.separator.period.python, source.sage
foo           : source.sage
              : source.sage
import        : keyword.control.import.python, source.sage
              : source.sage
d             : source.sage
from          : keyword.control.import.python, source.sage
.             : punctuation.separator.period.python, source.sage
import        : keyword.control.import.python, source.sage
              : source.sage
a             : source.sage
              : source.sage
foo           : source.sage
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
import        : keyword.control.import.python, meta.member.access.python, source.sage
              : source.sage
raise         : keyword.control.flow.python, source.sage
              : source.sage
Exception     : source.sage, support.type.exception.python
              : source.sage
from          : keyword.control.flow.python, source.sage
              : source.sage
Foo           : source.sage
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
bar           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
yield from    : keyword.control.flow.python, source.sage
              : source.sage
baz           : source.sage
