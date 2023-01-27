import unittest
import io
import sys
import python_print

class TestPrintStatements(unittest.TestCase):

    def test_print_hello_world(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        python_print.print_hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), "Hello, World!")

    def test_print_love_python(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        python_print.print_love_python()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), "I really love Python")
       
    def test_print_calculations(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        python_print.print_calculations()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), "5\n3\n28\n3.0\n8\n10.0\n6.0")

       
    def test_print_advanced_usage(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        python_print.print_advanced_usage()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue().strip(), "Hello|World!\n42-is a great-number\nHello, World!!!Starting a calculation...4*3 Done: -> 12")


if __name__ == '__main__':
    unittest.main()