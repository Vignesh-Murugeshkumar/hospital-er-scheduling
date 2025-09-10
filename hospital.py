import heapq
class EmergencyRoom:
    def __init__(self):
        self.queue = []  
    def add_patient(self, name, severity):
        heapq.heappush(self.queue, (-severity, name))  
        print(f"Patient {name} (Severity: {severity}) added to queue.")
    def treat_all_patients(self):
        print("\n--- Treatment Order ---")
        while self.queue:
            severity, name = heapq.heappop(self.queue)
            print(f"Treating patient {name} (Severity: {-severity})")
er = EmergencyRoom()
n = int(input("Enter number of patients: "))
for i in range(n):
    name = input(f"Enter patient {i + 1} name: ")
    severity = int(input(f"Enter severity for {name} (1-10): "))
    er.add_patient(name, severity)
er.treat_all_patients()

