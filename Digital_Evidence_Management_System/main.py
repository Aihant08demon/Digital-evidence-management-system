from case_manager import CaseManager
from evidence_manager import EvidenceManager
from report_generator import ReportGenerator

cm = CaseManager()
em = EvidenceManager()
rg = ReportGenerator()

while True:
    print("\n=== Digital Evidence Management System ===")
    print("1. Add Case")
    print("2. View Cases")
    print("3. Search Case")
    print("4. Update Status")
    print("5. Delete Case")
    print("6. Add Evidence")
    print("7. Generate Reports")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        case = {
            "case_id": input("Case ID: "),
            "crime_type": input("Crime Type: "),
            "location": input("Location: "),
            "date": input("Date (YYYY-MM-DD): "),
            "officer": input("Officer Assigned: "),
            "suspect": input("Suspect Name: "),
            "status": input("Investigation Status: "),
            "priority": input("Priority (Low/Medium/High): ")
        }
        cm.add_case(case)

    elif choice == "2":
        cm.view_cases()

    elif choice == "3":
        cid = input("Case ID: ")
        print(cm.search_case(cid))

    elif choice == "4":
        cm.update_status(input("Case ID: "), input("New Status: "))

    elif choice == "5":
        cm.delete_case(input("Case ID: "))

    elif choice == "6":
        ev = {
            "case_id": input("Case ID: "),
            "evidence_type": input("Evidence Type: "),
            "description": input("Description: ")
        }
        em.add_evidence(ev)

    elif choice == "7":
        rg.generate_reports(cm.cases, em.evidence)

    elif choice == "8":
        break
