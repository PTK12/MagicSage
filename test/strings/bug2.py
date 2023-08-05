# issue 150
cmd = "git-clang-format --style=\"{{BasedOnStyle: Google, ColumnLimit: 100, IndentWidth: 2, " \
 "AlignConsecutiveAssignments: true}}\" {COMMIT_SHA} -- ./**/*.proto > {OUTPUT}".format(




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 issue 150    : comment.line.number-sign.python, source.sage
cmd           : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
git-clang-format --style= : source.sage, string.quoted.single.python
\"            : constant.character.escape.python, source.sage, string.quoted.single.python
{{            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
BasedOnStyle: Google, ColumnLimit: 100, IndentWidth: 2,  : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
              : source.sage
\             : punctuation.separator.continuation.line.python, source.sage
              : source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
AlignConsecutiveAssignments: true : source.sage, string.quoted.single.python
}}            : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
\"            : constant.character.escape.python, source.sage, string.quoted.single.python
              : source.sage, string.quoted.single.python
{COMMIT_SHA}  : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
 -- ./**/*.proto >  : source.sage, string.quoted.single.python
{OUTPUT}      : constant.character.format.placeholder.other.python, meta.format.brace.python, source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
.             : meta.member.access.python, punctuation.separator.period.python, source.sage
format        : meta.function-call.generic.python, meta.function-call.python, meta.member.access.python, source.sage
(             : meta.function-call.python, meta.member.access.python, punctuation.definition.arguments.begin.python, source.sage
