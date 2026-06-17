import json
from pathlib import Path

class EvidenceManager:
    def __init__(self):
        self.file = Path("data/evidence.json")
        self.evidence = self.load()

    def load(self):
        if self.file.exists():
            return json.loads(self.file.read_text())
        return []

    def save(self):
        self.file.write_text(json.dumps(self.evidence, indent=4))

    def add_evidence(self, ev):
        self.evidence.append(ev)
        self.save()
        print("Evidence Added")
