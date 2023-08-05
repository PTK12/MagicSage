a = r'''
    (?x)
        foo
'''
a = br'''
    (?x)
        foo
'''
a = rb'''
    (?x)
        foo
'''
a = Br'''
    (?x)
        foo
'''
a = rB'''
    (?x)
        foo
'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
r             : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
(?x)          : source.sage, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
br            : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
(?x)          : source.sage, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
rb            : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
(?x)          : source.sage, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
Br            : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
(?x)          : source.sage, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
rB            : source.sage, storage.type.string.python, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.regexp.quoted.multi.python
              : source.sage, string.regexp.quoted.multi.python
(?x)          : source.sage, storage.modifier.flag.regexp, string.regexp.quoted.multi.python
        foo   : source.sage, string.regexp.quoted.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.regexp.quoted.multi.python
