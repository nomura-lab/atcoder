import sys
from io import StringIO
import unittest

def resolve():

    a,b = map(int,input().split())

    if a < 10 and b < 10 and a > 0 and b > 0 :
        print(a*b)
    else:
        print(-1)

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 10"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """9 9"""
        output = """81"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()