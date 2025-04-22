from pydantic import BaseModel, Field, root_validator, ValidationError
from typing import Optional

class planilha_vendas(BaseModel):
    Organizador: int = Field(..., description="Identificador do Organizador")
    Ano_Mes: str = Field(..., description="Ano e mês no formato")
    Dia_da_Semana: str = Field(..., description="Dia da semana")
    Tipo_Dia: str = Field(..., description="Classificação do dia: útil, feriado, etc.")
    Objetivo: str = Field(..., description="Objetivo da campaha ou ação")
    Date: str = Field(..., description="Data da entrada no formato YYYY-MM-DD")
    AdSet_name: Optional[str] = Field(description="Nome do conjunto de anúncios")
    Amount_spent: float = Field(0.0, ge=0, le=1200.00, description="Valor gasto no anúncio (mínimo 0, máximo 589.96")
    Link_clicks: Optional[float] = Field(None, description="Número de cliques no link", nullable=True)
    Impressions: Optional[float] = Field(0, description="Número de impressões do anúncio", nullable=True)
    Conversions: Optional[float] = Field(None, description="Número de conversões", nullable=True)
    Segmentação: str = Field(None, description="Segmentação usada")
    Tipo_de_Anúncio: str = Field(..., description="Tipo de anúncio")
    Fase: str = Field(..., description="Fase do funil de vendas")

    class Config:
        validate_default: True # Garante que os valores padrão sejam validados automaticamente
