# account.py

import csv
import os

class AccountManager:
    def __init__(self, file_path="data/customer.txt"):
        self.file_path = file_path
        os.makedirs("data", exist_ok=True)
        if not os.path.exists(self.file_path):
            open(self.file_path, "w").close()

    def register(self, username, password):
        accounts = self._load()
        if username in accounts:
            return False
        with open(self.file_path, "a", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([username, password])
        return True

    def login(self, username, password):
        accounts = self._load()
        return accounts.get(username) == password

    def _load(self):
        acc = {}
        with open(self.file_path, "r", encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    acc[row[0]] = row[1]
        return acc