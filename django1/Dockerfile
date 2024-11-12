# Usando a imagem do Python
FROM python:3.9

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiando o arquivo requirements.txt
COPY requirements.txt /app/

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da pasta 'app' para o diretório de trabalho no container
COPY app /app

# Expondo a porta 8000 para o Django
EXPOSE 8000

# Comando para rodar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
