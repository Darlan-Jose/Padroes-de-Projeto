from abc import ABC, abstractmethod

# --- PRODUTO (Interface) ---
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem: str) -> None:
        pass

# --- PRODUTOS CONCRETOS ---
class SMSNotificador(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"[SMS] Enviando torpedo: {mensagem}")

class WhatsAppNotificador(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"[WhatsApp] Enviando mensagem criptografada: {mensagem}")

class EmailNotificador(Notificador):
    def enviar(self, mensagem: str) -> None:
        print(f"[E-mail] Enviando correio eletrônico: {mensagem}")


# --- CRIADOR (Creator) ---
class Logistica(ABC):
    """
    O Criador declara o Factory Method que deve retornar um objeto Notificador.
    """
    
    @abstractmethod
    def criar_notificador(self) -> Notificador:
        """O Factory Method propriamente dito."""
        pass

    def gerenciar_entrega(self, pacote_id: str) -> None:
        """
        A lógica de negócio principal não depende de classes concretas,
        apenas do produto retornado pelo Factory Method.
        """
        notificador = self.criar_notificador()
        mensagem = f"O pacote {pacote_id} está a caminho!"
        
        print(f"\nLogística: Processando entrega {pacote_id}...")
        notificador.enviar(mensagem)


# --- CRIADORES CONCRETOS ---
class LogisticaNacional(Logistica):
    def criar_notificador(self) -> Notificador:
        return SMSNotificador()

class LogisticaInternacional(Logistica):
    def criar_notificador(self) -> Notificador:
        return WhatsAppNotificador()

class LogisticaB2B(Logistica):
    def criar_notificador(self) -> Notificador:
        return EmailNotificador()


# --- CLIENTE (Uso Polimórfico) ---
def cliente_code(logistica: Logistica, id_pacote: str):
    """
    O código cliente trabalha com qualquer instância de Logistica 
    via sua interface abstrata.
    """
    logistica.gerenciar_entrega(id_pacote)


if __name__ == "__main__":
    print("--- Sistema de Notificação de Logística ---")

    # O cliente decide qual fábrica usar baseada no contexto, 
    # mas o resto do sistema trata todas de forma polimórfica.
    
    print("\nCenário 1: Entrega no Brasil")
    cliente_code(LogisticaNacional(), "BR-123")

    print("\nCenário 2: Entrega na Europa")
    cliente_code(LogisticaInternacional(), "EU-987")

    print("\nCenário 3: Entrega para Empresa Parceira")
    cliente_code(LogisticaB2B(), "CORP-555")