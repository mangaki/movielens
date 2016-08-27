all:
	pandoc -s -t beamer gcc.md -o gcc.pdf
	open gcc.pdf