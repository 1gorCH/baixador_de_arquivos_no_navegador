# Automação Web com Selenium – Download Automático de Arquivos

Este script realiza uma **automação web com Selenium**, configurando o navegador para **baixar arquivos automaticamente em uma pasta definida**, com opção de execução **oculta (headless)**, permitindo que o processo rode em segundo plano.

## 🚀 Funcionalidades
- Configuração personalizada da pasta de download
- Download automático sem interação do usuário
- Execução com ou sem exibição do navegador (headless)
- Acesso automatizado a página web
- Controle total do Chrome via Selenium

## 🛠️ Tecnologias Utilizadas
- Python
- Selenium
- ChromeDriver
- Google Chrome

## ⚙️ Configuração de Download
```python
preferencias = {
    "download.default_directory": pasta_destino
}
```
# 🧭 Execução em Segundo Plano
```python
options.headless = True
```
True → navegador oculto (execução em 2º plano)
False → navegador visível durante a automação

# 🌐 Acesso à Página Web

```python
navegador.get("https://rpachallenge.com/")
```

***📌 Observações: O caminho do ChromeDriver deve estar correto; O Google Chrome precisa estar instalado; Alguns sites podem bloquear downloads automáticos; Para maior robustez, recomenda-se o uso de WebDriverWait***
