import Person as p
class Customer (p.Person):
	def inputDataCustomer(self) :
		p.Person.inputData(self)
		self.idCustomer = str(input("ID Customer :"))
		self.point = int(input("Point :"))
		self.totalPembelian = int(input("Total pembelian :"))

	def tampilDataCustomer(self) :
		print("-"*40)
		p.Person.tampilData(self) 
		print ("ID Customer 	:", self.idCustomer)
		print ("Point 		:", self.point)
		print ("Total pembelian :", self.totalPembelian)

	def tambahPoin(self):
		penambahan_point = self.totalPembelian / 100
		print ("Penambahan point:", penambahan_point)
		print("Point saat ini 	:", penambahan_point + self.point)
		print ()

