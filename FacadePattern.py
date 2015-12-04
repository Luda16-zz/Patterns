class Scanner: 
	def __init__(self):
		self.name = "Scanner"

class Parser:
	def __init__(self):
		self.name = "Parser"
	
class Compiler: 
	def __init__(self):
		self.name    = "Compiler"
		self.Scanner = Scanner()
		self.parser  = Parser()

	def compile(self):
		print("Compiling...")
		print("Scanning %s" % self.scanner.name)
		print("Parsing %s" % self.parser.name)

if __name__ == "__main__":
	compiler = Compiler()
	compiler.compile()