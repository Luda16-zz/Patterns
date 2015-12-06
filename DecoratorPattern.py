from abc import ABCMeta 
 
class Shape(metaclass=ABCMeta): 
	def draw(self):
		pass

class Circle(Shape):
	def draw(self):
		print("Im a circle")

class Rectangle(Shape):
	def draw(self):
		print("Im a Rectangle")

class ShapeDecorator(Shape):
	def __init__(self, decoratedShape):
		self.decoratedShape = decoratedShape

	def draw(self):
		self.decoratedShape.draw()
		self.doSomethingElse()

	def doSomethingElse(self):
		pass

class ColorRedShapeDecorator(ShapeDecorator):
	def draw(self):
		self.decoratedShape.draw()
		self.doSomethingElse()
	
	def doSomethingElse(self):
		print("Coloring red")

if __name__ == "__main__":
	circle = Circle()
	redCircle = ColorRedShapeDecorator(Circle())


	circle.draw()
	print("########")
	redCircle.draw()
		
