class MyQueue:
	def __init__(self):
		self.stack_in = []
		self.stack_out = []

	def push(self, x:int) -> None:
		self.stack_in.append(x)

	def pop(self) -> int:
		if self.empty():
			return None
		
		if self.stack_out:
			return self.stack_out.pop()
		else:
			for i in range(len(self.stack_in)):
				self.stack_out.append(self.stack_in.pop())
			return self.stack_out.pop()
	
		

