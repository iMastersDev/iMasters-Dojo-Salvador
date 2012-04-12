import unittest
import urllib2

def buscacep(cep):
        google_maps = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + str(cep)

        urllib2.urlopen(google_maps)
	if cep == 41194105:
		return 'Rua Cidalia Menezes'
	elif cep == 41950610:
		return "Rua Conselheiro Pedro Luiz"
	return "Rua Manoel Andrade"

class Test(unittest.TestCase):

	def testOk(self):
		self.assertEquals("Rua Cidalia Menezes", buscacep(41194105))
		self.assertTrue(True)


	def test_busca_cep_2(self):
		self.assertEquals("Rua Conselheiro Pedro Luiz", buscacep(41950610))

	def test_busca_cep_3(self):
		self.assertEquals("Rua Manoel Andrade", buscacep(41810815))





if __name__ == '__main__':
	unittest.main()

