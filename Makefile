.PHONY: all ci-test test devenv release

all: devenv release

ci-test:
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/MagicSage.syntax.yaml
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml

update-test:
#	Run tests and overwrite the output
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/MagicSage.syntax.yaml --overwrite-tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml --overwrite-tests

test: ci-test

devenv:
	npm install --dev

release:
	mkdir -p release

	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicSage.syntax.yaml --out ./release/MagicSage.tmLanguage
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicRegExp.syntax.yaml --out ./release/MagicRegExp.tmLanguage

	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicSage.syntax.yaml --out ./release/MagicSage.cson
	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicRegExp.syntax.yaml --out ./release/MagicRegExp.cson

	node ./script.js ./release/MagicSage.tmLanguage > ./release/MagicSage.tmLanguage.json
	node ./script.js ./release/MagicRegExp.tmLanguage > ./release/MagicRegExp.tmLanguage.json

	./node_modules/.bin/syntaxdev scopes --syntax grammars/src/MagicSage.syntax.yaml > misc/scopes

	./node_modules/.bin/syntaxdev atom-spec --package-name MagicSage --tests test/**/*.py --syntax grammars/src/MagicSage.syntax.yaml --out test/atom-spec/python-spec.js
	./node_modules/.bin/syntaxdev atom-spec --package-name MagicSage --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml --out test/atom-spec/python-re-spec.js
