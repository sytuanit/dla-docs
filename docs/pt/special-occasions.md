# Ocasiões Especiais

## 1. Propósito

O módulo **Ocasiões Especiais** ajuda você a gerenciar ocasiões especiais ao longo do ano e se preparar para elas, incluindo:
- Gerenciar ocasiões especiais (aniversários, feriados, etc.)
- Criar listas de tarefas (etapas de preparação)
- Anexar listas de verificação a cada etapa de preparação
- Lembretes antes das ocasiões
- Rastrear progresso de preparação

## 2. Quando Usar

Use este módulo quando você quiser:
- Gerenciar ocasiões especiais ao longo do ano
- Se preparar para ocasiões importantes
- Criar listas de tarefas
- Receber lembretes antes das ocasiões

## 3. Telas Relacionadas

- Lista de ocasiões especiais
- Adicionar nova ocasião especial
- Detalhes da ocasião e etapas de preparação
- Adicionar etapa de preparação
- Selecionar lista de verificação
- Criar nova lista de verificação

## 4. Uso Principal

### 4.1 Adicionar Ocasião Especial

1. Vá para **Funções** → Selecione **Ocasiões Especiais**
2. Toque no botão **+** (FAB)
3. Preencha as informações:
   - **Nome da Ocasião**: (ex.: "Aniversário da Mãe")
   - **Data**: Selecione dia/mês (DatePicker seleciona apenas dia/mês, sem ano)
   - **Usar Calendário Lunar**: (Opcional) Marque se quiser usar calendário lunar
     - Se marcado: Digite dia e mês lunar, o aplicativo calcula automaticamente a data solar mais próxima
   - **Repetir**: Anual / Apenas Este Ano
   - **Mostrar Notificação Em**: Selecione horário (obrigatório, ex.: 07:00)
   - **Nota**: Informações adicionais (opcional)
4. (Opcional) Adicione etapas de preparação (veja 4.2)
5. Toque em **Salvar**

### 4.2 Adicionar Etapa de Preparação

1. Ao adicionar nova ocasião: Toque em **+ Adicionar Etapa** na seção "Etapas de Preparação"
2. Ou dos detalhes da ocasião: Toque em **+ Adicionar Etapa**
3. Preencha as informações:
   - **Quando?**: "X dias antes" ou "No dia"
   - **Número de Dias**: (se selecionar "X dias antes") Digite o número de dias antes da ocasião
   - **Mostrar Notificação Em**: Selecione horário (obrigatório)
   - **Repetir Diariamente Até Concluído**: (Opcional) Marque se quiser lembretes diários
   - **Conteúdo**: Nome da etapa (obrigatório, ex.: "Comprar Presente")
   - **Nota**: (Opcional)
   - **Usar Lista de Verificação**: (Opcional) Marque para vincular com lista de compras
4. Toque em **Adicionar** (ou FAB "Aplicar")

### 4.3 Criar Lista de Verificação

1. Ao adicionar etapa de preparação, marque **Usar Lista de Verificação**
2. A tela "Selecionar Lista de Compras" abre automaticamente
3. Toque no FAB **+** para criar nova lista de verificação
4. Digite o nome da lista de verificação
5. Adicione itens:
   - Digite o nome do item
   - Toque em **+** para adicionar novo item
6. Toque em **Salvar**
7. A nova lista de verificação é automaticamente selecionada e retorna para a tela "Adicionar Etapa de Preparação"

### 4.4 Marcar Etapa como Concluída

1. Vá para os detalhes da ocasião especial
2. Encontre a etapa para marcar
3. Toque na caixa de seleção [ ] para mudar para [✓]
4. Se tiver lista de verificação, toque no nome da lista de verificação para ver e marcar/desmarcar itens

### 4.5 Ver Progresso

1. Vá para os detalhes da ocasião especial
2. Veja a seção "Visão Geral":
   - Etapas de Preparação: Número total de etapas
   - Concluídas: Número de etapas marcadas / Total de etapas
   - Status: Não Iniciado / Em Progresso / Concluído

### 4.6 Editar Ocasião Especial

1. Vá para os detalhes da ocasião especial
2. Toque no hiperlink **Editar ›** no cabeçalho
3. Edite as informações: Nome, data, repetir, horário do lembrete, nota
4. Toque em **Salvar**

### 4.7 Editar Etapa de Preparação

1. Vá para os detalhes da ocasião especial
2. Toque na etapa para editar (clique no item inteiro, exceto ícone Excluir)
3. Edite as informações: Horário, conteúdo, lista de verificação
4. Toque em **Aplicar** (ou FAB)

## 5. Exemplos e Ilustrações de UI

### OCCASION-01: Criar Nova Ocasião Especial (Aniversário com Etapas de Preparação)

**Objetivo**: Criar uma nova ocasião especial (aniversário) com etapas de preparação para que o aplicativo lembre automaticamente antes da ocasião ocorrer.

**Passos Principais**:
1. Vá para Funções → Ocasiões Especiais → Toque no botão "+" (FAB)
2. Digite o nome da ocasião, selecione data (01/05), selecione repetir "Anual", selecione horário do lembrete (07:00)
3. Adicione etapa de preparação 1: "7 dias antes – 08:00" - "Comprar Presente"
4. Adicione etapa de preparação 2: "1 dia antes – 19:00" - "Encomendar Bolo"
5. Toque em "Salvar"

---

### OCCASION-02: Criar Ocasião Especial Usando Calendário Lunar (Dia de Memória com Lista de Compras)

**Objetivo**: Criar uma ocasião especial usando calendário lunar (Dia de Memória) com etapas de preparação vinculadas à lista de compras para rastrear compra de oferendas.

**Passos Principais**:
1. Vá para Funções → Ocasiões Especiais → Toque no botão "+" (FAB)
2. Digite o nome da ocasião "Dia de Memória da Mãe", marque "Usar Calendário Lunar"
3. Digite data lunar: 15/11, o aplicativo calcula automaticamente data solar: 15/12/2025
4. Adicione 3 etapas de preparação, onde a etapa 2 tem vínculo de lista de verificação "comprar oferendas"
5. Toque em "Salvar"

---

### OCCASION-03: Ver Lista e Detalhes de Ocasiões Especiais

**Objetivo**: Ver visão geral de ocasiões especiais, filtrar por tempo e ver detalhes de cada ocasião com progresso de preparação.

**Passos Principais**:
1. Vá para Funções → Ocasiões Especiais
2. Veja a lista com filtro "Todas", "Próximas", "Este Mês"
3. Toque no card da ocasião para ver detalhes
4. Veja a visão geral: Número de etapas, Concluídas, Status
5. Marque etapa como concluída marcando a caixa de seleção

---

### OCCASION-04: Adicionar Etapa de Preparação com Lista de Compras

**Objetivo**: Adicionar nova etapa de preparação para ocasião especial e vincular com lista de compras para rastrear compras.

**Passos Principais**:
1. Vá para detalhes da ocasião especial → Toque em "+ Adicionar Etapa"
2. Selecione "Quando?": "X dias antes", digite número de dias: 1
3. Selecione horário do lembrete: 19:00
4. Ative "Repetir Diariamente Até Concluído"
5. Digite conteúdo: "Ir às compras para oferendas"
6. Marque "Usar Lista de Verificação" → Selecione lista de verificação "comprar oferendas"
7. Toque em "Adicionar"

---

### OCCASION-05: Marcar Etapa de Preparação como Concluída e Ver Progresso da Lista de Verificação

**Objetivo**: Marcar etapas de preparação como concluídas e rastrear progresso da lista de compras.

**Passos Principais**:
1. Vá para detalhes da ocasião especial
2. Veja etapa com lista de verificação mostrando progresso "Concluído 3 / 8 itens"
3. Toque no nome da lista de verificação para ver detalhes e marcar/desmarcar itens
4. Marque a caixa de seleção da etapa para marcar como concluída
5. Veja "Visão Geral" atualizar em tempo real

---

### OCCASION-06: Editar Ocasião Especial e Etapas de Preparação

**Objetivo**: Editar informações da ocasião especial e etapas de preparação após criação.

**Passos Principais**:
1. Vá para detalhes da ocasião especial → Toque em "Editar ›"
2. Edite o nome da ocasião, nota
3. Toque em "Salvar"
4. Toque na etapa para editar: Altere horário, conteúdo
5. Toque no ícone Excluir para excluir etapa (tem diálogo de confirmação)

## 6. Lógica e Regras

### 6.1 Datas do Calendário Lunar

- Você pode digitar datas do calendário solar e lunar
- O aplicativo calcula automaticamente a data solar correspondente à data lunar
- Suporta repetição anual por calendário lunar

### 6.2 Repetir

- **Anual**: A ocasião se repete todo ano (por calendário solar ou lunar)
  - Com calendário solar: Cada ano calcula nextOccurDate com base em (dia/mês) de solarDate
  - Com calendário lunar: Cada ano converte da data lunar para a data solar correspondente e atualiza nextOccurDate
- **Apenas Este Ano**: A ocasião é válida apenas no ano atual, não se repete no próximo ano

### 6.3 Etapas de Preparação

- **Quando?**: Tem 2 opções:
  - **X dias antes**: Lembrar X dias antes da data da ocasião (deve digitar número de dias)
  - **No dia**: Lembrar na data da ocasião (não precisa digitar número de dias)
- **Mostrar Notificação Em**: Horário do lembrete (obrigatório, formato HH:mm)
- **Repetir Diariamente Até Concluído**: Se ativado, a notificação se repetirá diariamente até o usuário marcar a etapa como concluída
- **Vincular Lista de Verificação**: Cada etapa pode anexar uma lista de compras para rastrear progresso de compras

### 6.4 Lista de Verificação

- A lista de verificação pode ser reutilizada para múltiplas etapas
- Rastrear número de itens concluídos / Total de itens (ex.: "Concluído 3 / 8 itens")
- Exibida nos detalhes da etapa com link "nome da lista de verificação ›" para ver detalhes
- Pode marcar/desmarcar itens na lista de verificação para atualizar progresso
- A etapa de preparação pode ser marcada como concluída mesmo se a lista de verificação não estiver totalmente concluída

### 6.5 Notificações

- **Notificação Principal da Ocasião**: Criada em `nextOccurDate + reminder_time`
  - Com ocasião ANUAL: a notificação será reconstruída quando o aplicativo iniciar (com base no nextOccurDate recém calculado)
  - Com ocasião UMA VEZ: a notificação é criada apenas uma vez para o nextOccurDate atual
- **Notificação da Etapa de Preparação**: Calcular data do lembrete com base em:
  - `nextOccurDate` da ocasião especial
  - `reminderType` e `daysBefore` (se houver)
  - `reminderTime`
- **Notificação de Repetição**: Se `repeatDailyUntilComplete = true`:
  - Criar notificação de repetição diária
  - Usar `notificationGroupKey` para agrupar notificações de repetição
  - Cancelar automaticamente quando o usuário marcar a etapa como concluída

## 7. Notas Importantes

- **Datas do Calendário Lunar**: 
  - O aplicativo converte automaticamente para calendário solar para exibição
  - Encontra "data solar MAIS PRÓXIMA no futuro" comparada à data atual
  - Anos futuros: O sistema sempre recalcula a data solar correspondente de (lunar_day, lunar_month) para cada ano
  - Se esse ano tiver mês regular e mês bissexto do mesmo mês: O sistema pode criar 2 lembretes para evitar perder
- **Repetição Anual**: 
  - A ocasião recalculará automaticamente nextOccurDate no próximo ano
  - Com calendário lunar: Cada ano converte da data lunar para a data solar correspondente
- **Horário do Lembrete**: 
  - Deve ter um valor (não pode estar vazio)
  - Deve estar no formato correto HH:mm (00:00 - 23:59)
- **Lista de Verificação**: 
  - Lista de verificação excluída ainda é exibida na etapa (mas não pode ser editada)
  - Pode marcar etapa como concluída mesmo se a lista de verificação não estiver totalmente concluída
- **Notificações**: 
  - Precisa ativar notificações em Configurações para receber lembretes
  - Notificações de repetição serão canceladas automaticamente ao marcar etapa como concluída
- **Status da Ocasião**:
  - **Não Iniciado**: Todas as etapas não estão concluídas (cinza)
  - **Em Progresso**: Pelo menos 1 etapa está concluída, mas não todas (azul)
  - **Concluído**: Todas as etapas estão concluídas (verde escuro)
  - Se a ocasião não tiver etapas de preparação: Status calculado por data (Não Iniciado / Em Andamento / Concluído)

