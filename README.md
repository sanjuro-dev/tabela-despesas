# Controle de Despesas com Tkinter

Este é um aplicativo simples em Python para registrar despesas mensais, categorizá-las e visualizar gráficos de distribuição e gastos mensais.

## Funcionalidades

* Cadastro de despesas por categoria, descrição e valor.
* Armazenamento dos dados em arquivo Excel (`planilha.xlsx`).
* Geração de gráficos:

  * Pizza: Distribuição percentual dos gastos por categoria no mês atual.
  * Barras: Gastos totais por mês no ano atual.

## Tecnologias Utilizadas

* Python 3.x
* Tkinter (interface gráfica)
* Pandas (manipulação de dados)
* Matplotlib (gráficos)
* Openpyxl (para leitura/escrita de Excel)

## Como usar

1. Certifique-se de ter Python 3 instalado.
2. Instale as dependências:

```bash
pip install pandas matplotlib openpyxl
```

3. Execute o script:

```bash
python seu_arquivo.py
```

4. Na interface, selecione a categoria, preencha descrição e valor, e clique em **Adicionar** para salvar uma despesa.
5. Clique em **Gerar Dados** para visualizar os gráficos.

## Observações

* O arquivo `planilha.xlsx` será criado automaticamente na primeira execução.
* Os valores devem ser informados usando ponto ou vírgula decimal (ex: `10.50` ou `10,50`).
* O gráfico de pizza considera apenas despesas do mês atual.

## Estrutura do arquivo Excel

| Categoria  | Descrição    | Valor  | Data       |
| ---------- | ------------ | ------ | ---------- |
| Luz        | Conta de luz | 100.00 | 2025-08-07 |
| Transporte | Ônibus       | 15.50  | 2025-08-07 |

## Exemplo de categorias

* Luz
* Wi-Fi
* Transporte
* Comida
* Lazer

