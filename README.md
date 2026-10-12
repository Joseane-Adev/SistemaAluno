# 📚 Sistema de Gestão Escolar - em andamento

Projeto desenvolvido em **Django** para gerenciamento de alunos em uma instituição escolar.  
O sistema permite cadastrar,visualizar e alterar informações dos estudantes.

## 🚀 Funcionalidades

### 👩‍🎓 Cadastro de Alunos
- Registro de informações básicas: nome, data de nascimento, endereço, telefone, e-mail.
- Campo **Data da matrícula** com seleção via calendário (`DateField`).
- Validação de datas no formato brasileiro (`dd/mm/yyyy`) e compatibilidade com o formato padrão HTML (`yyyy-mm-dd`).
- Atualização de cadastros existentes.
- Validações para campos inseridos no cadastro.

### 🖥️ Formulários
- Formulário customizado com `forms.DateField` e `input_formats` para aceitar múltiplos formatos de data.
- Interface amigável com calendário (`type="date"`).
- Mensagens de erro claras em caso de data inválida.

### ⚙️ Tecnologias Utilizadas
- **Python 3.x**
- **Django**
- **SQLite** (banco de dados padrão)
- **HTML5 / CSS3** para os formulários não foram criados por mim, recorri a IA e fiz algumas modificações de acordo com o código e estilização.

### ⚙️ Melhorias
-Segurança de login
-Estilização da página de ficha do estudante.

