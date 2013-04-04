
import random

class Dice:
	def roll(self):
		return random.randint(1, 6) 


class Attack:
	def roll(self, i_):
		res = []
		d = Dice()
		for i in range (0, i_):
			res.append(d.roll())
		return res

class Defence:
	def roll(self, i_):
		res = []
		d = Dice()
		for i in range(0, i_):
			res.append(d.roll())

		return res
		
class Battle:

	def calc(self, numa_, numb_, nuclear = False):
		a = Attack()
		d = Defence()

		attackdice = a.roll(numa_)
		defencedice = d.roll(numb_)

#		print "Attack", attackdice
#		print "Defense", defencedice

		return self.comp(attackdice, defencedice, nuclear)

		

	def comp(self, at_, df_, nuclear_):
		if nuclear_ == False:
			print "Attack Rolls: ", sorted(at_, reverse=True)
			print "Defence Rolls:", sorted(df_, reverse=True) 
		

		at = sorted(at_, reverse=True)
		df = sorted(df_, reverse=True)

		atwins = 0
		dfwins = 0
		
		#Check first order dice
		if at[0] > df[0]:
			atwins += 1
		else:
			dfwins += 1

		# Check second dice
		if len(at) > 1 and len(df) > 1:
			if at[1] > df[1]:
				atwins += 1
			else:
				dfwins += 1

		return [atwins, dfwins]


class War:

	def __init__(self):
		self.warcries = [
		"CHARGE!!!!",
		"MOVE OUT!!!",
		"LOCK N LOAD BITCHES",
		"I CAME HERE TO KICK ASS AND CHEW BUBBLE GUM AND IM ALL OUT OF GUM",
		"ITS A GOOD DAY TO DIE",
		"DIE MAGGOTS",
		"YIPEEKIYAY MOTHERFUCKER",
		"ITS NOT A TUMOR",
		"EAT SHIT AND DIE",
		"GO AHEAD, MAKE MY DAY",
		"YOU FEELIN LUCKY... PUNK",
		"GET TO THE CHOPPAAAA",
		]

	def nuclear(self):
		self.go(True)

	def go(self, nuclear = False):

		print ""
		print ""
		print "WAR"
		print ""	
		numat = int(raw_input("Number Attack Units:"))
		numdf = int(raw_input("Number Defence Units:"))

		while True:

			if nuclear == False:
				print ""
				print self.warcries[random.randint(0, len(self.warcries)-1)]

			b = Battle()
			
			numattackdice = 0
			numdefencedice = 0
	
			#Work out how many dice
			if numat > 3:
				numattackdice = 3
			elif numat == 3:
				numattackdice = 2
			elif numat == 2:
				numattackdice = 1

			if numdf >= 2:
				numdefencedice = 2
			elif numdf == 1:
				numdefencedice = 1

			res = b.calc(numattackdice, numdefencedice, nuclear)
			
			numat -= res[1]
			numdf -= res[0]
			
                        print "Remaining attack units: ", numat
                        print "Remaining defence units:", numdf
                        print ""
			
			if numdf == 0:
				print "Successfully invaded - move " + str(numattackdice) + " units to invaded country"
				break
	
			if numat == 1:
				print "Defense holds strong"
				break 
			
			if nuclear == False:
				if raw_input("Continue Attack?").lower() != "y":
					break
		
def main():

	print "*************************"
	print "*"
	print "*   RISK WAR MACHINE"
	print "*"
	print "*************************"

	while True:

		print "Main Menu:"
		print ""
		print "1. War"
		print "2. Nuclear war"
		print "3. Simple"
		print "q. Quit"

		sel = raw_input(":")
		if sel == "1":
			w = War()
			w.go()
		if sel == "2":
			w = War()
			w.nuclear()
		if sel == "3":
			pass
		if sel.lower() == "q":
			print "BYE"
			break
				

if __name__ == "__main__":
	main()
