import unittest
import dice

class TestDiceMethods(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(dice.parse("1d4"), ("1d4", 1, 4, 0))
        self.assertEqual(dice.parse("1d6"), ("1d6", 1, 6, 0))
        self.assertEqual(dice.parse("1d8"), ("1d8", 1, 8, 0))
        self.assertEqual(dice.parse("1d10"), ("1d10", 1, 10, 0))
        self.assertEqual(dice.parse("1d12"), ("1d12", 1, 12, 0))
        self.assertEqual(dice.parse("1d20"), ("1d20", 1, 20, 0))
        self.assertEqual(dice.parse("1d100"), ("1d100", 1, 100, 0))
        
        self.assertEqual(dice.parse("1d4+1"), ("1d4+1", 1, 4, 1))
        self.assertEqual(dice.parse("1d6+1"), ("1d6+1", 1, 6, 1))
        self.assertEqual(dice.parse("1d8+1"), ("1d8+1", 1, 8, 1))
        self.assertEqual(dice.parse("1d10+1"), ("1d10+1", 1, 10, 1))
        self.assertEqual(dice.parse("1d12+1"), ("1d12+1", 1, 12, 1))
        self.assertEqual(dice.parse("1d20+1"), ("1d20+1", 1, 20, 1))
        self.assertEqual(dice.parse("1d100+1"), ("1d100+1", 1, 100, 1))

        self.assertEqual(dice.parse("1d6+5"), ("1d6+5", 1, 6, 5))
        self.assertEqual(dice.parse("1d6+10"), ("1d6+10", 1, 6, 10))
        self.assertEqual(dice.parse("1d6+100"), ("1d6+100", 1, 6, 100))
        self.assertEqual(dice.parse("1d6+1000"), ("1d6+1000", 1, 6, 1000))
        
        self.assertEqual(dice.parse("1d6 1d4"), ())
        self.assertEqual(dice.parse("1d3"), ())
        self.assertEqual(dice.parse("1d60"), ())
        self.assertEqual(dice.parse("1d65"), ())
        self.assertEqual(dice.parse("1d69"), ())
        self.assertEqual(dice.parse("1d80"), ())
        self.assertEqual(dice.parse("1d1000"), ())
        self.assertEqual(dice.parse("1d1001"), ())
        self.assertEqual(dice.parse("1d1001"), ())
        self.assertEqual(dice.parse("1d6d10"), ())
        self.assertEqual(dice.parse("10d4d12"), ())
        self.assertEqual(dice.parse("d4"), ())
        self.assertEqual(dice.parse("1d6+5d"), ())
        self.assertEqual(dice.parse("1d6+10d"), ())
        self.assertEqual(dice.parse("1d6+100d"), ())
        self.assertEqual(dice.parse("1d6+1000d"), ())

    def test_avg(self):
        #1dN cases
        self.assertEqual(dice.calc_avg(1,4,0), 2.5)
        self.assertEqual(dice.calc_avg(1,6,0), 3.5)
        self.assertEqual(dice.calc_avg(1,8,0), 4.5)
        self.assertEqual(dice.calc_avg(1,10,0), 5.5)
        self.assertEqual(dice.calc_avg(1,12,0), 6.5)
        self.assertEqual(dice.calc_avg(1,20,0), 10.5)
        self.assertEqual(dice.calc_avg(1,100,0), 50.5)

        #2dN cases
        self.assertEqual(dice.calc_avg(2,4,0), 5.0)
        self.assertEqual(dice.calc_avg(2,6,0), 7.0)
        self.assertEqual(dice.calc_avg(2,8,0), 9.0)
        self.assertEqual(dice.calc_avg(2,10,0), 11.0)
        self.assertEqual(dice.calc_avg(2,12,0), 13.0)
        self.assertEqual(dice.calc_avg(2,20,0), 21.0)
        self.assertEqual(dice.calc_avg(2,100,0), 101.0)

        #10dN cases
        self.assertEqual(dice.calc_avg(10,4,0), 25.0)
        self.assertEqual(dice.calc_avg(10,6,0), 35.0)
        self.assertEqual(dice.calc_avg(10,8,0), 45.0)
        self.assertEqual(dice.calc_avg(10,10,0), 55.0)
        self.assertEqual(dice.calc_avg(10,12,0), 65.0)
        self.assertEqual(dice.calc_avg(10,20,0), 105.0)
        self.assertEqual(dice.calc_avg(10,100,0), 505.0)

    def test_avg_mod(self):
        self.assertEqual(dice.calc_avg(1,6,1),4.5)
        self.assertEqual(dice.calc_avg(5,6,1),18.5)
        self.assertEqual(dice.calc_avg(10,6,1),36)
        self.assertEqual(dice.calc_avg(1,6,10),13.5)
        self.assertEqual(dice.calc_avg(5,6,10),27.5)
        self.assertEqual(dice.calc_avg(10,6,10),45.0)

    def test_min(self):
        self.assertEqual(dice.calc_min(1,0), 1)
        self.assertEqual(dice.calc_min(2,0), 2)
        self.assertEqual(dice.calc_min(3,0), 3)
        self.assertEqual(dice.calc_min(5,0), 5)
        self.assertEqual(dice.calc_min(10,0), 10)

    def test_min_mod(self):
        self.assertEqual(dice.calc_min(1,1), 2)
        self.assertEqual(dice.calc_min(2,1), 3)
        self.assertEqual(dice.calc_min(3,1), 4)
        self.assertEqual(dice.calc_min(5,1), 6)
        self.assertEqual(dice.calc_min(10,1), 11)
        
        self.assertEqual(dice.calc_min(1,10), 11)
        self.assertEqual(dice.calc_min(2,10), 12)
        self.assertEqual(dice.calc_min(3,10), 13)
        self.assertEqual(dice.calc_min(5,10), 15)
        self.assertEqual(dice.calc_min(10,10), 20)

    def test_max(self):
        #1dN cases
        self.assertEqual(dice.calc_max(1,4,0), 4)
        self.assertEqual(dice.calc_max(1,6,0), 6)
        self.assertEqual(dice.calc_max(1,8,0), 8)
        self.assertEqual(dice.calc_max(1,10,0), 10)
        self.assertEqual(dice.calc_max(1,12,0), 12)
        self.assertEqual(dice.calc_max(1,20,0), 20)
        self.assertEqual(dice.calc_max(1,100,0), 100)

        #2dN cases
        self.assertEqual(dice.calc_max(2,4,0), 8.0)
        self.assertEqual(dice.calc_max(2,6,0), 12.0)
        self.assertEqual(dice.calc_max(2,8,0), 16.0)
        self.assertEqual(dice.calc_max(2,10,0), 20.0)
        self.assertEqual(dice.calc_max(2,12,0), 24.0)
        self.assertEqual(dice.calc_max(2,20,0), 40.0)
        self.assertEqual(dice.calc_max(2,100,0), 200.0)

        #10dN cases
        self.assertEqual(dice.calc_max(10,4,0), 40.0)
        self.assertEqual(dice.calc_max(10,6,0), 60.0)
        self.assertEqual(dice.calc_max(10,8,0), 80.0)
        self.assertEqual(dice.calc_max(10,10,0), 100.0)
        self.assertEqual(dice.calc_max(10,12,0), 120.0)
        self.assertEqual(dice.calc_max(10,20,0), 200.0)
        self.assertEqual(dice.calc_max(10,100,0), 1000.0)

    def test_max_mod(self):
        self.assertEqual(dice.calc_max(1,6,1),7)
        self.assertEqual(dice.calc_max(5,6,1),31)
        self.assertEqual(dice.calc_max(10,6,1),61)
        self.assertEqual(dice.calc_max(1,6,10),16)
        self.assertEqual(dice.calc_max(5,6,10),40)
        self.assertEqual(dice.calc_max(10,6,10),70)

if __name__ == '__main__':
    unittest.main()

