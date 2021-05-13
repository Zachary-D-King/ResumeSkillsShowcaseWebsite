from MessageAdd import MessageAdd 
from collections import defaultdict
import math, string, random, functools, csv

messagesList = []

def main():

	absoluteInput = ""

	while absoluteInput != "quit": # Statement is used so when the user types 'quit' into console, it quits, otherwise, it runs.
		absoluteInput = str(input(">>> "))
		absoluteInput = absoluteInput.upper()

		# ----------- Print Out Elements Function ------------ # 
		def printOutElements():
			with open('Elements.csv', 'r') as csvfile: # https://www.youtube.com/watch?v=q5uM4VKywbA (source)
				filereader = csv.reader(csvfile)
				for elements in filereader:
					print('{:<15}  {:<15}  {:<20} {:<25} {:<30} {:<35} {:<40}'.format(*elements)) # https://stackoverflow.com/questions/39176935/formatting-output-of-csv-file-in-python (source)
		# ------------- Polyatomics List Function ------------- #
		def printOutPolyatomics():
			with open('Polyatomics.csv', 'r') as csvfile:
				filereader = csv.reader(csvfile)
				for polyatomics in filereader:
					print('{:<15}  {:<15}'.format(*polyatomics))

		# Equations (Backlog 2)
		def molarMass(): # https://stackoverflow.com/questions/16503560/read-specific-columns-from-a-csv-file-with-csv-module
			#massAnswer = 0.00
			#covAddElem = "" # declaring variable before being used in if statement 
			with open('MolarMasses.csv') as csvfile:
				reader = csv.reader(csvfile)# read rows into a dictionary format (defaultdict)
				reader = csv.reader(csvfile)
				molarMassList = list(reader)
				emptyMolarList = []
				i = 0
				molarMassInput = str(input("Input your elements. type 'done' when you are finished naming all your elements. (space to continue)"))
				while molarMassInput != "done":
					molarMassInput = str(input(">>> "))
					if molarMassInput in molarMassList:
						emptyMolarList.append(molarMassInput)
						i += 1
					print("Valid element. (", molarMassInput, " ) ( ", i, " ) elements found.")

		def hwManager():
			''' would include messageadd.py here, and other classes to manage homework. '''
			print("Welcome to the homework manager. Manage your homework here! Commands are 'add' - add homework..., 'remove' - remove homework..., 'edit' - edit homework... , 'homework' - see all homework..., 'quit' - leave the manager and go back to the main commands.... What would you like to do?")
			hwManagerInput = str(input(">>> "))
			while hwManagerInput != "done":
				if hwManagerInput == "add":
					addHomework = str(input("What homework assignment would you like to add?"))
					homeworkPost = MessageAdd(addHomework)
					messagesList.append(homeworkPost)

				elif hwManagerInput == "remove":
					removeRequest = int(input("What # of homework would you like to remove?"))
					if len(messagesList) > removeRequest:
						del messagesList[removeRequest]
					else:
						print("Error. Homework not found. Try again.")

				elif hwManagerInput == "edit":
					for homework in messagesList:
						print(homework)
				hwEdit = int(input("Which homework would you like to edit?"))-1
				if len(messagesList) > hwEdit:
					finalHomeworkEdit = str(input("What would you like to edit the homework to?"))
					messagesList[hwEdit]=MessageAdd(finalHomeworkEdit)

				elif hwManagerInput == "homework":
					for i in messagesList:
						print(i)

				elif hwManagerInput == "quit":
					break

				else:
					print("Unknown command. Try again.")

				print("Welcome to the homework manager. Manage your homework here! Commands are 'add' - add homework..., 'remove' - remove homework..., 'edit' - edit homework... , 'homework' - see all homework..., 'quit' - leave the manager and go back to the main commands.... What would you like to do?")
				hwManagerInput = str(input(">>> "))






		# ---------------- Commands -------------------- #
		if absoluteInput == "HELP":
			print(""" List of commands:
			"elements" - Print out all elements, and their chemical properties.
			"polyatomics" - Print out common polyatomics, and their chemical formulas.
			"molarmass" - Molar Mass Calculator. Just input the Element Names and Calculate!
			"molestograms" - Moles to grams calculator.
			"gramstomoles" - Grams to moles calculator.
			"joules" - joules & related variables calculator.
			"hwmanager" - homework manager program.

			"quit" - End the program
			""")
		elif absoluteInput == "HWMANAGER":
			hwManager()
		elif absoluteInput == "QUIT":
			exit()
		elif absoluteInput == "ELEMENTS":
			printOutElements()

		elif absoluteInput == "POLYATOMICS":
			printOutPolyatomics()

		elif absoluteInput == "MOLARMASS":
			molarMass()
			#http://www.softschools.com/formulas/chemistry/moles_to_grams_conversion_formula/111/


		#-------------------------------------------------------------------------------------------------------------------------------------------------------- BELOW THIS IS INCOMPLETE CODE. IT MAY OR MAY NOT WORK. --------------------------------------------------------------------------------------------------------------------------#

		elif absoluteInput == "MOLESTOGRAMS":
			mtogElementName = input("What is the element's symbol?\n")
			print()

			mtogNumOfMoles = int(input("Please enter the amount of moles of the element.*Do Not Include Units*\n"))
			print()

			mtogMolarMass = int(input("Please enter the molar mass of the element (In grams).*Do Not Include Units*\n"))
			print()

			mtogAnswer = int(mtogNumOfMoles*mtogMolarMass)

			print("The answer is:\n"+str(mtogAnswer)+ " g "+str(mtogElementName))
			#https://sciencing.com/calculate-amount-heat-released-8219426.html
			#http://www.softschools.com/formulas/physics/specific_heat_formula/61/
		elif absoluteInput == "GRAMSTOMOLES":
			gtomElementName = input("What is the element's symbol?\n")
			print()

			gtomNumberOfGrams = int(input("Please enter the amount of grams of the element.*Do Not Include Units*\n"))
			print()

			gtomMolarMass = int(input("Please enter the molar mass of the element (In grams).*Do Not Include Units*\n"))
			print()

			gtomAnswer = int(gtomNumberOfGrams/gtomMolarMass)

			print("The answer is:\n"+str(gtomAnswer)+ " mol "+str(gtomElementName))

			#Joules Calculator
			# https://www.omnicalculator.com/physics/specific-heat
			# https://sciencing.com/calculate-amount-heat-released-8219426.html
			# https://www.youtube.com/watch?v=a1AjBqElz7A
			# https://sciencing.com/equation-finding-initial-temperature-10056377.html
			#Equation: Q = mc(∆T)
			#Q = heat energy (Joules, J)
			#m = mass of a the substance (g)
			#c = specific heat (units J/kg*C)
			#∆T = change in temperature (Celcius, C)
			# Joules/specific heat/mass/final & initial temp calculator.
			# Takes input
		'''
		elif absoluteInput =="JOULES":
			print("Leave no more than one option blank please.")
			print()
			mVar = input("What is the mass, in g, of the substance?(Do Not type units.)\n *If unknown, just leave blank and hit enter.*")
			print()

			cVar = input("What is the specific heat, in Celcius, of the equation? (Do Not type units.)\n *If unknown, just leave blank and hit enter.*")
			print()

			qVar = input("What is the heat transferred, in Joules, of the equation(Do Not type units.)\n *If unknown, just leave blank and hit enter.*")
			print()

			tInitVar = input("What is the initial temp, in Celcius, of the equation?(Do Not type units.)\n *If unknown, just leave blank and hit enter.*")
			print()

			tFinVar = input("What is the final temp, in Celcius, of the equation?(Do Not type units.)\n *If unknown, just leave blank and hit enter.*")
			print()

			# Gives answer based on variable input.
			if mVar == "":
				mAnswer = (qVar/(cVar*(tFinVar - tInitVar)))
				print(str(mAnswer)+" g")

			elif cVar == "":
				cAnswer = (qVar/(mVar*(tFinVar - tInitVar)))
				print(str(cAnswer)+" J/kg*C")

			elif qVar == "":
				qAnswer = (mVar*cVar*(tFinVar-tInitVar))
				print(str(qAnswer)+" Joules")

			elif tFinAnswer == "":
				tFinAnswer = ((qVar/(mVar*cVar))- tInitVar)
				print(str(tFinAnswer)+" degrees C")

			elif tInitAnswer == "":
				tInitAnswer =((qVar/(mVar*cVar))-tFinVar)
				print(str(tInitAnswer)+"degrees C")
			else:
				print("Error. One or more variable were entered in incorrectly, or more than one variable was left blank.")

		elif absoluteInput == "STOICHGTM":
			gramsGivenSubGTM= input("What is the amount of grams of the substance given to you, in grams?(The amount of grams given to you in the problem)\n Do Not Type Units*\n")
			print()
			givenSubChemFormGTM= input("What is the chemical formula for the substance you put into the previous question?\n")
			print()
			givenSubMolesGTM= input("How many moles of "+str(givenSubChemForm)+" are there?\n Do Not Type Units*")
			print()
			givenSubMolarMassGTM= input("What is the molar mass of the substance you just put the chemical formula in on the previous question?(In grams)\n Do Not Type Units*\n")
			print()
			unknownSubChemFormGTM= input("What is the chemical formula for the substance you are trying to find the moles of?")
			print()
			unknownSubMolesGTM= input("How many moles of "+str(unknownSubChemForm)+" are there?\n Do Not Type Units*\n")
			print()

			stoichGTMAnswer= ((gramsGivenSubGTM*givenSubMolesGTM*unknownSubMolesGTM)/(givenSubMolarMassGTM*unknownSubMolesGTM))
			print(str(stoichGTMAnswer)+" moles of "+str(unknownSubChemFormGTM))




		# moles to grams
		elif absoluteInput == "STOICHMTG":
			givenSubMolesMTG = input("What is the amount of moles of the substance given to you, not the number of moles in the chemical equation?(The amount of moles given to you in the problem)\n Do Not Type Units*\n")  
			print()
			givenSubNumOfMoles = input("Now, what is the amount of moles for the this substance in the chemical equation?\n Do Not Type Units*\n")
			print()
			unknownSubMolarMassMTG = input("What is the molar mass of the substance you just put the chemical formula in on the previous question?(In grams)\n Do Not Type Units*\n")
			print()
			unknownSubChemFormMTG = input("What is the chemical formula for the substance you are trying to find the moles of?\n")
			print()
			unknownSubMolesMTG = input("How many moles of "+str(unknownSubChemForm)+" are there?\n Do Not Type Units*\n")
			print()

			stiochMTGAnswer = ((givenSubMolesMTG*unknownSubMolesMTG*unknownSubMolarMassMTG)/(givenSubNumOfMoles))
			print(str(stiochMTGAnswer)+" grams of "+str(unknownSubChemFormMTG))

'''
firstUserInput = str(input("Start program? (y/n)"))
firstUserInput = firstUserInput.upper()
if firstUserInput == "Y":
	print("Proceeding to the program.")
	absoluteInput = str(input("Welcome to the Chemistry Class Helper Program. For a list of commands, type 'help'. Press enter to continue.\n"))
	main() # The main() function is called if the user inputs yes into the console. (just making sure the user wants to actually run the program.)
else:
	print("Goodbye...")















'''


#We need to reference every element here, also we need to make the functions that will layout the program







#Backlog 3(Element Database) 
#***Do different page(in a class?)***:
#https://www.sigmaaldrich.#com/technical-documents/articles/biology/periodic-table-of-elements-names.html





#Backlog 4(Complex Equations):
#Basic Stoichiometry













#https://courses.lumenlearning.com/introchem/chapter/si-units-of-pressure/
#https://blog.beamex.com/pressure-units-and-pressure-unit-conversion
#google calculator that pops up when you search: "atm to pa"
#https://www.metric-conversions.org/pressure/pascals-to-atmospheres.html
#Units of Pressure
print("convert between: atm, pa, bar, and psi.\n*Type Units of pressure labels exactly as shown*")
print("atm")
print("pa")
print("bar")
uOPValueOne = input("What is the value for the first unit of pressure?*No Labels*")
uOPLabelOne = input("What is the label for the first unit of pressure value?*Label Only*")
uOPValueTwo = input("What is the value for the second unit of pressure?*No Labels*")
uOPLabelTwo= input("What is the label for the second unit of pressure value?*Label Only*")

if uOPLabelOne == atm and uOPLabelTwo == pa:

# atm:
# atm to Pa = 101325(atm)
# atm to bar = 1.01325(atm)
# atm to psi = 14.6959(atm)



# Pa =
# Pa to atm = 0.0000098692(Pa)
# Pa to bar = 0.000001(Pa)
# Pa to psi = 0.000145038(Pa)


# bar = 
# bar to Pa = 100000(bar)
# bar to atm = 0.986923(bar)
# bar to psi = 14.5038(bar)

'''




#Backlog 5(Polyatomic Ions List):





#Backlog 6 (Homework Manager):

