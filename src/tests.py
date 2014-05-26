"""
tests.py
Nitaino

Prueba que cosas funcionen.

"""

import unittest

# cosas que vamos a probar
import ipadd

class TestIpAddress(unittest.TestCase):
    """
    Codigo que prueba el ipadd.py
    """
    
    def test_genera_i_procesa(self):
        """
        Asegura que la generacion de IP's funcione
        """
        # tiran lo mismo so solo tenemos que probar una funcion
        self.assertEqual(ipadd.genera_ips('0.0.0.0'), ipadd.procesa_ip(libnitaino.printea, '0.0.0.0'))
        self.assertEqual(ipadd.genera_ips('0-1.0-1.0-1.0-1'), ipadd.procesa_ip(libnitaino.printea, '0-1.0-1.0-1.0-1'))
        self.assertEqual(ipadd.genera_ips('0-10-2.0.0.0'), ipadd.procesa_ip(libnitaino.printea, '0-10-2.0.0.0'))
        
        # some ugly and wrongly formatted input
        # malformed ip
        self.assertRaises(ValueError, ipadd.genera_ips, '0')
        self.assertRaises(ValueError, ipadd.genera_ips, '')
        self.assertRaises(AttributeError, ipadd.genera_ips, 1)
        self.assertRaises(ValueError, ipadd.genera_ips, '0.0.0.')
        self.assertRaises(ValueError, ipadd.genera_ips, '0.0-.0.0')
        self.assertRaises(ValueError, ipadd.genera_ips, '0.-0')
        
        # too many seperations
        self.assertRaises(ValueError, ipadd.genera_ips, '0.0.0.0.0')
        # too few
        self.assertRaises(ValueError, ipadd.genera_ips, '0.0.0.0.0')

        

if __name__ == '__main__':
    unittest.main()
    
