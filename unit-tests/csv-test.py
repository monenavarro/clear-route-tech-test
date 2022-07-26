import os
import csv
import unittest

test_file = 'stage-1/latest-customers-converted.csv'
rows = [
    ['name', 'age', 'address', 'phone', 'email'],
    ['Kirestin Delaney', '22', '464-7197 Ultricies Ave', '0800 326358', 'orci.lobortis@icloud.org'],
]


class TestCsv(unittest.TestCase):

  def test_read_line(self):
      with open(test_file, 'r') as csv_file:
          reader = csv.reader(csv_file)
          self.assertEqual(next(reader), rows[0])
          self.assertEqual(next(reader), rows[1])



if __name__ == "__main__":
    unittest.main()