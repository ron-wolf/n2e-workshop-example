import sys

if len(sys.argv > 0):
	name = sys.argv[0]
	print("Hello, ", name)
	print("Goodbye, ", name)
else:
	print("Hello, world!")
	print("Goodbye, world!")
