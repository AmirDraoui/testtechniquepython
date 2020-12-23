import unittest
from sol_2 import main
from sol_1 import sort



class Test(unittest.TestCase):

    def test_ex1(self):
        self.assertEqual([1,2,3,4,5,6],sort([3,2,5,1,6,4]))


    def test_ex2(self):
        section_item_att = ['order', 'type', 'reference', 'level', 'description']
        non_section_item_att = ['unity', 'quantity']
        cell_item_att = ['order', 'type', 'description', 'unity', 'quantity']
        non_cell_item_att = ['reference', 'level']
        output = main()
        self.assertEqual(['items'],list(output.keys()))
        items = output['items']
        for i in range(len(items)):
            self.assertEqual(i,items[i]['order'])
            if items[i]['type'] == 'CELL':
                for att in cell_item_att :
                    self.assertIn(att,items[i].keys())
                for att in non_cell_item_att :
                    self.assertNotIn(att,items[i].keys())

            if items[i]['type'] == 'SECTION':
                for att in section_item_att :
                    self.assertIn(att,items[i].keys())
                for att in non_section_item_att :
                    self.assertNotIn(att,items[i].keys())
                self.assertEqual(1,items[i]['level'])



if __name__ == '__main__':
    unittest.main()