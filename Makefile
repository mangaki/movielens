all:
	pandoc -s -t beamer gcc.md -o gcc.pdf
	evince gcc.pdf
