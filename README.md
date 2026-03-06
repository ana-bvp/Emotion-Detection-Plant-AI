# Emotion Detection Plant AI

Este projeto é uma aplicação web baseada em IA para detecção de emoções em textos. Utiliza a biblioteca Watson NLP da IBM e o framework Flask para o backend.

## Funcionalidades
- Análise de 5 emoções: Raiva (Anger), Nojo (Disgust), Medo (Fear), Alegria (Joy) e Tristeza (Sadness).
- Identificação da emoção dominante.
- Tratamento de erros para entradas vazias (Status 400).
- Testes unitários integrados.

## Como Executar
1. Instale as dependências: `pip install flask requests pylint`
2. Execute o servidor: `python3 server.py`
3. Aceda a `http://localhost:5000` no seu navegador.
