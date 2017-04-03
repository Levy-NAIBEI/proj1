import unittest 

from LoanPayable import loan_Payable

class test(unittest.TestCase):
    def test_time(self):
        self.assertEqual(loan_payable(100000,14,0.12),112000, "Invalid")
        
