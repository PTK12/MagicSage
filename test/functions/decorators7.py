# this is testing trailing whitespace after the decorator
# DO NOT DELETE TRAILING WHITESTAPCE IN THIS FILE
@foo    
@foo()    
@bar	
@bar()	
@bar() illegal # legal
@bar():   
def baz(): pass





#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 this is testing trailing whitespace after the decorator : comment.line.number-sign.python, source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 DO NOT DELETE TRAILING WHITESTAPCE IN THIS FILE : comment.line.number-sign.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
              : meta.function.decorator.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
foo           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
              : source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
	             : meta.function.decorator.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
	             : source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
 illegal      : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
              : source.sage
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.sage
 legal        : comment.line.number-sign.python, source.sage
@             : entity.name.function.decorator.python, meta.function.decorator.python, punctuation.definition.decorator.python, source.sage
bar           : entity.name.function.decorator.python, meta.function.decorator.python, source.sage
(             : meta.function.decorator.python, punctuation.definition.arguments.begin.python, source.sage
)             : meta.function.decorator.python, punctuation.definition.arguments.end.python, source.sage
:             : invalid.illegal.decorator.python, meta.function.decorator.python, source.sage
              : source.sage
def           : meta.function.python, source.sage, storage.type.function.python
              : meta.function.python, source.sage
baz           : entity.name.function.python, meta.function.python, source.sage
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.sage
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.sage
:             : meta.function.python, punctuation.section.function.begin.python, source.sage
              : source.sage
pass          : keyword.control.flow.python, source.sage
