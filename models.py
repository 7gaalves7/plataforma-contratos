from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

# Esta tabela guarda as informações da pessoa
class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    cpf: str
    telefone: str
    email: str
    endereco: str

# Esta tabela guarda as informações do serviço que você está vendendo
class Contrato(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="cliente.id") # Isso liga o contrato ao cliente
    valor_servico: float
    data_vencimento: date
    status: str = "Pendente" # Ex: Pendente, Assinado, Cancelado
