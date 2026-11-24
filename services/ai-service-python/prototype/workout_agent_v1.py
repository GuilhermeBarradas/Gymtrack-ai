import os
from google import genai
from pydantic import BaseModel, Field

MODEL = "gemini-3.6-flash"  # para trocar se der erro de modelo

class ExerciseProgression(BaseModel):
    exercicio: str = Field(description="Nome do exercício analisado")
    volume_total_kg: int = Field(description="Soma total de (séries * repetições * carga)")
    analise_fadiga: str = Field(description="Diagnóstico técnico com base no RPE e repetições")
    carga_recomendada_proximo_treino_kg: float = Field(description="Peso sugerido para a próxima sessão")
    repeticoes_alvo: str = Field(description="Intervalo de repetições recomendado")

class WorkoutSessionAnalysis(BaseModel):
    resumo_sessao: str
    exercicios: list[ExerciseProgression]
    dica_recuperacao: str

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

treino_hoje = """
Treino A (Superior):
- Supino Inclinado com Halteres: 3 séries x 8, 8, 7 reps com 30kg (RPE 9.5 na última)
- Remada Curvada com Barra: 3 séries x 10, 10, 10 reps com 70kg (RPE 8 - controlado)
"""

response = client.models.generate_content(
    model=MODEL,
    contents=f"Analisa este treino e calcula a progressão de carga para a próxima semana:\n{treino_hoje}",
    config={
        "system_instruction": (
            "És um treinador especialista em força e hipertrofia baseada em evidência. "
            "Se o atleta atingiu o topo das repetições com RPE <= 8.5, sobe a carga em 2.5kg. "
            "Se falhou repetições com RPE >= 9.5, mantém a carga e foca na execução."
        ),
        "response_mime_type": "application/json",
        "response_schema": WorkoutSessionAnalysis,
        "temperature": 0.2,
    },
)

print(response.text)