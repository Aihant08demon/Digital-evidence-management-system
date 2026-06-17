import csv
from pathlib import Path

class ReportGenerator:
    def generate_reports(self, cases, evidence):
        Path("reports").mkdir(exist_ok=True)

        with open("reports/cases_report.txt","w") as f:
            f.write("ACTIVE CASES\n\n")
            for c in cases:
                f.write(str(c)+"\n")

        if cases:
            with open("reports/cases_report.csv","w",newline="") as f:
                writer = csv.DictWriter(f, fieldnames=cases[0].keys())
                writer.writeheader()
                writer.writerows(cases)

        print("Reports Generated")
