from abc import ABC, abstractmethod

# O canal é o meio por onde a mensagem será entregue.
class Canal(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass

# Os canais concretos implementam o canal.
class CanalSMS(Canal):
    def enviar(self, mensagem: str) -> None:
        print(f"[SMS] Enviando torpedo: {mensagem}")

class CanalEmail(Canal):
    def enviar(self, mensagem: str) -> None:
        print(f"[E-mail] Enviando correio eletrônico: {mensagem}")

class CanalWhatsApp(Canal):
    def enviar(self, mensagem: str) -> None:
        print(f"[WhatsApp] Enviando mensagem criptografada: {mensagem}")


class Prioridade(ABC):
    def __init__(self, canal: Canal): # AQUI está a ponte!
        self.canal = canal

    @abstractmethod
    def processar_notificacao(self, mensagem: str) -> None:
        pass


class Urgente(Prioridade):
    def processar_notificacao(self, mensagem: str) -> None:
        
        msg_formatada = f"!!! PRIORIDADE MÁXIMA !!!: {mensagem}"
        
        self.canal.enviar(msg_formatada)

class Baixa(Prioridade):
    def processar_notificacao(self, mensagem: str) -> None:
        msg_formatada = f"Aviso: {mensagem}"
        self.canal.enviar(msg_formatada)



# Você escolhe o CANAL (Implementação)
sms = CanalSMS()
whats = CanalWhatsApp()

# Você combina com a URGÊNCIA (Abstração)
notificacao1 = Urgente(sms)
notificacao1.processar_notificacao("Servidor caiu!") 
# Saída: [SMS] Enviando torpedo: !!! PRIORIDADE MÁXIMA !!!: Servidor caiu!

notificacao2 = Baixa(whats)
notificacao2.processar_notificacao("O café está pronto.")
# Saída: [WhatsApp] Enviando mensagem: Aviso: O café está pronto.