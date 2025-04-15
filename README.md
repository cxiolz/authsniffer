# 🔐 AuthSniffer — Burp Suite Extension

Extensão para Burp Suite feita em Python (Jython) que **detecta automaticamente** tokens sensíveis em requisições e respostas HTTP.  
Ideal pra quem quer farejar **JWTs, Bearer tokens, API Keys, Basic Auth e outros segredos** que aparecem no tráfego durante um pentest.

---

## 💥 Funcionalidades

- 🚨 Detecta tokens e chaves automaticamente
- 🔍 Suporte a JWT, Bearer, Basic, API Keys, etc
- 📚 Mostra resultados em uma aba exclusiva no Burp
- 🔁 Escuta tanto requisições quanto respostas
- 🔥 Código limpo, simples e pronto pra extensão

---

## 🧠 Regex Detectadas

- `Bearer <token>`
- JWTs no formato `eyJ...`
- API Keys tipo `api_key=...`
- Headers `Authorization: Basic ...`
- Tokens base64 e similares

---

## 🛠️ Instalação

### 1. Requisitos

- [Burp Suite (Community ou Pro)](https://portswigger.net/burp)
- [Jython standalone 2.7.x JAR](https://www.jython.org/download.html)

> ⚠️ Burp Suite ainda **não suporta Python 3** com extensões. Use **Jython 2.7**.

---

### 2. Como Rodar

1. Baixe este repositório.
2. Abra o Burp Suite.
3. Vá em `Extender > Options > Python Environment` e selecione o `jython-standalone-2.7.x.jar`.
4. Vá em `Extender > Extensions`, clique em `Add`.
5. Selecione:
   - Type: **Python**
   - File: `sniffer.py`
6. A aba **"AuthSniffer"** aparecerá no Burp.
7. Use normalmente o Burp — a extensão mostrará tokens detectados em tempo real.

---

## ✨ Melhorias Futuras

- [ ] Exportar tokens para `.txt`
- [ ] Adicionar botão "Copiar"
- [ ] Exibir origem do token (URL, método, etc)
- [ ] Classificar tokens por tipo (JWT, Basic, etc)
- [ ] Adicionar botão "Reusar token" para testes rápidos

---

## 👨‍💻 Autor

**Caio Luchetti**  
🔗 [LinkedIn](https://www.linkedin.com/in/caio-luchetti/)  
🐙 GitHub: [@cxiolz](https://github.com/cxiolz)

---

## 🧠 Licença

MIT — Faça o que quiser, só não diga que foi você que fez 😎
