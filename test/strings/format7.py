# XXX we have to highlight '% o' here, as it is a valid python
# format spec. Otherwise, it would be hard to spot an error in
# the code below.
a = '12% of %s' % ('name',)



#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
              : comment.line.number-sign.python, source.sage
XXX           : comment.line.number-sign.python, keyword.codetag.notation.python, source.sage
 we have to highlight '% o' here, as it is a valid python : comment.line.number-sign.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 format spec. Otherwise, it would be hard to spot an error in : comment.line.number-sign.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 the code below. : comment.line.number-sign.python, source.sage
a             : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
12            : source.sage, string.quoted.single.python
% o           : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
f             : source.sage, string.quoted.single.python
%s            : constant.character.format.placeholder.other.python, meta.format.percent.python, source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
%             : keyword.operator.arithmetic.python, source.sage
              : source.sage
(             : punctuation.parenthesis.begin.python, source.sage
'             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
name          : source.sage, string.quoted.single.python
'             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
,             : punctuation.separator.element.python, source.sage
)             : punctuation.parenthesis.end.python, source.sage
