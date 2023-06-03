# Passo-a-Passo-datetime


Exercitando a biblioteca datetime
Para esse exercício, vamos imaginar que você está indo fazer um exame de sangue.

Antes de tudo, crie uma constante STR_FORMATACAO, que vai armazenar a string contendo o padrão de caracteres do strftime para que utilizarmos nas nossas formatações de string.
Crie uma variável exame_realizado_em que contenha a data e hora atual, utilizando now, para simular a data do seu exame.
Imprima na tela a variável recém criada.
Formate o valor da variável criada para melhor legibilidade e atribua o resultado a outra variável data_exame_str. Para isso, use strftime.
Printe o valor de data_exame_str.
Crie uma constante, chamada TEMPO_RESULTADO_EXAME, e grave o tempo padrão que os resultados dos exames de sangue demoram para serem liberados. Neste caso, utilize timedelta.
Printe o valor de TEMPO_RESULTADO_EXAME.
Agora, crie uma variável previsao_resultado que guardará a data e hora da previsão de entrega do resultado. Neste caso, você fará uma operação matemática para conseguir a data estimada.
Imprima na tela previsao_resultado.
Formate-a para melhor legibilidade, assim como foi feito no passo 2, e armazene a formatação em uma variável chamada previsao_de_entrega_str.
Imprima na tela a formatação feita em previsao_de_entrega_str.
Por fim, printe exame_realizado_em e previsao_de_entrega_str no seguinte padrão:
"Data de realização do exame: 27/05/22 13:56:37"
"Previsão de entrega do resultado: 29/05/22 13:56:37"

