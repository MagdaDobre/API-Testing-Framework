import unittest
import HtmlTestRunner
from API_project.Tests.test_books import TestBooks
from API_project.Tests.test_orders import TestOrders
from API_project.Tests.test_status import TestStatus
from API_project.Tests.test_api_client import TestApiClient

class MyTestSuite(unittest.TestCase):
        #numele metodei este predefinit si nu trebuie schimbat.
    def test_suite(self):
        #prin obiectul creat test_to_run vom accesa metoda addTests
        test_to_run = unittest.TestSuite()
        test_to_run.addTests(
            [
            unittest.defaultTestLoader.loadTestsFromTestCase(TestBooks),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestStatus),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestOrders),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestApiClient)
            ]
        )
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='MagdaRaportProiect',
            report_title = 'FinalProject'
        )
        runner.run(test_to_run)
