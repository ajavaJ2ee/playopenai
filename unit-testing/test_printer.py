from unittest import TestCase
from printer import Printer,PrinterError


class TestPrinter(TestCase):

    def setUp(self):
        self.printer=Printer(pages_per_s=2.0, capacity=300)


    def test_printer_within_capacity(self):
        message= self.printer.print(25)


    def test_printer_outside_capacity(self):
        with self.assertRaises(PrinterError):
            self.printer.print(301)

    def test_printer_exact_capacity(self):
        message= self.printer.print(self.printer._capacity)
        self.assertEqual(f"Printed 300 pages in 150.00 seconds",message)

    def test_printer_speed(self):
        pages=10
        expected="Printed 10 pages in 5.00 seconds"
        result=self.printer.print(10)
        self.assertEqual(result,expected)

    def test_multiple_printer_runs(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

    def test_multiple_runs_end_up_error(self):
        self.printer.print(25)
        self.printer.print(50)
        self.printer.print(225)

        with self.assertRaises(RuntimeError):
            self.printer.print(1)