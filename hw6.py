import re
import unittest

def sumNums(fileName):

    file = open(fileName)
    lines = file.readlines()
    file.close()

    sum = 0

    for line in lines:
        line.rstrip()

        l= re.findall('[0-9]+', line)

        for k in l:
            sum += int(k)

    return sum


def countWord(fileName, word):

    file = open(fileName)
    lines = file.readlines()
    file.close()

    count = 0

    for line in lines:
        l = re.findall(word + '\\b', line, re.IGNORECASE)

        count += len(l)

    return count



def listURLs(fileName):

    file = open(fileName)
    lines = file.readlines()
    file.close()

    lst = []
    for line in lines:
        line.rstrip()

        l = re.findall('www.[a-z A-z 0-9 ]+.[a-z A-Z]{3}\S*', line)

        for i in l:
            lst.append(i)

    return lst

class TestHW6(unittest.TestCase):
    """ Class to test this homework """

    def test_sumNums1(self):
        """ test sumNums on the first file """
        self.assertEqual(sumNums("regex_sum_42.txt"), 445833)

    def test_sumNums2(self):
        """ test sumNums on the second file """
        self.assertEqual(sumNums("regex_sum_132198.txt"), 374566)

    def test_countWord(self):
        """ test count word on the first file """
        self.assertEqual(countWord("regex_sum_42.txt", "computer"),21)

    def test_listURLs(self):
        """ test list URLs on the first file """
        self.assertEqual(len(listURLs("regex_sum_42.txt")), 3)

# run the tests
unittest.main(verbosity=2)

