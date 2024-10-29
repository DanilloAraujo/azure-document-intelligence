# Aplicação de análise de imagem de cartão de crédito utilizando Azure Document Intelligences

Este é um projeto que dado uma imagem de cartão de crédito é verificado se as informações realmente refere-se a um cartão.

## Funcionalidades

- **Carregamento de Imagem**: Suporta upload de arquivos `.png, .jpg, .jpeg`.
- **Análise de Imagem**: Análisa imagem identificanco se é um cartão de crédito.

## Requisitos

- Python 3.7+
- Conta do **Azure Cognitive Services** com a API Document Intelligences configurada
- Blob Storage configurado no Azure.
- Jupyter Notebook
- Pacotes Python:
  - `azure.core`
  - `azure-ai-documentintelligence`
  - `streamlit`
  -  `azure-storage-blob`
  -  `python-dotenv`

1. Clone este repositório:
   ```bash
   git clone https://github.com/DanilloAraujo/azure-document-intelligence.git
