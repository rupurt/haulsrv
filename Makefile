all: deps.install format.check test

setup: deps.install

deps.install: deps.install.pyproject
deps.install.pyproject: deps.install.pyproject/global deps.install.pyproject/test
deps.install.pyproject/global:
	./scripts/deps/install_pyproject
deps.install.pyproject/test:
	./scripts/deps/install_pyproject test
deps.install.requirements: deps.install.requirements/global deps.install.requirements/test
deps.install.requirements/global:
	./scripts/deps/install_requirements
deps.install.requirements/test:
	./scripts/deps/install_requirements test
deps.freeze/global:
	./scripts/deps/freeze
deps.freeze/test:
	./scripts/deps/freeze test
deps.compile: deps.compile/global deps.compile/test
deps.compile/global:
	./scripts/deps/compile
deps.compile/test:
	./scripts/deps/compile test
deps.clean:
	./scripts/deps/clean
deps.purge:
	./scripts/deps/purge

format/run:
	./scripts/format/run
format/check:
	./scripts/format/check

test: test.lint test.typecheck test.run
test.lint:
	ruff check .
test.typecheck:
	pyright
test.run:
	pytest -vv --no-header src
test.coverage:
	pytest --cov src

ifeq ($(findstring build,$(firstword $(MAKECMDGOALS))),build)
  BUILD_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(BUILD_ARGS):;@:)
endif
build: build.nuitka
build.nuitka:
	@./scripts/build/nuitka $(BUILD_ARGS)
build.clean:
	./scripts/build/clean $(BUILD_ARGS)

ifeq ($(findstring run.,$(firstword $(MAKECMDGOALS))),run.)
  RUN_ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(RUN_ARGS):;@:)
endif
run:
	@python src/haulsrv $(RUN_ARGS)

clean: deps.clean build.clean

compose.build:
	./scripts/compose/build
compose.up:
	./scripts/compose/up
compose.down:
	./scripts/compose/down

pypi: pypi/build pypi/publish
pypi/build:
	./scripts/pypi/build
pypi/publish:
	./scripts/pypi/publish
