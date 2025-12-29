# Configurações

## 1. Propósito

O módulo **Configurações** permite que você configure o aplicativo de acordo com suas necessidades pessoais, incluindo:
- Idioma e moeda
- Notificações
- Categorias
- Backup e restauração de dados
- Segurança (senha, Face ID)

## 2. Quando Usar

Use este módulo quando você quiser:
- Alterar idioma ou moeda
- Ativar/desativar notificações
- Gerenciar categorias (adicionar, editar, excluir, definir padrão)
- Fazer backup ou restaurar dados
- Alterar senha ou ativar Face ID

## 3. Telas Relacionadas

- Tela principal de configurações
- Configurações básicas
- Selecionar idioma
- Selecionar moeda
- Gerenciar categorias
- Fazer backup de dados
- Restaurar dados
- Alterar senha
- Ativar Face ID / Impressão Digital

## 4. Uso Principal

### 4.1 Alterar Idioma

1. Vá para **Configurações** → **Exibição e Idioma** → **Idioma**
2. Selecione o idioma desejado
3. O aplicativo será recarregado automaticamente com o novo idioma

### 4.2 Alterar Moeda

1. Vá para **Configurações** → **Exibição e Idioma** → **Moeda**
2. Selecione o tipo de moeda
3. Todos os valores serão exibidos na nova unidade

### 4.3 Ativar/Desativar Notificações

1. Vá para **Configurações** → **Notificações**
2. Alterne o interruptor **Notificações**
3. Se ativado, você receberá lembretes sobre:
   - Renda recorrente devida
   - Despesas recorrentes devidas
   - Contas de poupança vencendo
   - Ocasiões especiais chegando

### 4.4 Gerenciar Categorias

1. Vá para **Configurações** → **Categorias**
2. Selecione o tipo de categoria para gerenciar:
   - Renda Recorrente
   - Renda Extra
   - Despesas Recorrentes
   - Despesas Diárias
3. Adicionar/Editar/Excluir categorias
4. Definir categoria padrão (para despesas diárias)

### 4.5 Fazer Backup de Dados

1. Vá para **Configurações** → **Backup e Dados** → **Backup**
2. Selecione o local de salvamento (Sistema de arquivos)
3. Toque em **Backup**
4. O arquivo de backup será criado

### 4.6 Restaurar Dados

1. Vá para **Configurações** → **Backup e Dados** → **Restaurar**
2. Selecione o arquivo de backup
3. Confirme a restauração
4. **Nota**: A restauração substituirá todos os dados atuais

## 5. Ilustrações de UI (Wireframe)

### 5.1 Tela Principal de Configurações

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Configurações              │
├─────────────────────────────────────────┤
│  Exibição e Idioma                       │
│  ┌───────────────────────────────────┐ │
│  │ Idioma                             │ │
│  │ Português                    →     │ │
│  │                                    │ │
│  │ Moeda                              │ │
│  │ EUR (€)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notificações                            │
│  ┌───────────────────────────────────┐ │
│  │ Notificações                [LIGADO]│ │
│  └───────────────────────────────────┘ │
│                                         │
│  Backup e Dados                          │
│  ┌───────────────────────────────────┐ │
│  │ Backup                        →    │ │
│  │                                    │ │
│  │ Restaurar                     →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Categorias                              │
│  ┌───────────────────────────────────┐ │
│  │ Gerenciar Categorias           →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Segurança                              │
│  ┌───────────────────────────────────┐ │
│  │ Senha                         →    │ │
│  │                                    │ │
│  │ Face ID / Impressão Digital    →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Lógica e Regras

### 6.1 Idioma

- Suportado: Inglês, Português, Tiếng Việt, 日本語
- Alterar o idioma recarregará todo o aplicativo
- As categorias do sistema serão automaticamente traduzidas para o novo idioma

### 6.2 Moeda

- Cada idioma tem uma moeda padrão (ex.: EUR para Português)
- Você pode selecionar uma moeda diferente
- Todos os valores serão formatados de acordo com a moeda selecionada

### 6.3 Notificações

- As notificações só funcionam quando o aplicativo tem permissão
- O horário da notificação depende de cada função e pode ser configurado:
  - Renda/Despesas Recorrentes: `notificationTime1`, `notificationTime2` (padrão 16:00 e 19:00)
  - Contas de Poupança e Empréstimos: `notificationTime1`, `notificationTime2` (padrão 10:00 e 19:00)
  - Ocasiões Especiais e Etapas de Preparação: de acordo com `reminderTime` que você inserir
  - Pode desativar notificações para cada tipo separadamente (no futuro)

### 6.4 Categorias

- As categorias do sistema não podem ser excluídas, apenas desativadas
- As categorias do usuário podem ser excluídas (se não estiverem em uso)
- Cada tipo de categoria é independente (renda recorrente, despesas diárias, etc.)

## 7. Notas Importantes

- **Fazer Backup Regularmente**: Deve fazer backup dos dados periodicamente para evitar perda de dados
- **Restaurar Substituirá**: A restauração substituirá todos os dados atuais
- **Senha**: Se você esquecer a senha, pode redefinir (excluirá os dados)

