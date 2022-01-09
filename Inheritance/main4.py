import Employee as e
import Customer as c
import Person as p

if __name__ == "__main__":
	print ("Employee")
	employee1 = e.Employee()
	employee1.inputDataEmployee()
	employee1.tampilDataEmployee()
	employee1.hitungMasaKerja()

	print ("Customer")
	customer1 = c.Customer()
	customer1.inputDataCustomer()
	customer1.tampilDataCustomer()
	customer1.tambahPoin()

	person1 = p.Person()