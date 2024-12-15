
# Data de arquivamento: 15/12/2024

import random

class ComunicacaoAdaptativa:
    import random

class ComunicacaoAdaptativa:
    def __init__(self):
        self.contextos = ["escola", "faculdade", "casa", "trabalho", "lazer", "relacionamentos", "saúde", "finanças", "comunidade"]
        self.emocoes = ["feliz", "irritado", "aliviado", "desapontado", "inseguro", "entediado", "ansioso", "frustrado", "calmo", "empolgado", "triste", "confuso", "confiante", "estressado", "esperançoso"]
        self.emocoes_adicionais = ["irritado", "aliviado", "desapontado", "inseguro", "entediado"]
        self.emocoes_complexas = ["nostálgico", "culpado"]
        self.emocoes_contextos_sociais = ["rejeitado", "apoiado"]
        self.reacoes_fisicas = ["tenso", "entrando em crise de pânico"]
        self.emocoes_relacionadas_ao_aprendizado = ["curioso"]
        self.sentimentos_sobre_o_futuro = ["preocupado"]
        self.usuario_atual = None

    def interpretar_contexto(self, mensagem):
        palavras_chave = {
            "escola": ["aula", "professor", "lição", "estudar"],
            "casa": ["família", "lar", "doméstico"],
            "trabalho": ["emprego", "escritório", "carreira", "profissional"],
            "lazer": ["hobby", "diversão", "passatempo", "relaxar"],
            "relacionamentos": ["amigos", "namoro", "família", "social"],
            "saúde": ["bem-estar", "exercício", "médico", "doença"],
            "finanças": ["dinheiro", "economia", "gastos", "investimento"],
            "comunidade": ["bairro", "vizinhos", "voluntariado", "local"],
            "saúde mental": ["ansiedade", "depressão", "terapia"],
            "educação": ["curso", "ensino", "aprendizado"],
            "tecnologia": ["computador", "internet", "software"],
            "viagens": ["turismo", "viagem", "destino"],
            "cultura": ["arte", "música", "literatura"]
        }

        for contexto, palavras in palavras_chave.items():
            if any(palavra in mensagem.lower() for palavra in palavras):
                return contexto
        return random.choice(self.contextos)

    def analisar_emocao(self, mensagem):
        todas_emocoes = {
            "feliz": ["alegre", "contente", "satisfeito"],
            "ansioso": ["nervoso", "preocupado", "tenso"],
            "frustrado": ["irritado", "chateado", "desapontado"],
            "calmo": ["tranquilo", "sereno", "relaxado"],
            "empolgado": ["animado", "entusiasmado", "motivado"],
            "triste": ["melancólico", "abatido", "desanimado"],
            "confuso": ["perdido", "incerto", "em dúvida"],
            "confiante": ["seguro", "determinado", "otimista"],
            "estressado": ["sobrecarregado", "pressionado", "tenso"],
            "esperançoso": ["otimista", "positivo", "confiante"]
        }
        for emocao, palavras in todas_emocoes.items():
            if any(palavra in mensagem.lower() for palavra in palavras):
                return emocao
        return random.choice(self.emocoes)

    def gerar_resposta(self, mensagem):
        contexto = self.interpretar_contexto(mensagem)
        emocao = self.analisar_emocao(mensagem)

        if "python" in mensagem.lower() or "código" in mensagem.lower() or "programação" in mensagem.lower():
            return "Entendo que você está estudando Python. Que parte específica do Python você está achando difícil? Posso te dar algumas dicas ou explicar algum conceito específico."

        if "estudar" in mensagem.lower() or "entender" in mensagem.lower():
            return "Estudar pode ser desafiador às vezes. Sobre qual matéria ou tópico específico você gostaria de ajuda? Podemos quebrar o assunto em partes menores para facilitar o entendimento."

        respostas = {
            ("escola", "ansioso"): "Entendo que você está ansioso na escola. Que tal fazermos um exercício de respiração juntos?",
            ("casa", "feliz"): "Que bom que você está feliz em casa! Quer compartilhar o que está te deixando assim?",
            ("trabalho", "frustrado"): "Percebo que você está frustrado no trabalho. Vamos quebrar suas tarefas em partes menores?",
            ("lazer", "empolgado"): "É ótimo ver você empolgado com seu tempo de lazer! Que atividades você tem planejado?",
            ("relacionamentos", "confuso"): "Relacionamentos podem ser complicados. Quer conversar sobre o que está te deixando confuso?",
            ("saúde", "preocupado"): "Sua saúde é importante. Vamos listar suas preocupações e pensar em passos práticos para cada uma?",
            ("finanças", "estressado"): "Finanças podem ser estressantes. Que tal criarmos um plano de orçamento juntos?",
            ("comunidade", "esperançoso"): "É inspirador ver você esperançoso sobre sua comunidade. Tem algum projeto comunitário em mente?"
        }

        chave = (contexto, emocao)
        if chave in respostas:
            return respostas[chave]
        else:
            return f"Entendo que você está em um contexto de {contexto} e se sentindo {emocao}. Como posso te ajudar especificamente com isso?"

    def interagir(self):
        print("Bem-vindo à Plataforma de Comunicação Adaptativa!")
        self.usuario_atual = input("Como você gostaria de ser chamado? ")

        while True:
            try:
                mensagem = input(f"\n{self.usuario_atual}, como posso te ajudar hoje? (ou digite 'sair' para encerrar) ")
                if mensagem.lower() == 'sair':
                    print("Obrigado por usar nossa plataforma. Até a próxima!")
                    break

                resposta = self.gerar_resposta(mensagem)
                print(f"\nAssistente: {resposta}")

                feedback = input("Esta resposta foi útil? (sim/não) ")
                if feedback.lower() == 'não':
                    print("Sinto muito que a resposta não foi útil. Pode me dizer mais sobre o que você precisa? Estou aqui para ajudar da melhor forma possível.")
            except KeyboardInterrupt:
                print("\nEntendo que você pode precisar de uma pausa. Estou aqui quando quiser continuar.")
                continue

    def interagir(self):
        print("Bem-vindo à Plataforma de Comunicação Adaptativa!")
        self.usuario_atual = input("Como você gostaria de ser chamado? ")

        while True:
            try:
                mensagem = input(f"\n{self.usuario_atual}, como posso te ajudar hoje? (ou digite 'sair' para encerrar) ")
                if mensagem.lower() == 'sair':
                    print("Obrigado por usar nossa plataforma. Até a próxima!")
                    break

                resposta = self.gerar_resposta(mensagem)
                print(f"\nAssistente: {resposta}")

                feedback = input("Esta resposta foi útil? (sim/não) ")
                if feedback.lower() == 'não':
                    print("Sinto muito que a resposta não foi útil. Pode me dizer mais sobre o que você precisa? Estou aqui para ajudar da melhor forma possível.")
            except KeyboardInterrupt:
                print("\nEntendo que você pode precisar de uma pausa. Estou aqui quando quiser continuar.")
                continue

if __name__ == "__main__":
    plataforma = ComunicacaoAdaptativa()
    plataforma.interagir()
