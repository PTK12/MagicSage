.PHONY: all ci-test test release devenv publish

all: devenv release

ci-test: release
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/MagicPython.syntax.yaml
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml

# 	Check if the version specified in "package.json" matches the latest git tag
	@if [ \
		`cat package.json | grep -e '^[[:space:]]*"version":' | sed -e 's/[[:space:]]*"version":[[:space:]]*"\(.*\)",/\1/'` \
		!= \
		`git describe --tags --abbrev=0 | sed -e 's/v\([[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\).*/\1/'` \
	] ; \
		then echo "Error: package.version != git.tag" && exit 1 ; fi

update-test:
#	Run tests and overwrite the output
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/MagicPython.syntax.yaml --overwrite-tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml --overwrite-tests

test: ci-test
	atom -t test/atom-spec

devenv:
	npm install --dev

release:
	mkdir release

	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicPython.syntax.yaml --out ./release/MagicPython.tmLanguage
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicRegExp.syntax.yaml --out ./release/MagicRegExp.tmLanguage

	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicPython.syntax.yaml --out ./release/MagicPython.cson
	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicRegExp.syntax.yaml --out ./release/MagicRegExp.cson

	./node_modules/.bin/syntaxdev scopes --syntax grammars/src/MagicPython.syntax.yaml > misc/scopes

	./node_modules/.bin/syntaxdev atom-spec --package-name MagicPython --tests test/**/*.py --syntax grammars/src/MagicPython.syntax.yaml --out test/atom-spec/python-spec.js
	./node_modules/.bin/syntaxdev atom-spec --package-name MagicPython --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml --out test/atom-spec/python-re-spec.js

publish: test
	apm publish patch
	rm -rf ./node_modules/syntaxdev
	vsce publish

new-all: devenv new-release

new-release: release
	node ./script.js ./release/MagicPython.tmLanguage > ./release/MagicPython.tmLanguage.json
	node ./script.js ./release/MagicRegExp.tmLanguage > ./release/MagicRegExp.tmLanguage.json
