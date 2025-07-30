# Mobile_Python
- utilizar android 13.
- executar a partir da branch master

- Executar a partir da pasta mobile_python

# 📱 Projeto Mobile com Python + Behave + Allure
 
Este projeto utiliza **Python**, **Behave**, **Appium** e **Allure Reports** para automação de testes em aplicações mobile.
 
---
 
## ⚙️ Pré-requisitos
 
- Modelo do dispositivo - Motorola g52
- Python 3.10 ou superior
- Appium instalado e em execução
- Allure https://allurereport.org/docs/behave/
- Editor recomendado: [PyCharm](https://www.jetbrains.com/pycharm/)
 
---
 
## 📦 Criar o ambiente virtual
 
1. No terminal, navegue até a pasta do projeto:
 
   ```bash
   cd caminho/para/seu/projeto

2. Crie o ambiente virtual
 
  python -m venv .venv

3. Ative o ambiente virtual:
   
  Windows (PowerShell):
  .\.venv\Scripts\activate
  Linux/macOS:
  source .venv/bin/activate

5. Instale as dependências:
   
  pip install -r requirements.txt

▶️ Executando os testes
Após ativar o ambiente virtual, basta dar play no arquivo main.py na raiz do projeto (ou executá-lo via terminal):
 
python main.py
 
Esse arquivo é responsável por iniciar a suíte de testes.

📊 Gerando o Allure Report

Execute no terminal: 
1. allure generate 
2. allure open

❗ Dicas

Se estiver usando PyCharm, certifique-se de configurar o Python Interpreter para usar o .venv criado na pasta do projeto.
Verifique se o Appium está rodando antes de iniciar os testes.
Caso o comando allure não funcione, verifique se o diretório do Allure CLI está no seu PATH.

  
