a = R'''\fr{still_ok}ac{m_{j \rightarrow i}(\mathrm{good})}
        {not_ok} %d
'''



a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
R             : source.sage, storage.type.string.python, string.quoted.raw.multi.python
'''           : punctuation.definition.string.begin.python, source.sage, string.quoted.raw.multi.python
\fr           : source.sage, string.quoted.raw.multi.python
{still_ok}    : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.raw.multi.python
ac            : source.sage, string.quoted.raw.multi.python
{m_{j \rightarrow i}(\mathrm{good})} : source.sage, string.quoted.raw.multi.python
        {not_ok}  : source.sage, string.quoted.raw.multi.python
%d            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.raw.multi.python
'''           : punctuation.definition.string.end.python, source.sage, string.quoted.raw.multi.python
