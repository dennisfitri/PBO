import Buku as b
import Novel as n
import Majalah as m
import Buku_pelajaran as p

if __name__ == "__main__":
	nvl = n.Novel()
	nvl.inputDataNovel()
	nvl.dispDataNovel()

	mjl = m.Majalah()
	mjl.inputDataMajalah()
	mjl.dispDataMajalah()

	plj = p.BukuPelajaran()
	plj.inputDataPelajaran()
	plj.dispDataPelajaran()

	bk = b.Buku()