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
        self.conversation_history = []

    def greet(self):
        current_time = datetime.datetime.now()
        if current_time.hour < 12:
            greeting = f"Bom dia, {self.user_name}!"
        elif 12 <= current_time.hour < 18:
            greeting = f"Boa tarde, {self.user_name}!"
        else:
            greeting = f"Boa noite, {self.user_name}!"
        return f"{greeting} Como você está se sentindo hoje? Dormiu bem?"

    def remind_medications(self):
        meds = ", ".join([f"{med['name']} ({med['dose']})" for med in self.medications])
        return f"Não se esqueça de suas medicações de hoje: {meds}. Já tomou alguma delas?"

    def log_medication(self, med_name, time):
        if med_name.lower() in [med['name'].lower() for med in self.medications]:
            today = datetime.date.today().isoformat()
            if today not in self.med_log:
                self.med_log[today] = {}
            self.med_log[today][med_name] = time
            return f"Ótimo, {self.user_name}! Registrei que você tomou {med_name} às {time}. Como está se sentindo após tomar o remédio?"
        else:
            return f"Desculpe, {self.user_name}, mas não reconheço essa medicação. Pode verificar o nome e me dizer novamente?"

    def get_daily_report(self):
        today = datetime.date.today().isoformat()
        if today in self.med_log:
            report = f"{self.user_name}, aqui está seu relatório de hoje:\n"
            for med in self.medications:
                time = self.med_log[today].get(med['name'], "Não registrado")
                report += f"{med['name']}: {time}\n"
            return report + "\nComo você está se sentindo em relação à sua rotina de medicações?"
        else:
            return f"{self.user_name}, ainda não registrei nenhuma medicação hoje. Quer que eu te lembre dos horários?"

    def process_input(self, user_input):
        self.conversation_history.append(("user", user_input))
        
        if "bom dia" in user_input.lower() or "boa tarde" in user_input.lower() or "boa noite" in user_input.lower():
            response = self.greet()
        elif "medicação" in user_input.lower() or "remédio" in user_input.lower():
            response = self.remind_medications()
        elif "tomei" in user_input.lower():
            parts = user_input.split()
            if len(parts) >= 4 and "às" in parts:
                med_name = parts[parts.index("tomei") + 1]
                time = parts[parts.index("às") + 1]
                response = self.log_medication(med_name, time)
            else:
                response = f"{self.user_name}, pode me dizer qual medicação você tomou e o horário? Por exemplo: 'Tomei Puran às 08:00'"
        elif "relatório" in user_input.lower():
            response = self.get_daily_report()
        elif "tchau" in user_input.lower() or "até logo" in user_input.lower():
            response = f"Até logo, {self.user_name}! Cuide-se bem e não se esqueça das suas medicações. Estarei aqui se precisar de algo."
        elif "sim" in user_input.lower() or "não" in user_input.lower():
            response = f"Entendo, {self.user_name}. Pode me contar mais sobre como está se sentindo? Estou aqui para ajudar no que for preciso."
        elif "cansada" in user_input.lower() or "cansado" in user_input.lower():
            response = f"Sinto muito que você esteja se sentindo cansada, {self.user_name}. Lembre-se de descansar e se hidratar bem. Quer que eu te sugira algumas técnicas de relaxamento?"
        else:
            response = f"{self.user_name}, não tenho certeza se entendi completamente. Pode me explicar um pouco mais sobre o que você precisa?"

        self.conversation_history.append(("NAIA", response))
        return response

def main():
    naia = NAIA()
    print("NAIA: " + naia.greet())

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ['sair', 'exit', 'quit']:
            print(f"NAIA: Até logo, {naia.user_name}! Cuide-se bem. Estarei aqui quando precisar.")
            break
        response = naia.process_input(user_input)
        print("NAIA:", response)

if __name__ == "__main__":
    main()
