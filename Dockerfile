FROM python:3.11-slim

# Cria o usuário não-root exigido pelo Hugging Face Spaces
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

# Copia e instala as dependências
COPY --chown=user:user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia toda a estrutura do seu projeto (src, app, pages, docs, data)
COPY --chown=user:user . .

# Expõe a porta que o Hugging Face escuta obrigatoriamente
EXPOSE 7860

# Executa o Streamlit apontando para o seu arquivo principal
CMD ["streamlit", "run", "main.py", "--server.port=7860", "--server.address=0.0.0.0"]
