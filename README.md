 # Plataforma de Automação de Contratos


 # ♠  Descrição do Projeto
 
**Este sistema foi desenvolvido para automatizar o fluxo completo de contratação, desde a coleta de informações iniciais até a geração do contrato final. O foco principal é a otimização de tempo e a redução de erros operacionais, tanto para o usuário quanto para a parte contratada.**

O sistema processa dados dinâmicos, integra pré-requisitos informados no momento do preenchimento e gera documentos prontos para assinatura, garantindo agilidade e conformidade.

-----------------------------------------------------------------------------------------------------------------------------------------------------

• Funcionalidades Principais

Automação de Documentos: Geração automática de contratos personalizados com base nos dados de entrada.

Integração de Dados: Processamento inteligente que une informações do usuário com os requisitos contratuais em tempo real.

Banco de Dados Exclusivo: Armazenamento centralizado e seguro de dados sobre contratantes, permitindo maior controle, consulta rápida e histórico de processos.

Otimização de Processos: Redução significativa no tempo de redação e validação de documentos contratuais.

-----------------------------------------------------------------------------------------------------------------------------------------------------

•Tecnologias Utilizadas:

Backend API: FastAPI com servidor Uvicorn para alta performance.

Gerenciamento de Dados: SQLModel para modelagem robusta de banco de dados e persistência.

Banco de Dados: PostgreSQL (via psycopg2-binary).

Geração de Documentos: Jinja2 para templating e WeasyPrint para exportação em PDF.

Segurança: Gerenciamento de configuração via python-dotenv.

-----------------------------------------------------------------------------------------------------------------------------------------------------


 # Sobre o Desenvolvimento
 
Este projeto foi arquitetado como uma aplicação back-end escalável, utilizando FastAPI para comunicação de alta performance. A gestão de dados é centralizada via SQLModel com persistência em PostgreSQL, garantindo integridade e segurança. O sistema conta com uma camada de processamento para geração dinâmica de documentos em PDF, seguindo boas práticas de segurança de variáveis de ambiente.
