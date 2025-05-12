import matplotlib.pyplot as plt

# Dados fictícios
meses = ['June']
vendas_mensais = [1200, 1500, 1700, 1600, 1800, 2000]

produtos = ['Produto A', 'Produto B', 'Produto C']
vendas_produtos = [3200, 2800, 2300]

participacao = [40, 35, 25]

# Gráfico de linha - Vendas Mensais
plt.figure(figsize=(8, 5))
plt.plot(meses, vendas_mensais, marker='o', color='blue')
plt.title('Vendas Mensais')
plt.xlabel('Mês')
plt.ylabel('Vendas (R$)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico de barras - Vendas por Produto
plt.figure(figsize=(8, 5))
plt.bar(produtos, vendas_produtos, color='green')
plt.title('Vendas por Produto')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas (R$)')
plt.tight_layout()
plt.show()

# Gráfico de pizza - Participação de Mercado
plt.figure(figsize=(6, 6))
plt.pie(participacao, labels=produtos, autopct='%1.1f%%', startangle=90)
plt.title('Participação de Mercado por Produto')
plt.tight_layout()
plt.show()
