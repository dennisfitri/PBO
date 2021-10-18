import Tabung as t
import Balok as ba
import Bola as bo

if __name__ == '__main__':
	print("="*10, "TABUNG", "="*10)
	tabung1 = t.Tabung()
	tabung1.volume()
	tabung1.dispTabung()

	print("="*10, "BALOK", "="*10)
	balok1 = ba.Balok()
	balok1.volume()
	balok1.dispBalok()

	print("="*10, "BOLA", "="*10)
	bola1 = bo.Bola()
	bola1.volume()
	

