![Streamlit App](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)

# 🎯 Sorteio de Vagas de Condomínio

Aplicativo desenvolvido com **Streamlit** para realizar o sorteio e alocação de vagas de garagem em condomínios, com base nas preferências das unidades e nas categorias de vagas.

---

## 🚗 Funcionalidades

- 📂 Upload dos arquivos de **Cadastro de Unidades** e **Cadastro de Vagas**
- 🔀 Filtro por tipo de vaga: **PNE**, **TRIPLO** ou **DUPLO**
- 🎲 Sorteio da ordem das unidades
- ✅ Alocação das vagas com base nas **preferências**
- 🎲 Alocação **aleatória** para unidades que não conseguiram uma vaga preferencial
- 🔍 Busca individual para verificar a vaga alocada de uma unidade
- 📥 Exportação do resultado completo em Excel
- 🧾 Separação clara entre alocações por **preferência** e **aleatória**

---

## 🗂️ Estrutura do Projeto

```
sorteio_vagas_app/
├── streamlit_app.py          # Arquivo de entrada principal
├── app/
│   ├── main.py               # Código principal da aplicação
│   ├── core/
│   │   ├── sorteio.py        # Funções de sorteio e alocação
│   │   └── exportacao.py     # Função de exportação para Excel
│   ├── pages/                # (opcional) páginas extras do Streamlit
│   └── data/                 # (opcional) arquivos de entrada e exemplo
├── .streamlit/
│   └── config.toml           # Configuração de tema para Streamlit Cloud
├── README.md
├── requirements.txt
└── LICENSE (opcional)
```

---

## 📄 Formato dos Arquivos

### Cadastro de Unidades

| unidade   | tipo   | preferencia_1 | preferencia_2 | ... |
|-----------|--------|---------------|---------------|-----|
| 101A      | TRIPLO | 01            | 02            | ... |

- `tipo`: deve ser um dos valores **PNE**, **TRIPLO** ou **DUPLO**
- `preferencia_n`: representa o grupo da vaga desejada

### Cadastro de Vagas

| vagas   | grupo_vaga | pavimento | tipo   |
|---------|------------|-----------|--------|
| 01 - 02 | 01         | 1º andar  | TRIPLO |
| 03 - 04 | 02         | TÉRREO    | DUPLO  |

---

## ▶️ Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sorteio-vagas-condominio.git
   cd sorteio-vagas-condominio
   ```

2. Crie e ative o ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o app:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## ☁️ Como publicar na Streamlit Cloud

1. Acesse: https://streamlit.io/cloud  
2. Clique em **"New app"** e conecte seu repositório GitHub  
3. Escolha o arquivo `streamlit_app.py` como ponto de entrada  
4. Certifique-se de que seu repositório contenha:
   - `streamlit_app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`
5. Clique em **Deploy** — pronto!

---

## 📃 Licença

Este projeto está licenciado sob a **MIT License** – veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **Guilherme Fidalgo**  
[LinkedIn](https://www.linkedin.com/in/guilherme-fidalgo/)  
[GitHub](https://github.com/guifidalgo)
