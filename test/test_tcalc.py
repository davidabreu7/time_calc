import unittest

from lib.timecalc import *


class TestTimeCalc(unittest.TestCase):

    def test_calc_date(self):
        self.assertEqual(calc_date([datetime.strptime("28/04/1993", "%d/%m/%Y"), datetime.strptime("10/04/1984", "%d/%m/%Y")]), "8 years 12 months 18 days")
        self.assertEqual(calc_date([datetime.strptime("10/04/1984", "%d/%m/%Y"), datetime.strptime("28/04/1993", "%d/%m/%Y")]), "8 years 12 months 18 days")
        self.assertEqual(calc_date([datetime.strptime("10/04/1984", "%d/%m/%Y")]), "37 years 07 months 25 days")

