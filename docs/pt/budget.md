# Orçamento

## 1. Propósito

O módulo **Orçamento** ajuda você a planejar e rastrear os gastos mensais, garantindo que você não ultrapasse o orçamento definido. Este módulo calcula automaticamente com base em:
- Sua renda recorrente
- Suas despesas recorrentes
- Despesas diárias reais

## 2. Quando Usar

Use este módulo quando você quiser:
- Planejar gastos mensais
- Controlar para não ultrapassar o orçamento
- Rastrear a taxa de poupança
- Ver análise de gastos por categoria
- Comparar orçamentos entre meses

## 3. Telas Relacionadas

- Criar orçamento (primeira vez ou copiar do mês anterior)
- Ver visão geral do orçamento
- Histórico de orçamento por mês
- Sugestão de cópia do mês anterior

## 4. Uso Principal

### 4.1 Criar Orçamento pela Primeira Vez (Caso A)

1. Vá para **Funções** → Selecione **Orçamento**
2. Se não houver orçamento, o aplicativo abrirá automaticamente a tela **Criar Orçamento**
3. O aplicativo calcula e exibe automaticamente:
   - **Renda Recorrente**: Total de toda a renda recorrente ativa (somente leitura, mostra detalhamento)
   - **Despesas Recorrentes**: Total de todas as despesas recorrentes ativas (somente leitura, mostra detalhamento)
   - **Orçamento Total (antes da poupança)**: Calculado automaticamente = Renda Recorrente - Despesas Recorrentes
4. Digite **Taxa de Poupança**: % de poupança (0-100%, obrigatório)
5. Veja **Valor da Poupança** e **Orçamento de Gastos** calculados automaticamente
6. Toque em **Salvar Orçamento**

### 4.2 Copiar Orçamento do Mês Anterior (Caso C)

1. Vá para **Funções** → Selecione **Orçamento**
2. Se o mês atual não tiver orçamento, mas o mês anterior tiver, o aplicativo mostrará a tela **Sugestão de Copiar Orçamento**
3. Escolha uma das opções:
   - **Copiar orçamento completo do mês anterior**: O aplicativo copia automaticamente a taxa de poupança, recalcula renda/despesas recorrentes dos dados atuais e cria o orçamento imediatamente
   - **Copiar e Ajustar**: O aplicativo navega para a tela de criar orçamento com a taxa de poupança pré-preenchida do mês anterior, você pode ajustar antes de salvar
   - **Criar Novo Orçamento**: Executar o fluxo de criar orçamento do zero (Caso A)
4. Se escolher "Copiar e Ajustar", ajuste a taxa de poupança se necessário
5. Toque em **Salvar Orçamento**

**Nota**: Ao copiar, a Renda Recorrente e as Despesas Recorrentes são recalculadas dos dados recorrentes atuais (não copiadas do mês anterior), apenas a taxa de poupança é copiada.

### 4.3 Ver Visão Geral do Orçamento (Caso B)

1. Vá para **Funções** → Selecione **Orçamento**
2. Se o mês atual tiver orçamento, o aplicativo abrirá a tela **Visão Geral**
3. Veja as informações:
   - **Orçamento de Gastos**: Limite de gastos definido
   - **Usado**: Valor gasto (incluindo despesas diárias e variações de renda/despesas)
   - **Restante**: Valor restante no orçamento
   - **Taxa de Uso**: % do orçamento usado (com cores de aviso)
   - **Variações de Renda e Despesas do Plano**: Variações do plano original
   - **Despesas Diárias por Categoria**: Análise detalhada de gastos por categoria

### 4.4 Editar Orçamento do Mês Atual

1. Na tela **Visão Geral do Orçamento**, toque no botão **"Editar Orçamento"**
2. O aplicativo mostra a tela de edição com:
   - **Renda Recorrente** e **Despesas Recorrentes**: Mantém valores antigos (somente leitura)
   - **Taxa de Poupança**: Pré-preenchida do orçamento atual (pode ser editada)
3. Altere a taxa de poupança se necessário
4. Veja o valor da poupança e o orçamento de gastos atualizarem automaticamente
5. Toque em **"Salvar Orçamento"**

**Nota**: Ao editar, a Renda Recorrente e as Despesas Recorrentes não são recalculadas (mantém snapshot antigo), apenas a taxa de poupança e o orçamento de gastos são atualizados.

### 4.5 Ver Histórico de Orçamento

1. Vá para **Funções** → Selecione **Orçamento**
2. Selecione **Histórico** no menu
3. Veja a lista de orçamentos dos meses passados
4. Toque em um mês para ver detalhes

### 4.6 Ver Detalhes de Despesas por Categoria

1. Vá para a tela **Visão Geral do Orçamento**
2. Role para baixo até a seção **Análise por Categoria**
3. Toque em uma categoria
4. Veja a lista de despesas nessa categoria

## 5. Exemplos e Ilustrações de UI

### 5.1 BUDGET-01: Criar Orçamento pela Primeira Vez para o Mês Atual

**Objetivo**: Criar orçamento pela primeira vez para que o aplicativo calcule e rastreie automaticamente os gastos mensais com base na renda e despesas recorrentes.

**Passos**:
1. Vá para a tela Funções, selecione "Gerenciamento de Orçamento"
2. O aplicativo detecta automaticamente que não há orçamento e mostra a tela "Criar Orçamento"
3. Veja as informações calculadas automaticamente: Renda Recorrente, Despesas Recorrentes, Orçamento Total (antes da poupança)
4. Digite a taxa de poupança: 20
5. Veja o valor da poupança e o orçamento de gastos calculados automaticamente
6. Toque no botão "Salvar Orçamento"

**Resultado**: Orçamento salvo para o mês atual, navega automaticamente para a tela "Visão Geral do Orçamento".

---

### 5.2 BUDGET-02: Ver Visão Geral do Orçamento do Mês Atual

**Objetivo**: Ver a situação de gastos comparada ao orçamento definido, incluindo valores usados, restantes e análise por categoria.

**Passos**:
1. Vá para a tela Funções, selecione "Gerenciamento de Orçamento"
2. O aplicativo detecta automaticamente que o orçamento existe e mostra a tela "Visão Geral do Orçamento"
3. Veja o Card 1 - Orçamento Mensal: Orçamento de Gastos, Usado, Restante, Taxa de Uso
4. Veja o Card 2 - Variações de Renda e Despesas do Plano
5. Veja o Card 3 - Despesas Diárias por Categoria
6. (Opcional) Clique em "Orçamento de Gastos ›" para ver o diálogo detalhado explicando o cálculo do orçamento

**Resultado**: Exibe todas as informações do orçamento do mês atual com barra de progresso e cores apropriadas.

---

### 5.3 BUDGET-03: Editar Orçamento do Mês Atual

**Objetivo**: Ajustar a taxa de poupança para alterar o orçamento de gastos do mês atual.

**Passos**:
1. Na tela "Visão Geral do Orçamento", toque no botão "Editar Orçamento"
2. O aplicativo mostra a tela de edição (similar à tela de criar orçamento)
3. Veja as informações atuais: Renda Recorrente, Despesas Recorrentes (mantém valores antigos)
4. Altere a taxa de poupança para 25
5. Veja o valor da poupança e o orçamento de gastos atualizarem automaticamente
6. Toque no botão "Salvar Orçamento"

**Resultado**: Orçamento atualizado, retorna para a tela "Visão Geral do Orçamento" com novos valores.

---

### 5.4 BUDGET-04: Copiar Orçamento do Mês Anterior ao Iniciar Novo Mês

**Objetivo**: Reutilizar o orçamento do mês anterior para economizar tempo criando novo orçamento, com opção de ajustar se necessário.

**Passos**:
1. Vá para a tela Funções, selecione "Gerenciamento de Orçamento"
2. O aplicativo detecta automaticamente que o mês atual não tem orçamento, mas o mês anterior tem, mostra a tela "Sugestão de Copiar Orçamento"
3. Selecione "Copiar e Ajustar"
4. O aplicativo navega para a tela de criar orçamento com a taxa de poupança pré-preenchida do mês anterior
5. (Opcional) Ajuste a taxa de poupança se necessário
6. Toque no botão "Salvar Orçamento"

**Resultado**: Novo orçamento criado para o mês atual, navega automaticamente para a tela "Visão Geral do Orçamento".

## 6. Lógica e Regras

### 6.1 Casos

- **Caso A**: Criar orçamento pela primeira vez (sem orçamento para nenhum mês)
- **Caso B**: O mês atual tem orçamento → Ver visão geral
- **Caso C**: O mês atual não tem, mas o mês anterior tem → Sugestão de cópia

### 6.2 Cálculo Automático

- **Renda Recorrente**: Total de todos os `recurring_income` ativos
- **Despesas Recorrentes**: Total de todas as `recurring_expense` ativas
- **Despesas Diárias**: Total de `daily_expense` no mês
- **Orçamento Total**: Renda Recorrente + Renda Extra
- **Poupança**: Orçamento Total × Taxa de Poupança

### 6.3 Integração com Outros Módulos

- Ao confirmar renda recorrente → Atualiza automaticamente o orçamento
- Ao confirmar despesa recorrente → Atualiza automaticamente o orçamento
- As despesas diárias são automaticamente calculadas no orçamento

### 6.4 Aviso de Orçamento Ultrapassado

- O aplicativo mostrará um aviso quando os gastos ultrapassarem o orçamento
- Aviso exibido na tela inicial e nas notificações

### 6.5 Snapshot

- Ao criar orçamento, o aplicativo cria um snapshot dos itens de renda/despesa para salvar o estado naquele momento
- O snapshot é usado para comparação e análise

## 7. Notas Importantes

- **Um orçamento por mês**: Você precisa criar orçamento para cada mês
- **Editar orçamento**: Você pode editar o orçamento do mês atual alterando a taxa de poupança. A Renda Recorrente e as Despesas Recorrentes permanecerão inalteradas (snapshot) para garantir precisão
- **Atualização automática**: O orçamento atualiza automaticamente quando você confirma renda/despesas
- **Copiar do mês anterior**: O recurso de cópia ajuda você a economizar tempo criando orçamento

