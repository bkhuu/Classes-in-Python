from project5 import *
import traceback
import subprocess

def checkEqual(shipments1,shipments2):
	ctr = 0
	if len(shipments1) != len(shipments2):
		return False
	while ctr < len(shipments1):
		shipment1 = shipments1[ctr]
		shipment2 = shipments2[ctr]
		if str(shipment1.getId()) != str(shipment2.getId()):
			return False
		if len(shipment1.getItems()) != len(shipment2.getItems()):
			return False
		i = 0
		while i < len(shipment1.getItems()):
			item1 = shipment1.getItems()[i]
			item2 = shipment2.getItems()[i]
			if str(item1) != str(item2):
				return False
			i = i + 1
		ctr = ctr + 1
		
	return True
		


def test1():
	item = Item('socks',12345,'$4.56')
	return str(item) == 'socks 12345 $4.56'
	
def test2():
	item = Item('socks',12345,'$4.56')
	return str(item.getName()) == 'socks'	
	
def test3():
	item = Item('socks',12345,'$4.56')
	return str(item.getId()) == '12345'		
	
def test4():
	item = Item('socks',12345,'$4.56')
	return str(item.getPrice()) == '$4.56'		
	
def test5():
	shipment = Shipment(55555555)
	return str(shipment) == '55555555: []'
	
def test6():
	shipment = Shipment(55555555)
	return str(shipment.getId()) == '55555555'	
	
def test7():
	shipment = Shipment(55555555)
	return shipment.getItems() == []		
	
def test8():
	item = Item('socks',12345,'$4.56')
	shipment = Shipment(55555555)
	shipment.addItem(item)
	return str(shipment) == '55555555: [socks 12345 $4.56]'	
	
def test9():
	item = Item('socks',12345,'$4.56')
	shipment = Shipment(55555555)
	shipment.addItem(item)
	item = Item('shirt',33333,'$14.78')
	shipment.addItem(item)		
	return str(shipment) == '55555555: [socks 12345 $4.56,shirt 33333 $14.78]'		
	
def test10():
	item = Item('socks',12345,'$4.56')
	shipment = Shipment(55555555)
	shipment.addItem(item)
	result = main(['55555555\n','socks 12345\n','$4.56\n'])
	
	return checkEqual([shipment],result)
	
def test11():
	shipments = []
	item = Item('socks',12345,'$4.56')
	shipment = Shipment(55555555)
	shipment.addItem(item)
	item = Item('shorts',33333,'$42.56')	
	shipment.addItem(item)
	shipments.append(shipment)

	result = main(['55555555\n','socks 12345\n','$4.56\n','shorts 33333\n','$42.56\n'])
	
	return checkEqual(shipments,result)	
	
def test12():
	shipments = []
	
	item = Item('socks',12345,'$4.56')
	shipment = Shipment(55555555)
	shipment.addItem(item)
	item = Item('shorts',33333,'$42.56')	
	shipment.addItem(item)
	shipments.append(shipment)
	
	item = Item('books',12345,'$4.56')
	shipment = Shipment(66678)
	shipment.addItem(item)
	item = Item('mirror',33333,'$42.56')	
	shipment.addItem(item)	
	item = Item('necklace',33333,'$42.56')	
	shipment.addItem(item)		
	shipments.append(shipment)	
	
	item = Item('shoes',12345,'$4.56')
	shipment = Shipment(1)
	shipment.addItem(item)
	item = Item('pencils',33333,'$42.56')	
	shipment.addItem(item)	
	item = Item('eraser',33333,'$42.56')	
	shipment.addItem(item)		
	shipments.append(shipment)

	result = main(['55555555\n','socks 12345\n','$4.56\n','shorts 33333\n','$42.56\n','66678\n','books 12345\n','$4.56\n','mirror 33333\n','$42.56\n'	,'necklace 33333\n','$42.56\n','1\n','shoes 12345\n','$4.56\n','pencils 33333\n','$42.56\n','eraser 33333\n','$42.56\n'])

	return checkEqual(shipments,result)	
	
def test13():
	shipments = []
	item = Item('socks',12345,'$4.56')
	shipment = Shipment(55555555)
	shipment.addItem(item)
	item = Item('socks',12345,'$4.56')	
	shipment.addItem(item)
	shipments.append(shipment)

	result = main(['55555555\n','socks 12345\n','$4.56\n','socks 12345\n','$4.56\n'])
	
	return checkEqual(shipments,result)	
	
def test14():
	result = False
	try:
		main(['55555555\n','socks12345\n','$4.56\n','socks 12345\n','$4.56\n'])
	except ItemException:
		result = True
	
	return result	
	
def test15():
	result = False
	try:
		main(['55555555\n','socks 12345\n','4.56\n','socks 12345\n','$4.56\n'])
	except ItemException:
		result = True
	
	return result	
	
def test16():
	result = False
	try:
		main(['55555555\n','socks 12345\n','$4.567\n','socks 12345\n','$4.56\n'])
	except ItemException:
		result = True
	
	return result		
	
def test17():
	result = False
	try:
		main(['55555555\n','socks 12345\n','$4.56\n','socks 12345\n','$-4.56\n'])
	except ItemException:
		result = True
	
	return result		
	
def test18():
	result = False
	try:
		main(['55555555\n','socks 12345\n','$4.56\n','socks 12345\n','$4.56.56\n'])
	except ItemException:
		result = True
	
	return result		
	
ctr = 1
failed = False
while ctr <= 18: 
	try:
		if eval("test"+str(ctr)+"()") == True:
			print "PASSED test"+str(ctr)+"!"
		else:
			print "Please check your code for test"+str(ctr)
			failed = True
	except Exception as e:
		traceback.print_exc()
		print "Please check your code for test"+str(ctr)+", it raised an undesired exception"
		failed = True
	ctr = ctr + 1
	
#if failed:
#	result = subprocess.check_output("curl -k	https://cs.gmu.edu/~kdobolyi/sparc/process.php?user=guest-project5-PROGRESS", shell=True)  
#else:
#	result = subprocess.check_output("curl -k	https://cs.gmu.edu/~kdobolyi/sparc/process.php?user=guest-project5-COMPLETED", shell=True)  

	
