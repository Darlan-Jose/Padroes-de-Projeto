# Índices
[Factory Method](https://github.com/Darlan-Jose/Padroes-de-Projeto/blob/main/Factory_Method/main.py)

# Factory Method
## 🏗️ Estrutura do Padrão

A implementação segue os papéis canônicos do Design Pattern:

- **Product:** `Notificador` (Interface/Classe Abstrata).
    
- **Concrete Products:** `SMSNotificador`, `WhatsAppNotificador`, `EmailNotificador`.
    
- **Creator:** `Logistica` (Classe Abstrata com o Factory Method).
    
- **Concrete Creators:** `LogisticaNacional`, `LogisticaInternacional`, `LogisticaB2B`.
    

## 🚀 Como Executar

### Pré-requisitos

- Python 3.8 ou superior instalado.
    

### Passo a Passo

1. **Clone o repositório:**
    
    
    ``` bash
    git clone https://github.com/Darlan-Jose/Padroes-de-Projeto
    cd Padroes-de-Projeto
    cd Factory_Method
    ```
    
2. **Execute o script principal:**
    
    O exemplo foi consolidado em um único arquivo para facilitar a visualização didática.
    
    ``` bash
    python main.py
    ```
    ou
	``` bash
	py main.py    
	```

## 🧪 Demonstração de Uso

O arquivo principal (`main.py`) demonstra o uso polimórfico. O código cliente interage apenas com a abstração `Logistica`, sem saber qual classe concreta está sendo instanciada por baixo do capô:

``` Python
# Exemplo de polimorfismo no cliente
def cliente_code(logistica: Logistica, id_pacote: str):
    logistica.gerenciar_entrega(id_pacote)

# Uso
cliente_code(LogisticaNacional(), "BR-123") # Produz SMS
cliente_code(LogisticaInternacional(), "EU-987") # Produz WhatsApp
```
