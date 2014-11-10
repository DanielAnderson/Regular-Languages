Regular-Languages
=================

This program can check membership in a given regular language

Developers
==========
How to import project files from other files:
	It depends on how you run the script. If you run the script by running the command "python <name of file>", then you can
	only import from the same directory, by typing from <name of file> import <class/function to import>
	While this is useful for hand testing, to get the file to work overall, the import must be from reference to main.py
	So if you want to import the class fooBar from the file FooBar.py, in the directory Regular Languages/foo/bar/fooBar.py
	you would type "from foo.bar.FooBar import FooBar" 
	For examples, go to testNFA.py 

To run tests:
	run python3 -m unittest discover
	This will run all tests, defined as (I believe) any methods which start with the name test in a class that inherits from unittest.TestCase
