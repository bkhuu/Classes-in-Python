class Item:
	def __init__(self,name,id,price):
		self.name = name
		self.id = id
		self.price = price
	def getName(self):
		return self.name
	def getId(self):
		return self.id
	def getPrice(self):
		return self.price
	def __str__(self):
		return str(self.name) + " " + str(self.id) + " " + str(self.price)

class Shipment:
	def __init__(self,id):
		self.id = id
		self.items = []
	def getId(self):
		return self.id
	def getItems(self):
		return self.items
	def addItem(self,Item):
		self.items.append(Item)
	def __str__(self):
		result = str(self.id) + ": ["
		ctr = 0
		while ctr < len(self.items):
			if ctr == (len(self.items) - 1):
				result = result + str(self.items[ctr])
			else:
				result = result + str(self.items[ctr]) + ","
			ctr = ctr + 1
		result = result + "]"
		return result
		
class ItemException(Exception):
	def __init__(self, message):
		Exception.__init__(self)
		self.message = message
		self.items = []
	def __str__(self):
		return self.message

#Main
def main(list):
	shipments = []
	ctr = 0
	while ctr < len(list):
		string = ""
		i = 0
		while i < len(list[ctr]) - 1:
			string = string + str(list[ctr][i])
			i = i + 1
		if string.isdigit() == True:
			shipment = Shipment(int(string))
			ctr = ctr + 1
		else:
			sub = ctr
			while sub <= ctr + 1:
				string = ""
				i = 0
				while i < len(list[sub]) - 1:
					string = string + str(list[sub][i])
					i = i + 1
				if sub == ctr:
					if string[len(string) - 6] != " ":
						raise ItemException("Missing Space!")
					string2 = ""
					i = len(string) - 5
					while i < len(string):
						string2 = string2 + str(list[sub][i])	
						i = i + 1
					string3 = ""
					i = 0
					while i < len(string) - 6:
						string3 = string3 + str(list[sub][i])	
						i = i + 1
				if sub == ctr + 1:
					if string[0] != "$":
						raise ItemException("Invalid Price!")				
					if string[1] == "-":
						raise ItemException("Invalid Price!")
					if string[len(string) - 3] != ".":
						raise ItemException("Invalid Price!")
					try:
						int(string[len(string) - 1])
						int(string[len(string) - 2])
					except:
						raise ItemException("Invalid Price!")
					test = 0
					result = 0
					while test < len(string):
						if string[test] == ".":
							result = result + 1
						test = test + 1
					if result > 1 or result < 1:
						raise ItemException("Invalid Price!")
					item = Item(string3,int(string2),string)
					shipment.addItem(item)
				sub = sub + 1
				if sub == len(list):
					shipments.append(shipment)
				elif sub < len(list):
					string = ""
					i = 0
					while i < len(list[sub]) - 1:
						string = string + str(list[sub][i])
						i = i + 1
					if string.isdigit() == True:
						shipments.append(shipment)
			ctr = ctr + 2

	return shipments
				














