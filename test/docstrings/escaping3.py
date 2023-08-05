r'''Module docstring

    (?x)                # not a regexp
        foo[20]{42}     # not a comment
'''



r             : source.sage, storage.type.string.python, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.raw.multi.python
Module docstring : source.sage, string.quoted.docstring.raw.multi.python
              : source.sage, string.quoted.docstring.raw.multi.python
    (?x)                # not a regexp : source.sage, string.quoted.docstring.raw.multi.python
        foo[20]{42}     # not a comment : source.sage, string.quoted.docstring.raw.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.raw.multi.python
