import pylint

options = ['--disable=unnecessary-lambda, missing-function-docstring', 'exam.py']
pylint.run_pylint(argv=options)

