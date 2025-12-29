# Poupança

## 1. Propósito

O módulo **Poupança** ajuda você a gerenciar contas de poupança bancárias, rastrear saldos, taxas de juros e prazos. Este módulo suporta:
- Gerenciar múltiplas contas de poupança
- Rastrear taxas de juros e prazos
- Calcular automaticamente juros no vencimento
- Saque antecipado (se necessário)
- Renovação de conta

## 2. Quando Usar

Use este módulo quando você tiver:
- Contas de poupança bancárias
- Necessidade de rastrear saldos e taxas de juros
- Desejo de lembretes no vencimento
- Necessidade de gerenciar múltiplas contas de poupança

## 3. Telas Relacionadas

- Lista de contas de poupança
- Adicionar nova conta
- Editar conta
- Detalhes da conta
- Saque antecipado

## 4. Uso Principal

### 4.1 Criar Nova Conta de Poupança

1. Vá para **Funções** → Selecione **Poupança Bancária**
2. Toque no botão **+** (FAB) no canto inferior direito
3. Veja "Saldo Atual" (pode clicar para ver detalhes)
4. Selecione o banco:
   - Se existir: Selecione no menu suspenso
   - Se não: Toque no botão "+" para criar novo banco
5. Digite o valor do depósito (deve ser ≤ Saldo Atual)
6. Digite o prazo: 1-36 meses
7. Digite a taxa de juros: %/ano (1-100%)
8. Selecione a data de início (padrão é hoje, pode selecionar do mês anterior até o presente)
9. Veja a data de vencimento calculada automaticamente (da data de início + prazo)
10. Selecione o plano no vencimento:
    - Sacar principal e juros (padrão)
    - Renovar PRINCIPAL (juros para conta)
    - Renovar PRINCIPAL + JUROS
11. (Opcional) Digite nota
12. (Opcional) Selecione horários de notificação (padrão: 10:00 e 19:00)
13. Toque em **CRIAR CONTA**

### 4.2 Ver Lista e Detalhes da Conta

1. Vá para **Funções** → Selecione **Poupança Bancária**
2. Veja a tela "Lista de Contas de Poupança" com filtro padrão "Ativo"
3. Veja o card de visão geral:
   - Filtro "Ativo": Saldo atual, Dinheiro em poupança, Juros esperados, Juros deste mês
   - Filtro "Concluído": Total sacado, Juros recebidos
4. (Opcional) Use a barra de pesquisa para encontrar contas por nome ou código do banco
5. Alterne o filtro entre "Ativo" e "Concluído"
6. Toque em uma conta de poupança para ver detalhes:
   - Informações da conta: Banco, Prazo, Taxa de juros, Valor do depósito, Juros estimados
   - Data de início e data de vencimento
   - Status: Ativo
   - Plano no vencimento
   - (Se existir) Histórico de renovação
   - Botão "SACAR" (se ativo)

### 4.3 Sacar Conta de Poupança

1. Vá para a lista de poupança, encontre a conta que atingiu ou passou da data de vencimento
2. Toque no botão **SACAR** no card (ou vá para detalhes e toque em "SACAR")
3. Veja o diálogo "SACAR CONTA DE POUPANÇA" com:
   - Informações da conta: Banco, Valor do depósito, Prazo, Taxa de juros
   - Data de saque (padrão = data de vencimento, pode selecionar data diferente)
   - Juros recebidos (padrão = juros estimados, pode editar)
   - Total recebido (calculado automaticamente = principal + juros)
4. (Opcional) Edite a data de saque ou juros recebidos
5. Toque em **CONFIRMAR**

### 4.4 Renovar Conta de Poupança

1. Vá para a lista de poupança, encontre a conta que atingiu a data de vencimento com plano "Renovar PRINCIPAL" ou "Renovar PRINCIPAL + JUROS"
2. Toque no botão **RENOVAR** ou "Renovar conforme planejado"
3. Veja o diálogo "RENOVAR CONTA DE POUPANÇA" com:
   - Informações da conta: Banco, Valor do principal, Prazo, Taxa de juros
   - Juros recebidos (se renovar PRINCIPAL, juros vão para conta)
4. (Opcional) Edite a nova taxa de juros ou novo prazo (padrão = prazo antigo)
5. Toque em **CONFIRMAR RENOVAÇÃO**

### 4.5 Editar Conta de Poupança

1. Vá para os detalhes da conta de poupança ativa
2. Toque no botão **Editar** no canto superior direito
3. Edite as informações:
   - Banco (se necessário)
   - Valor do depósito (se aumentar, deve ser ≤ Saldo Atual)
   - Prazo, Taxa de juros
   - Data de início (se necessário)
   - Plano no vencimento
   - Nota, Horários de notificação
4. Veja a data de vencimento recalculada automaticamente (se prazo/data de início mudar)
5. Toque em **SALVAR ALTERAÇÕES**

### 4.6 Criar Novo Banco

1. Na tela "Adicionar Conta de Poupança" ou "Editar Conta de Poupança"
2. Toque no campo "Banco"
3. Toque no botão "+" ao lado do menu suspenso para criar novo banco
4. Veja o diálogo "ADICIONAR NOVO BANCO"
5. Digite o nome do banco
6. Digite o código do banco (máx. 3-4 caracteres, maiúsculas automáticas)
7. Selecione a cor do ícone (do seletor de cores ou paleta)
8. Veja a visualização do ícone
9. Toque em **CRIAR**

## 5. Exemplos e Ilustrações de UI

### SAVINGS-01: Criar Nova Conta de Poupança

**Objetivo**: Criar uma nova conta de poupança para rastrear depósito bancário, taxa de juros e data de vencimento.

**Passos Principais**:
1. Vá para Funções → Poupança Bancária
2. Toque no botão "+" (FAB)
3. Selecione o banco (ou crie novo)
4. Digite o valor do depósito, prazo, taxa de juros
5. Selecione a data de início (padrão hoje)
6. Selecione o plano no vencimento
7. (Opcional) Digite nota e horários de notificação
8. Toque em "CRIAR CONTA"

---

### SAVINGS-02: Sacar Conta de Poupança

**Objetivo**: Sacar conta de poupança quando atingir a data de vencimento para receber principal e juros.

**Passos Principais**:
1. Vá para a lista de poupança, encontre a conta que atingiu ou passou da data de vencimento
2. Toque no botão "SACAR"
3. Veja o diálogo com informações da conta, data de saque, juros recebidos
4. (Opcional) Edite a data de saque ou juros recebidos
5. Toque em "CONFIRMAR"

---

### SAVINGS-03: Ver Lista e Detalhes da Conta

**Objetivo**: Ver visão geral de contas de poupança ativas e concluídas, bem como detalhes de cada conta.

**Passos Principais**:
1. Vá para Funções → Poupança Bancária
2. Veja o card de visão geral por filtro
3. Use a barra de pesquisa (opcional)
4. Alterne o filtro entre "Ativo" e "Concluído"
5. Toque na conta para ver detalhes

---

### SAVINGS-04: Renovar Conta de Poupança

**Objetivo**: Renovar conta de poupança conforme planejado quando atingir a data de vencimento.

**Passos Principais**:
1. Encontre a conta que atingiu a data de vencimento com plano "Renovar PRINCIPAL" ou "Renovar PRINCIPAL + JUROS"
2. Toque no botão "RENOVAR"
3. Veja o diálogo com informações da conta e juros recebidos
4. (Opcional) Edite a nova taxa de juros ou novo prazo
5. Toque em "CONFIRMAR RENOVAÇÃO"

**Resultado**: A conta antiga é atualizada, nova conta é criada com rootSavingId vinculado à conta antiga. Se renovar PRINCIPAL, juros são adicionados ao saldo atual. Se renovar PRINCIPAL + JUROS, tanto principal quanto juros são renovados.

---

### SAVINGS-05: Criar Novo Banco

**Objetivo**: Criar um novo banco para usar ao criar contas de poupança.

**Passos Principais**:
1. Na tela "Adicionar Conta de Poupança" ou "Editar Conta de Poupança"
2. Toque no botão "+" ao lado do menu suspenso "Banco"
3. Digite o nome do banco, código do banco
4. Selecione a cor do ícone
5. Veja a visualização do ícone
6. Toque em "CRIAR"

---

### SAVINGS-06: Editar Conta de Poupança

**Objetivo**: Editar informações da conta de poupança ativa (banco, valor, prazo, taxa de juros, plano de vencimento).

**Passos Principais**:
1. Vá para os detalhes da conta de poupança ativa
2. Toque no botão "Editar"
3. Edite as informações necessárias
4. Veja a data de vencimento recalculada automaticamente (se prazo/data de início mudar)
5. Toque em "SALVAR ALTERAÇÕES"

**Resultado**: As informações da conta são atualizadas, os juros estimados são recalculados com base na nova taxa de juros. Se o valor mudar, o saldo atual é ajustado adequadamente.

## 6. Lógica e Regras

### 6.1 Cálculo de Juros

- Os juros são calculados pela fórmula: `Valor × Taxa de Juros × (Prazo / 12)`
- Os juros são calculados no vencimento ou ao sacar antecipadamente

### 6.2 Status

- **Ativo (ACTIVE)**: A conta de poupança está ativa, não atingiu a data de vencimento ou não foi processada
- **Concluído (COMPLETED)**: A conta foi sacada
- **Renovado (ROLLED_OVER)**: A conta foi renovada, nova conta criada

### 6.3 Saque e Renovação

- **Saque**: Ao sacar, principal + juros são adicionados ao saldo atual, cria automaticamente "Renda Extra" com categoria "Juros de Poupança"
- **Saque Antecipado**: Pode sacar antes da data de vencimento, juros recebidos podem ser menores que juros estimados
- **Renovar PRINCIPAL**: Juros são adicionados ao saldo atual, principal é renovado com novo prazo
- **Renovar PRINCIPAL + JUROS**: Tanto principal quanto juros são renovados, saldo atual não muda
- **Histórico de Renovação**: Renovações são salvas e exibidas nos detalhes da conta, vinculadas via `rootSavingId`

### 6.4 Notificações

- O aplicativo envia notificação de lembrete quando a data de vencimento chega
- O horário da notificação pode ser configurado para cada conta (`notificationTime1`, `notificationTime2`, padrão 10:00 e 19:00)

## 7. Notas Importantes

- **Módulo Premium Necessário**: Este recurso é apenas para usuários Premium
- **Taxa de Juros**: Digite a taxa de juros por ano (%/ano), de 1 a 100%
- **Prazo**: Calculado em meses, de 1 a 36 meses
- **Data de Vencimento**: Calculada automaticamente da data de início + prazo
- **Valor do Depósito**: Deve ser ≤ Saldo Atual, ao criar conta subtrai automaticamente do saldo atual
- **Data de Início**: Pode selecionar apenas do início do mês anterior até o presente
- **Notificações**: Notificações são enviadas na data de vencimento em 2 horários (padrão 10:00 e 19:00), podem ser personalizadas para cada conta
- **Badge "Vencendo em Breve"**: Mostrado quando ≤ 7 dias até a data de vencimento
- **Badge "Vencido"**: Mostrado quando a data de vencimento chegou
- **Excluir Conta**: Ao excluir conta ativa, o valor do principal é adicionado de volta ao saldo atual. Excluir conta raiz excluirá toda a cadeia de renovação
- **Card de Visão Geral**: Muda por filtro, exibe informações agregadas para contas ativas ou concluídas

