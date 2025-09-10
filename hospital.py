import heapq


class EmergencyRoom:
    def __init__(self):
        self.queue = []  # priority queue (max-heap using negative severity)

    def add_patient(self, name, severity):
        heapq.heappush(self.queue, (-severity, name))  # negative for max-heap
        print(f"Patient {name} (Severity: {severity}) added to queue.")

    def treat_all_patients(self):
        print("\n--- Treatment Order ---")
        while self.queue:
            severity, name = heapq.heappop(self.queue)
            print(f"Treating patient {name} (Severity: {-severity})")


# ---------------- Main Program ----------------
er = EmergencyRoom()

n = int(input("Enter number of patients: "))
for i in range(n):
    name = input(f"Enter patient {i + 1} name: ")
    severity = int(input(f"Enter severity for {name} (1-10): "))
    er.add_patient(name, severity)

# Automatically treat all patients
er.treat_all_patients()
