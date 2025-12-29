# Empréstimos Bancários

## 1. Propósito

O módulo **Empréstimos Bancários** ajuda você a gerenciar empréstimos bancários, incluindo:
- Rastrear valor do empréstimo, taxa de juros, prazo
- Gerenciar cronograma de pagamento
- Calcular juros por período (se aplicável)
- Gerenciar multas por atraso
- Liquidação antecipada (se necessário)

## 2. Quando Usar

Use este módulo quando você tiver:
- Empréstimos bancários
- Necessidade de rastrear cronograma de pagamento
- Desejo de calcular juros e multas
- Necessidade de lembretes quando o pagamento está devido

## 3. Telas Relacionadas

- Lista de empréstimos
- Adicionar novo empréstimo (4 etapas)
- Editar empréstimo
- Detalhes do empréstimo e cronograma de pagamento
- Liquidação antecipada

## 4. Uso Principal

### 4.1 Adicionar Novo Empréstimo (4 Etapas)

#### Etapa 1: Informações Básicas

1. Vá para **Funções** → Selecione **Empréstimos Bancários**
2. Toque no botão **+** (FAB)
3. Preencha as informações:
   - **Banco**: Selecione ou crie novo banco
   - **Nome do Empréstimo**: (ex.: "Empréstimo Imobiliário")
   - **Valor do Empréstimo**: Valor principal
   - **Data de Desembolso**: Data em que o dinheiro foi recebido
   - **Prazo**: Número de anos
   - **Tipo de Juros**: Taxa promocional/flutuante ou Taxa fixa
4. Toque em **Próximo**

#### Etapa 2: Configurar Taxa de Juros

**Se selecionar "Taxa Promocional/Flutuante":**
- Ative **Tem Taxa Promocional** (se aplicável)
- Digite **Meses Promocionais** e **Taxa Promocional**
- Adicione períodos de taxa flutuante:
  - Selecione ano e intervalo de meses
  - Digite a taxa de juros (%/ano)
  - Selecione **Flutuante** ou **Fixo**

**Se selecionar "Taxa Fixa":**
- Digite **Taxa Fixa** (%/ano)

Toque em **Próximo**

#### Etapa 3: Configurar Multas

1. Ative **Tem Multa por Atraso** (se aplicável)
2. Adicione períodos de multa:
   - Selecione ano e intervalo de meses
   - Digite **Taxa de Multa** (%/ano)
3. Toque em **Próximo**

#### Etapa 4: Confirmar e Salvar

1. Revise as informações:
   - Valor total a pagar
   - Cronograma de pagamento esperado
2. Toque em **Salvar**

### 4.2 Ver Detalhes do Empréstimo

1. Vá para a lista de empréstimos
2. Toque em um empréstimo
3. Veja as informações:
   - Informações básicas
   - Cronograma de pagamento
   - Valor pago / Restante
   - Taxa de juros e multas

### 4.3 Marcar Período de Pagamento como Pago

1. Vá para os detalhes do empréstimo
2. Encontre o período de pagamento devido (badge "Não Pago")
3. Toque em **Marcar como Pago**
4. Preencha as informações:
   - **Data Real de Pagamento**: Data paga (padrão = hoje)
   - **Juros Reais Pagos**: Juros reais pagos (padrão = juros planejados)
   - **Nota**: (opcional)
5. Veja **Pagamento Real Total** calculado automaticamente (principal + juros reais)
6. Toque em **Confirmar**

### 4.4 Atualizar Taxa de Juros Atual

1. Vá para os detalhes do empréstimo (apenas mostrado se atualmente em período de taxa flutuante)
2. Toque em **Atualizar Taxa de Juros Atual**
3. Preencha as informações:
   - **Nova Taxa de Juros**: Nova taxa de juros (%/ano)
   - **Data Efetiva**: Data para começar a aplicar nova taxa (padrão = início do período atual)
   - **Nota**: (opcional)
4. Toque em **Salvar**
5. Períodos não pagos do período atual em diante serão atualizados com a nova taxa de juros

### 4.5 Liquidação Antecipada

1. Vá para os detalhes do empréstimo
2. Toque em **Calcular Valor de Liquidação**
3. **Etapa 1 - Digite Informações de Pagamento Antecipado:**
   - Selecione o método: **Pagamento Parcial** ou **Liquidação Total**
   - Selecione a data de pagamento antecipado (padrão = hoje)
   - Digite o valor do pagamento antecipado (se parcial)
   - Veja **Multa por Pagamento Antecipado** calculada automaticamente
4. Toque em **Próximo**
5. **Etapa 2 - Compare Opções:**
   - Veja comparação entre "Sem Pagamento Antecipado" e "Pagamento Antecipado"
   - Veja resultados: Economia de juros, redução de tempo
6. Toque em **Confirmar Pagamento Antecipado**

### 4.6 Editar Empréstimo

1. Vá para os detalhes do empréstimo
2. Toque em **Editar** (apenas editar nome, nota, banco)
3. Edite as informações editáveis:
   - **Nome do Empréstimo**: Pode editar
   - **Banco**: Pode alterar
   - **Nota**: Pode editar
   - **Valor do Empréstimo, Data de Desembolso, Prazo, Taxa de Juros**: Só pode editar se nenhum pagamento foi feito ainda
4. Toque em **Salvar**

## 5. Exemplos e Ilustrações de UI

### LOAN-01: Criar Novo Empréstimo (Empréstimo Imobiliário com Taxa de Juros Promocional)

**Objetivo**: Criar um novo empréstimo para rastrear um empréstimo imobiliário, taxa de juros promocional e cronograma de pagamento mensal.

**Passos**:
1. Vá para **Funções** → Selecione **Empréstimos Bancários**
2. Toque no botão **+** (FAB) para adicionar novo empréstimo
3. **Etapa 1 - Informações Básicas:**
   - Selecione banco: Banco de Portugal
   - Digite nome: "Empréstimo Imobiliário - Apartamento Centro"
   - Digite valor do empréstimo: €180.000
   - Selecione data de desembolso: 01/04/2023
   - Digite prazo: 10 anos (calculado automaticamente = 120 períodos)
   - Selecione horários de notificação: 10:00 e 19:00
   - Selecione tipo de juros: "Saldo Devedor"
   - Toque em **Próximo**
4. **Etapa 2 - Configurar Taxa de Juros:**
   - Ative "Tem Período de Juros Promocional"
   - Digite: Primeiros 6 meses @ 5,4%/ano
   - Adicione períodos subsequentes:
     - Ano 1 (meses 7-12): 8,1%/ano, flutuante
     - Ano 2 (meses 13-24): 8,6%/ano, flutuante
     - Ano 3 em diante: 9,0%/ano, flutuante
   - Toque em **Próximo**
5. **Etapa 3 - Configurar Multa por Pagamento Antecipado:**
   - Ative "Aplicar Multa por Pagamento Antecipado"
   - Digite multas: Anos 1-3: 1,8%, Anos 4-5: 1,4%, Ano 6+: 0,9%
   - Toque em **Próximo**
6. **Etapa 4 - Confirmar:**
   - Revise as informações resumidas
   - Toque em **Criar Empréstimo**

**Resultado**: Empréstimo criado com sucesso, cronograma de pagamento de 120 períodos criado automaticamente, notificações agendadas.

---

### LOAN-02: Ver Lista e Detalhes do Empréstimo

**Objetivo**: Ver visão geral dos empréstimos, filtrar por status, pesquisar e ver detalhes de cada empréstimo.

**Passos**:
1. Vá para **Funções** → Selecione **Empréstimos Bancários**
2. Veja a tela de lista com filtros "Ativo" (padrão) e "Concluído"
3. Alterne entre filtros para ver diferentes visões gerais
4. Use a barra de pesquisa: Digite "Centro"
5. Toque no empréstimo para ver detalhes
6. Veja o cronograma de pagamento com períodos pagos, período atual e períodos futuros
7. Use a barra de pesquisa no cronograma de pagamento: Digite "9/2024"

**Resultado**: A lista exibe corretamente por filtro, os detalhes do empréstimo mostram todas as informações e o cronograma de pagamento.

---

### LOAN-03: Marcar Período de Pagamento como Pago (Registrar Pagamento)

**Objetivo**: Marcar um período de pagamento como "Pago" após fazer o pagamento ao banco.

**Passos**:
1. Vá para os detalhes do empréstimo
2. Encontre o período atual (Período 9) com badge "Não Pago"
3. Toque em **Marcar como Pago**
4. Preencha as informações:
   - Data real de pagamento: 15/01/2024 (padrão = hoje)
   - Juros reais pagos: €1.035 (padrão = juros planejados)
   - Nota: (opcional)
5. Veja o pagamento real total calculado automaticamente
6. Toque em **Confirmar**

**Resultado**: Período 9 atualizado para "Pago", saldo diminui, períodos pagos aumentam, saldo atual diminui.

---

### LOAN-04: Atualizar Taxa de Juros Atual (Quando Banco Ajusta Taxa Flutuante)

**Objetivo**: Atualizar nova taxa de juros quando o banco anuncia ajuste de taxa flutuante.

**Passos**:
1. Vá para os detalhes do empréstimo
2. Veja "Taxa de Juros Atual: 8,1%/ano"
3. Toque em **Atualizar Taxa de Juros Atual** (apenas mostrado se atualmente em período de taxa flutuante)
4. Preencha as informações:
   - Nova taxa de juros: 9,5%/ano
   - Data efetiva: 15/01/2024 (padrão = início do período atual)
   - Nota: "Banco ajustou taxa de juros conforme nova decisão"
5. Toque em **Salvar**

**Resultado**: Taxa de juros atual atualizada, períodos não pagos do período atual em diante atualizados com a nova taxa de juros.

---

### LOAN-05: Liquidação Antecipada (Pagamento Parcial para Reduzir Juros)

**Objetivo**: Liquidar parte do empréstimo antecipadamente para reduzir o total de juros a pagar e encurtar o prazo do empréstimo.

**Passos**:
1. Vá para os detalhes do empréstimo
2. Toque em **Calcular Valor de Liquidação**
3. **Etapa 1 - Digite Informações de Pagamento Antecipado:**
   - Selecione o método: "Pagamento Parcial"
   - Selecione data de pagamento antecipado: 15/01/2024
   - Digite valor do pagamento antecipado: €72.000
   - Veja multa calculada automaticamente: €1.296 (1,8%)
   - Toque em **Próximo**
4. **Etapa 2 - Compare Opções:**
   - Veja comparação entre "Sem Pagamento Antecipado" e "Pagamento Antecipado €72.000"
   - Veja resultados: Economize €27.000 em juros, reduza 40 períodos
   - Toque em **Confirmar Pagamento Antecipado**

**Resultado**: Saldo diminui, cronograma de pagamento recalculado, número de períodos diminui, data de término mais cedo.

---

### LOAN-06: Editar Empréstimo (Editar Informações Básicas)

**Objetivo**: Editar informações básicas do empréstimo (nome, banco, nota) após iniciar pagamentos.

**Passos**:
1. Vá para os detalhes do empréstimo
2. Toque em **Editar** (apenas editar nome, nota, banco)
3. Edite:
   - Nome do Empréstimo: "Empréstimo Imobiliário - Apartamento Centro - Unidade A1-1201"
   - (Opcional) Altere banco: Banco Santander
   - Nota: "Transferido para novo banco"
4. Veja campos desabilitados: Valor do Empréstimo, Data de Desembolso, Prazo, Taxa de Juros
5. Toque em **Salvar**

**Resultado**: Informações básicas atualizadas, outras informações inalteradas.

**Nota**: Se o empréstimo não tiver pagamentos feitos ainda, pode editar todas as informações (valor, prazo, configuração de juros).

## 6. Lógica e Regras

### 6.1 Taxa Promocional/Flutuante

- Pode ter período promocional (taxa de juros menor)
- Após período promocional, taxa de juros flutua por período
- Cada período pode ser **Flutuante** (baseado no mercado) ou **Fixo**

### 6.2 Multas por Atraso

- Multas calculadas por %/ano
- Pode configurar diferentemente para cada período
- Multas só se aplicam quando o pagamento está atrasado

### 6.3 Cronograma de Pagamento

- O aplicativo cria automaticamente o cronograma de pagamento com base em:
  - Valor do empréstimo
  - Taxa de juros
  - Prazo
- Cada período de pagamento inclui: Principal + Juros

### 6.4 Liquidação Antecipada

- Calcular valor restante (principal + juros + multas se houver)
- Após liquidação, o empréstimo mudará para status "Concluído"

### 6.5 Notificações

- O aplicativo envia notificação de lembrete quando o pagamento está devido
- O horário da notificação pode ser configurado para cada empréstimo (`notificationTime1`, `notificationTime2`, padrão 10:00 e 19:00)

## 7. Notas Importantes

- **Taxas de Juros Complexas**: Este módulo suporta taxas de juros que mudam por período, requer configuração cuidadosa
- **Não pode excluir quando cronograma de pagamento existe**: Se o cronograma de pagamento existir, você só pode liquidar, não pode excluir
- **Liquidação Antecipada**: Pode exigir taxas de multa adicionais, depende da política do banco
- **Cronograma de Pagamento**: O cronograma de pagamento é calculado automaticamente, você não pode editar diretamente

