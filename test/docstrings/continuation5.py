'implicit ' "concatenation"

'''implicit
''' 'concatenation'

'''implicit
''' """
concatenation
"""

'implicit' '''
concatenation
'''



'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
implicit      : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
concatenation : source.sage, string.quoted.docstring.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
implicit      : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
concatenation : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
implicit      : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
              : source.sage
"""           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
concatenation : source.sage, string.quoted.docstring.multi.python
"""           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.single.python
implicit      : source.sage, string.quoted.docstring.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.single.python
              : source.sage
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.docstring.multi.python
concatenation : source.sage, string.quoted.docstring.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.docstring.multi.python
