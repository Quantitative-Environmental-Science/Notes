.PHONY: html live pdf pdflatex

html:
	jupyter-book build book

# Live-reloading preview at http://127.0.0.1:8000
# Notebooks use the execution cache, so only edited notebooks are re-run.
live:
	jupyter-book config sphinx book
	sphinx-autobuild book book/_build/live \
		--open-browser \
		--ignore "*/_build/*" \
		--ignore "*/conf.py" \
		--ignore "*/.ipynb_checkpoints/*" \
		-D nb_execution_mode=cache

pdf:
	jupyter-book build book --builder pdfhtml

pdflatex:
	jupyter-book build book --builder pdflatex