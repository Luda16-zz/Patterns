from abc import ABCMeta 
 
class Command(metaclass=ABCMeta): 
	def execute(self):
		pass

class Light:
	#Reciever class
	def turnOn(self):
		print("Foco encendido")


	def turnOff(self):
		print("Foco apagado")

class Switch:
	#Invoker class
	def __init__(self, onCommand, offCommand):
		self._onCommand = onCommand
		self._offCommand = offCommand


	def on(self):
		self._onCommand.execute();

	def off(self):
		self._offCommand.execute();

class onCommand(Command):
	def __init__(self, light):
		self._light = light

	def execute(self):
		self._light.turnOn()
		

class offCommand(Command):
	def __init__(self, light):
		self._light = light

	def execute(self):
		self._light.turnOff()


class LightSwitch:
	#Client Class
	def __init__(self):
		self._foco = Light()
		self._switchUp 		= onCommand(self._foco)
		self._switchDown 	= offCommand(self._foco)
		self._switch 		= Switch(self._switchUp, self._switchDown)

	def operation(self, cmd):
		if cmd == "ON":
			self._switch.on()
		elif cmd == "OFF":
			self._switch.off()
		else:
			print("Operacion invalida")

if __name__ == "__main__":
	client = LightSwitch()
	print("Testing On operation")
	client.operation("ON")
	print("Testing off command")
	client.operation("OFF")
