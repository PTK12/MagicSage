@dec
# Bar.name=... is not legal, but the test is for highlighter not breaking badly
class Spam(Foo.Bar, Bar.name={'very': 'odd'}):
    pass




@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
dec           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 Bar.name=... is not legal, but the test is for highlighter not breaking badly : comment.line.number-sign.python, source.sage
class         : meta.class.python, source.sage, storage.type.class.python
              : meta.class.python, source.sage
Spam          : entity.name.type.class.python, meta.class.python, source.sage
(             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.begin.python, source.sage
Foo           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.sage
.             : meta.class.inheritance.python, meta.class.python, meta.member.access.python, punctuation.separator.period.python, source.sage
Bar           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, meta.member.access.python, source.sage
,             : meta.class.inheritance.python, meta.class.python, punctuation.separator.inheritance.python, source.sage
              : meta.class.inheritance.python, meta.class.python, source.sage
Bar           : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, source.sage
.             : meta.class.inheritance.python, meta.class.python, meta.member.access.python, punctuation.separator.period.python, source.sage
name          : entity.other.inherited-class.python, meta.class.inheritance.python, meta.class.python, meta.member.access.python, source.sage
=             : keyword.operator.assignment.python, meta.class.inheritance.python, meta.class.python, source.sage
{             : meta.class.inheritance.python, meta.class.python, punctuation.definition.dict.begin.python, source.sage
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
very          : meta.class.inheritance.python, meta.class.python, source.sage, string.quoted.single.python
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
:             : meta.class.inheritance.python, meta.class.python, punctuation.separator.dict.python, source.sage
              : meta.class.inheritance.python, meta.class.python, source.sage
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.begin.python, source.sage, string.quoted.single.python
odd           : meta.class.inheritance.python, meta.class.python, source.sage, string.quoted.single.python
'             : meta.class.inheritance.python, meta.class.python, punctuation.definition.string.end.python, source.sage, string.quoted.single.python
}             : meta.class.inheritance.python, meta.class.python, punctuation.definition.dict.end.python, source.sage
)             : meta.class.inheritance.python, meta.class.python, punctuation.definition.inheritance.end.python, source.sage
:             : meta.class.python, punctuation.section.class.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
