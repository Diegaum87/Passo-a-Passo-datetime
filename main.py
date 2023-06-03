# 1.
from datetime import datetime, timedelta


STR_FORMATACAO = '%d/%m/%y %H:%M:%S'

# 2.
exame_realizado_em = datetime.now()

# 3.
print(exame_realizado_em)

# 4.
data_exame_str = exame_realizado_em.strftime(STR_FORMATACAO)

# 6.
TEMPO_RESULTADO_EXAME = timedelta(days=4)

# 7. 
print(TEMPO_RESULTADO_EXAME)

# 8
previsao_resultado = exame_realizado_em + TEMPO_RESULTADO_EXAME

# 9 
print(previsao_resultado)

# 10
previsao_de_entrega_str = previsao_resultado.strftime(STR_FORMATACAO)

# 11
print(previsao_de_entrega_str)

# 12
print(f"Data da realização do exame:{exame_realizado_em}")
print(f"Previsão de entrega do resultado:{previsao_de_entrega_str}")