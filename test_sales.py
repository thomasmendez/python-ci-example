import unittest
# to pass input as if it was from command line use @patch decorator
# The patch function temporarily replaces the target object with a different object during the test
from unittest.mock import patch

from item import Item

from sales import imp, impLine, extractItem

class TestSales(unittest.TestCase):

    # input1
    input1 = ['1 book at 12.49', '1 music CD at 14.99', '1 chocolate bar at 0.85']

    # The side_effect argument can accept a function to be called when the mock
    # is called, an iterable or an Exception

    @patch('builtins.input', side_effect=input1)
    def testImpPatch(self, imp):

        calling_1 = imp()
        calling_2 = imp()
        calling_3 = imp()
        self.assertTrue(calling_1 == '1 book at 12.49' and calling_2 == '1 music CD at 14.99' and
                        calling_3 == '1 chocolate bar at 0.85')
    
    @patch('builtins.input', side_effect=[15, '1 book at 12.49'])
    def testImpLine(self, mock_inputs):
        result = impLine()
        item = Item(1, False, 12.49)
        self.assertIsInstance(result, Item)
        self.assertEqual(result.quantity, item.quantity)
        self.assertEqual(result.imported, item.imported)
        self.assertEqual(result.cost, item.cost)

    
    def testExtractItem(self):
        line = '1 music CD at 14.99'
        result = extractItem(line)
        item = Item(1, False, 14.99)
        self.assertIsInstance(result, Item)
        self.assertEqual(result.quantity, item.quantity)
        self.assertEqual(result.imported, item.imported)
        self.assertEqual(result.cost, item.cost)
    
    def testExtractItemInput(self):
        line1 = 'music CD at 14.99'
        line2 = '14.99 music CD at 1'
        self.assertRaises(ValueError, extractItem, line1)
        self.assertRaises(ValueError, extractItem, line2)