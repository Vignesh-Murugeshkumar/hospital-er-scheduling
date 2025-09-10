import heapq
class EmergencyRoom:
    def __init__(self):
        self.queue = []
        self.counter = 0  # Tracks arrival order for tie-breaking
    def add_patient(self, name, severity):
        if not (1 <= severity <= 10):
            print("Severity must be between 1 and 10.")
            return
        heapq.heappush(self.queue, (-severity, self.counter, name))
        self.counter += 1
        print(f" Patient {name} (Severity: {severity}) added to queue.")
    def treat_next_patient(self):
        if self.queue:
            severity, _, name = heapq.heappop(self.queue)
            print(f" Treating patient {name} (Severity: {-severity})")
        else:
            print(" No patients left to treat.")
    def treat_all_patients(self):
        print("\n---  Treatment Order ---")
        while self.queue:
            self.treat_next_patient()
    def show_queue(self):
        print("\n Current Queue:")
        for s, _, n in sorted(self.queue, reverse=True):
            print(f"- {n} (Severity: {-s})")
def main():
    er = EmergencyRoom()
    try:
        n = int(input("Enter number of patients: "))
    except ValueError:
        print(" Invalid input. Please enter an integer.")
        return
    for i in range(n):
        name = input(f"\nEnter patient {i + 1} name: ").strip()
        while True:
            try:
                severity = int(input(f"Enter severity for {name} (1-10): "))
                if 1 <= severity <= 10:
                    break
                else:
                    print("Severity must be between 1 and 10.")
            except ValueError:
                print(" Please enter a valid integer.")
        er.add_patient(name, severity)
    while True:
        print("\nChoose an action:")
        print("1. Treat next patient")
        print("2. Treat all patients")
        print("3. Show queue")
        print("4. Exit")
        choice = input("Enter choice (1-4): ").strip()
        if choice == '1':
            er.treat_next_patient()
        elif choice == '2':
            er.treat_all_patients()
        elif choice == '3':
            er.show_queue()
        elif choice == '4':
            print(" Exiting Emergency Room system.")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()
