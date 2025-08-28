# 🕊️ BirdFly  
**Scanner de Cabeçalhos HTTP para Domínios**  

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/status-beta-orange.svg)]()  

---

## 📖 Sobre o Projeto
O **BirdFly** é uma ferramenta simples para análise de **cabeçalhos HTTP de segurança** em aplicações web.  
Foi desenvolvida por **Marius Jabami** e **Yumi**, membros da **SEC-0**, com o objetivo de oferecer uma **base sólida** para quem deseja aprender, estudar ou expandir um projeto de scanner.  

---

## 🚀 Objetivo
Criar um **template inicial** para que desenvolvedores, pesquisadores e entusiastas em **AppSec** tenham um ponto de partida prático e extensível.  

---

## ⚙️ Instalação
Clone o repositório e instale as dependências:  

```bash
git clone https://github.com/seu-usuario/birdfly.git
cd birdfly
pip install -r requirements.txt
```

---

## ▶️ Uso

Exibir o menu de ajuda:
```Bash
python birdfly.py -h
```
Exemplo de varredura em um domínio:
```Bash
python birdfly.py -u https://exemplo.com
```
## Saída esperada:

```Bash
[+] Verificando cabeçalhos de https://exemplo.com
[✔] X-Content-Type-Options: presente
[✖] X-Frame-Options: ausente
[✔] Strict-Transport-Security: presente
```

---

## 📌 Roadmap

[ ] Melhorar suporte a múltiplos domínios

[ ] Adicionar exportação em JSON/CSV

[ ] Criar integração com CI/CD

[ ] Ampliar verificação para OWASP Secure Headers



---

## 🤝 Contribuindo

Sinta-se à vontade para forkar o repositório e enviar pull requests.
Toda contribuição é bem-vinda para melhorar e expandir o BirdFly.


---

## 📜 Licença

Distribuído sob a licença MIT. Veja LICENSE para mais detalhes.


---

## ✍️ Autoria

Projeto desenvolvido pela SEC-0
Artigo escrito por Marius Jabami

📢 Menção especial: @mariusjabami

---