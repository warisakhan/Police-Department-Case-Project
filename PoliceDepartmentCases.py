##I received no asistance on this assignment that violates the ethical guidelines set forth by the professor and the class syllabus 

class Detective():
	#storing parameters for the functions
	def __init__(self, name, cases, solved_cases):
		#initializing all of the variables 
			
		self.name = name
		self.cases = cases
		self.solved_cases = solved_cases

		#using for loop to count the number of total cases 
		num_cases = 0
		for element in self.cases:
			num_cases += 1 
		self.num_cases = num_cases

		# using for loop to count number of solved cases 
		num_solved = 0 
		for element in self.solved_cases:
			num_solved += 1 
		self.num_solved = num_solved

		#raising DATA error 
		if num_solved > num_cases:
			msg = "Solved cases cannot be more than total cases!"
			raise DataError(msg)


			


		# do i return the values?

	def __str__(self):
		#concatenating all of the variables to return the string
		#is the error happening here because I am returning here?

		return ("Detective " + str(self.name) + ": total cases " + str(self.num_cases) + ", solved " + str(self.num_solved) + ", failed " + str(self.num_cases - self.num_solved) + ".")
		#how do i call the failed cases function? do i just call the return value or the function itself?


	def num_failed_cases(self):
		#subtracting solved cases from total cases to get the failed cases
		num_failed_cases = self.num_cases - self.num_solved
		return num_failed_cases

	def add_new_cases(self, new_cases, new_solved):
#raising Data Error 
		if len(new_solved) > len(new_cases):
			msg = "New solved cases cannot be more than new cases!"
			raise DataError(msg)
		#updating the cases with all of the new cases
		for element in new_cases:
			self.cases.append(element)
			self.num_cases += 1


		#using range function to match the solved cases to the correct case names 
		#updating the number of solved cases 
		for i in range(len(new_cases)):
			for j in range(len(new_solved)):
				if (i + 1) == new_solved[j]:
					self.solved_cases.append(new_cases[i])
					self.num_solved += 1
		#DATA error exception

	def failed_cases(self):
		#creating new list to add all failed cases 
		update = []
		#checking to see if the case is in solved cases 
		for element in self.cases:
			if element not in self.solved_cases:
				update.append(element)
		return update 




class DataError(Exception):

	def __init__(self, msg):
		#initializing variable 
		self.msg = msg

	def __str__(self):
		#returning string 
		return self.msg




