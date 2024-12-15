import datetime

class NAIA:
    def __init__(self):
        self.user_name = "Babi"
        self.medications = [
            {"name": "Puran", "dose": "112 mcg"},
            {"name": "Bisoprolol", "dose": "2,5 mg"},
            {"name": "Venvanse", "dose": "70 mg"}
        ]
        self.med_log = {}

    def greet(self):
        current_time = datetime.datetime.now()
        if current_time.hour < 12:
            return f"Bom dia, {self.user_name}!"
        elif 12 <= current_time.hour < 18:
            return f"Boa tarde, {self.user_name}!"
        else:
            return f"Boa noite, {self.user_name}!"

    def remind_medications(self):
        meds = ", ".join([f"{med['name']} ({med['dose']})" for med in self.medications])
        return f"Lembre-se de tomar suas medicações: {meds}"

    def log_medication(self, med_name, time):
        if med_name in [med['name'] for med in self.medications]:
            today = datetime.date.today().isoformat()
            if today not in self.med_log:
                self.med_log[today] = {}
            self.med_log[today][med_name] = time
            return f"Registrado: {med_name} tomado às {time}"
        else:
            return "Medicação não reconhecida."

    def get_daily_report(self):
        today = datetime.date.today().isoformat()
        if today in self.med_log:
            report = "Relatório de hoje:\n"
            for med in self.medications:
                time = self.med_log[today].get(med['name'], "Não registrado")
                report += f"{med['name']}: {time}\n"
            return report
        else:
            return "Nenhuma medicação registrada hoje."

def main():
    naia = NAIA()
    print(naia.greet())
    print(naia.remind_medications())

    while True:
        command = input("Digite um comando (log/report/exit): ").lower()
        if command == "log":
            med = input("Qual medicação você tomou? ")
            time = input("Em que horário? ")
            print(naia.log_medication(med, time))
        elif command == "report":
            print(naia.get_daily_report())
        elif command == "exit":
            print("Até logo!")
            break
        else:
            print("Comando não reconhecido. Tente novamente.")

if __name__ == "__main__":
    main()
