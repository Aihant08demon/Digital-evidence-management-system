import json
from pathlib import Path

class CaseManager:
    def __init__(self):
        self.file = Path("data/cases.json")
        self.cases = self.load()

    def load(self):
        if self.file.exists():
            return json.loads(self.file.read_text())
        return []

    def save(self):
        self.file.write_text(json.dumps(self.cases, indent=4))

    def add_case(self, case):
        if any(c["case_id"] == case["case_id"] for c in self.cases):
            print("Duplicate Case ID not allowed.")
            return
        self.cases.append(case)
        self.save()
        print("Case Added")

    def view_cases(self):
        for c in self.cases:
            print(c)

    def search_case(self, case_id):
        return next((c for c in self.cases if c["case_id"] == case_id), "Not Found")

    def update_status(self, case_id, status):
        for c in self.cases:
            if c["case_id"] == case_id:
                c["status"] = status
                self.save()
                print("Updated")
                return

    def delete_case(self, case_id):
        self.cases = [c for c in self.cases if c["case_id"] != case_id]
        self.save()
