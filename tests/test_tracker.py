import unittest
from services.tracker import Tracker
import os
import tempfile

class TestTracker(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.tracker = Tracker(file_path=self.temp_file.name)

    def tearDown(self):
        os.unlink(self.temp_file.name)

    def test_add_transaction(self):
        self.tracker.add_transaction(100, "salary", "income")
        self.assertEqual(len(self.tracker.transactions), 1)
        self.assertEqual(self.tracker.transactions[0]["amount"], 100)

    def test_remove_transaction(self):
        self.tracker.add_transaction(50, "food", "expense")
        trans_id = self.tracker.transactions[0]["id"]
        self.tracker.remove_transaction(trans_id)
        self.assertEqual(len(self.tracker.transactions), 0)

    def test_generate_report(self):
        self.tracker.add_transaction(200, "job", "income")
        self.tracker.add_transaction(50, "snacks", "expense")
        income = sum(t["amount"] for t in self.tracker.transactions if t["type"] == "income")
        expense = sum(t["amount"] for t in self.tracker.transactions if t["type"] == "expense")
        self.assertEqual(income, 200)
        self.assertEqual(expense, 50)

if __name__ == "__main__":
    unittest.main()
