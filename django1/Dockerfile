# Usar uma imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos requirements.txt e instala as dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código para o container
COPY . /app/

# Expõe a porta em que o Django vai rodar
EXPOSE 8000

# Comando para rodar o Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
