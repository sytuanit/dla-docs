# Backup e Restauração

## 1. Propósito

O módulo **Backup e Restauração** ajuda você a:
- Fazer backup de todos os dados do aplicativo em arquivo
- Restaurar dados do arquivo de backup
- Proteger dados contra perda devido a erros do dispositivo ou reinstalação do aplicativo

## 2. Quando Usar

Use este módulo quando você quiser:
- Fazer backup de dados antes de reinstalar o aplicativo
- Transferir dados para novo dispositivo
- Restaurar dados após perda de dados
- Criar backups periódicos

## 3. Telas Relacionadas

- Tela de backup
- Tela de restauração

## 4. Uso Principal

### 4.1 Fazer Backup de Dados

1. Vá para **Configurações** → **Backup e Dados** → **Backup**
2. Veja as informações:
   - Número de registros a serem copiados
   - Tamanho esperado do arquivo
3. Toque em **Backup**
4. Selecione o local de salvamento (Sistema de arquivos)
5. O arquivo de backup será criado com o nome: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Salve este arquivo em um local seguro (nuvem, computador, etc.)

### 4.2 Restaurar Dados

1. Vá para **Configurações** → **Backup e Dados** → **Restaurar**
2. Selecione o arquivo de backup do sistema de arquivos
3. Veja as informações do arquivo:
   - Data de criação do backup
   - Número de registros
   - Tamanho do arquivo
4. **Aviso**: A restauração substituirá todos os dados atuais
5. Toque em **Restaurar**
6. Confirme a restauração
7. Aguarde o processo de restauração ser concluído
8. O aplicativo será recarregado automaticamente

## 5. Ilustrações de UI (Wireframe)

### 5.1 Tela de Backup

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Fazer Backup de Dados      │
├─────────────────────────────────────────┤
│  Informações de Backup                   │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Número de Registros                │ │
│  │ 1.234 registros                    │ │
│  │                                    │ │
│  │ Tamanho Esperado                   │ │
│  │ ~2,5 MB                            │ │
│  │                                    │ │
│  │ Dados a serem copiados:            │ │
│  │ • Renda Recorrente                 │ │
│  │ • Despesas Recorrentes             │ │
│  │ • Despesas Diárias                 │ │
│  │ • Orçamento                        │ │
│  │ • Poupança                         │ │
│  │ • Empréstimos                      │ │
│  │ • Ocasiões Especiais               │ │
│  │ • Categorias                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Backup]                               │
└─────────────────────────────────────────┘
```

### 5.2 Tela de Restauração

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Restaurar Dados             │
├─────────────────────────────────────────┤
│  Selecionar Arquivo de Backup            │
│                                         │
│  [Selecionar Arquivo...]                │
│                                         │
│  Informações do Arquivo                  │
│  ┌───────────────────────────────────┐ │
│  │ Arquivo: dla-backup-2024-11-15.json│ │
│  │                                    │ │
│  │ Criado: 15/11/2024 10:30          │ │
│  │                                    │ │
│  │ Número de Registros: 1.234        │ │
│  │                                    │ │
│  │ Tamanho: 2,5 MB                    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Aviso                               │
│  A restauração substituirá todos os    │
│  dados atuais. Tem certeza?            │
│                                         │
│  [Restaurar] [Cancelar]                │
└─────────────────────────────────────────┘
```

## 6. Lógica e Regras

### 6.1 Formato do Arquivo de Backup

- O arquivo de backup está em formato JSON
- Nome do arquivo: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Contém todos os dados: usuários, categorias, transações, orçamentos, etc.

### 6.2 Dados Copiados

- Todas as tabelas no banco de dados
- Inclui dados do sistema e dados do usuário
- Não inclui: configurações do aplicativo, preferências (idioma, moeda)

### 6.3 Restauração

- A restauração excluirá todos os dados atuais
- Em seguida, importará dados do arquivo de backup
- O aplicativo será recarregado automaticamente após a conclusão da restauração

### 6.4 Validação

- O aplicativo verifica o formato do arquivo antes de restaurar
- Verifica compatibilidade de versão (se houver)
- Exibe erro se o arquivo for inválido

## 7. Notas Importantes

- **Fazer Backup Regularmente**: Deve fazer backup periodicamente (semanal ou mensal)
- **Salvar em Múltiplos Locais**: Salve o arquivo de backup em múltiplos locais (nuvem, computador, USB)
- **Restaurar Perderá Dados Atuais**: Certifique-se de ter feito backup dos dados atuais antes de restaurar
- **Não Pode Desfazer**: Após a restauração, não pode desfazer

