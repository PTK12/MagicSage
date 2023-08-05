# issue 150
record = {
    "a": {k: str(v) for k, v in foo if ""}
}




#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 issue 150    : comment.line.number-sign.python, source.sage
record        : source.sage
              : source.sage
=             : keyword.operator.assignment.python, source.sage
              : source.sage
{             : punctuation.definition.dict.begin.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
a             : source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
:             : punctuation.separator.dict.python, source.sage
              : source.sage
{             : punctuation.definition.dict.begin.python, source.sage
k             : source.sage
:             : punctuation.separator.dict.python, source.sage
              : source.sage
str           : meta.function-call.python, source.sage, support.type.python
(             : meta.function-call.python, punctuation.definition.arguments.begin.python, source.sage
v             : meta.function-call.arguments.python, meta.function-call.python, source.sage
)             : meta.function-call.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
for           : keyword.control.flow.python, source.sage
              : source.sage
k             : source.sage
,             : punctuation.separator.element.python, source.sage
              : source.sage
v             : source.sage
              : source.sage
in            : keyword.control.flow.python, source.sage
              : source.sage
foo           : source.sage
              : source.sage
if            : keyword.control.flow.python, source.sage
              : source.sage
"             : punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
"             : punctuation.definition.string.end.python, source.sage, string.quoted.single.python
}             : punctuation.definition.dict.end.python, source.sage
}             : punctuation.definition.dict.end.python, source.sage
