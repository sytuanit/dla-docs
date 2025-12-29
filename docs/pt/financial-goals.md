# Metas Financeiras

## 1. Propósito

O módulo **Metas Financeiras** ajuda você a:
- Definir metas financeiras (ex.: comprar casa, comprar carro)
- Planejar finanças para alcançar metas
- Avaliar suposições financeiras
- Comparar cenários de empréstimo
- Rastrear progresso da meta

## 2. Quando Usar

Use este módulo quando você quiser:
- Planejar para uma meta financeira importante
- Avaliar capacidade de empréstimo para comprar ativos
- Comparar opções financeiras
- Rastrear progresso de poupança

## 3. Telas Relacionadas

- Criar meta financeira (3 etapas)
- Detalhes da meta e planos
- Ver plano de empréstimo
- Avaliar suposições
- Avaliar suposições e empréstimo

## 4. Uso Principal

### 4.1 Criar Meta Financeira (3 Etapas)

#### Etapa 1: Digite Plano Financeiro

1. Vá para **Funções** → Selecione **Planejamento e Suposições**
2. Toque no botão **➕ Adicionar Novo** (FAB)
3. Veja as informações preenchidas automaticamente:
   - **Renda Média**: Recuperada automaticamente da renda recorrente ativa (pode clicar para ver detalhamento)
   - **Despesas Fixas**: Recuperadas automaticamente das despesas recorrentes ativas + pagamentos de empréstimo (pode clicar para ver detalhamento)
   - **Saldo Atual**: Recuperado automaticamente do saldo atual
4. Digite **Despesas de Vida**: Despesas mensais de vida (alimentação, transporte, etc.)
5. Veja a previsão calculada automaticamente:
   - Após 12 meses
   - Após 24 meses
   - Após 36 meses
   (se mantiver níveis atuais de renda e despesas)
6. Toque em **Continuar**

#### Etapa 2: Digite Informações da Meta

1. Digite **Nome da Meta**: (ex.: "Comprar Casa")
2. Digite **Valor Necessário**: Valor total necessário para alcançar a meta
3. Veja **Entrada**: Pré-preenchida do saldo atual (pode editar)
4. Toque em **Continuar**

#### Etapa 3: Verificar Capacidade de Alcançar Meta

1. Veja as informações da meta: Nome, Valor da Meta, Entrada, Lacuna Restante
2. Veja as finanças atuais: Renda Média, Despesas Médias, Poupança Média
3. Veja a conclusão:
   - "Você alcançará a meta em ~X anos" (se poupança > 0)
   - "Com a situação atual, você não pode alcançar a meta sem empréstimo ou melhorar as finanças" (se poupança <= 0)
4. Veja as próximas opções:
   - **Ver Opção de Empréstimo**: Avaliar capacidade de empréstimo
   - **Criar Suposição de Renda/Despesa**: Simular melhoria financeira
   - **Combinar Suposição + Empréstimo**: Cenário ótimo
5. Toque em **Salvar Meta** (pode salvar agora ou criar plano depois)

### 4.2 Ver Lista e Detalhes da Meta

1. Vá para **Funções** → Selecione **Planejamento e Suposições**
2. Veja a lista de metas criadas:
   - Cada meta exibe: Nome, Valor da Meta, Entrada Feita, Lacuna Restante
3. (Opcional) Use a barra de pesquisa para encontrar meta por nome
4. Toque em uma meta para ver detalhes:
   - **Informações da Meta**: Nome, Valor da Meta, Entrada, Lacuna Restante
   - **Plano Financeiro (baseline)**: Clique para ver diálogo com renda média, despesas, poupança
   - **Lista de Planos Salvos**: Planos de empréstimo, suposições ou combinações que foram criados

### 4.3 Criar Plano de Empréstimo para Meta

1. Na tela de detalhes da meta, toque no botão **➕ Adicionar Novo**
2. O aplicativo mostra diálogo para selecionar tipo de plano, selecione **"Empréstimo"**
3. Digite as informações do empréstimo: Valor do Empréstimo, Taxa de Juros, Prazo do Empréstimo, Nome do Plano
4. Veja os resultados calculados automaticamente: Pagamento Mensal, Valor Total a Pagar, Tempo para Alcançar Meta, Acessibilidade
5. Toque em **Salvar Plano**

### 4.4 Criar Suposição de Renda/Despesa

1. Na tela de detalhes da meta, toque no botão **➕ Adicionar Novo**
2. O aplicativo mostra diálogo para selecionar tipo de plano, selecione **"Suposição"**
3. Digite as suposições:
   - **Aumentar Renda**: Valor adicional (ou deixe em branco se não houver aumento)
   - **Diminuir Despesas**: Valor reduzido (ou deixe em branco se não houver diminuição)
   - Nome da suposição
4. Veja os resultados calculados automaticamente: Nova Renda, Novas Despesas, Nova Poupança, Novo Tempo para Alcançar Meta
5. Toque em **Salvar Suposição**

### 4.5 Excluir Meta Financeira

1. Vá para a tela de detalhes da meta
2. Toque no botão **Excluir** (ícone de excluir) no canto superior direito do card da meta
3. O aplicativo mostra diálogo de confirmação
4. Toque em **Excluir** para confirmar

**Nota**: Excluir meta excluirá todos os planos relacionados e não pode ser desfeito.

## 5. Exemplos e Ilustrações de UI

### 5.1 PLANNING-01: Criar Nova Meta Financeira (Comprar Casa)

**Objetivo**: Criar uma meta financeira para planejar e simular a capacidade de alcançar essa meta.

**Passos**:
1. Vá para a tela Funções, selecione "Planejamento e Suposições"
2. Toque no botão "➕ Adicionar Novo"
3. **Etapa 1**: Digite plano financeiro (veja informações preenchidas automaticamente, digite despesas de vida, veja previsão)
4. **Etapa 2**: Digite informações da meta (nome, valor necessário, entrada)
5. **Etapa 3**: Verifique capacidade de alcançar meta (veja conclusão e opções)
6. Toque em "Salvar Meta"

**Resultado**: Meta salva, retorna para a tela de lista de metas.

---

### 5.2 PLANNING-02: Ver Lista e Detalhes da Meta

**Objetivo**: Ver lista de metas criadas e ver detalhes de cada meta com planos salvos.

**Passos**:
1. Vá para a tela Funções, selecione "Planejamento e Suposições"
2. Veja a lista de metas criadas
3. (Opcional) Use a barra de pesquisa para encontrar meta por nome
4. Toque em uma meta para ver detalhes
5. Veja as informações da meta, plano financeiro (baseline) e lista de planos salvos

**Resultado**: Exibe todas as informações da meta e planos salvos.

---

### 5.3 PLANNING-03: Criar Plano de Empréstimo para Meta

**Objetivo**: Criar um plano de empréstimo para ver se empréstimo ajuda a encurtar o tempo para alcançar a meta e acessibilidade.

**Passos**:
1. Na tela de detalhes da meta, toque no botão "➕ Adicionar Novo"
2. Selecione "Empréstimo" no diálogo
3. Digite as informações do empréstimo: Valor do Empréstimo, Taxa de Juros, Prazo do Empréstimo, Nome do Plano
4. Veja os resultados calculados automaticamente
5. Toque em "Salvar Plano"

**Resultado**: Plano de empréstimo salvo e aparece na lista de planos.

---

### 5.4 PLANNING-04: Criar Suposição de Renda/Despesa para Melhorar Capacidade de Alcançar Meta

**Objetivo**: Criar suposição sobre aumentar renda ou diminuir despesas para ver se isso ajuda a alcançar a meta mais rápido.

**Passos**:
1. Na tela de detalhes da meta, toque no botão "➕ Adicionar Novo"
2. Selecione "Suposição" no diálogo
3. Digite as suposições: Aumentar Renda (se houver), Diminuir Despesas (se houver), Nome da Suposição
4. Veja os resultados calculados automaticamente
5. Toque em "Salvar Suposição"

**Resultado**: Suposição salva e aparece na lista de planos.

---

### 5.5 PLANNING-05: Excluir Meta Financeira

**Objetivo**: Excluir uma meta financeira quando não for mais necessária.

**Passos**:
1. Vá para a tela de detalhes da meta
2. Toque no botão "Excluir" (ícone de excluir)
3. Confirme a exclusão no diálogo

**Resultado**: Meta e todos os planos relacionados foram excluídos.

## 6. Lógica e Regras

### 6.1 Cálculo de Previsão

- Previsão baseada em:
  - Renda - Despesas Fixas - Despesas de Vida = Poupança/mês
  - Saldo Atual + (Poupança/mês × Número de meses)

### 6.2 Metas

- Lacuna Restante = Valor Necessário - Entrada
- Tempo Estimado = Lacuna Restante / Poupança Média (meses)
- Se poupança média <= 0: Não pode alcançar meta sem empréstimo ou melhorar finanças

### 6.3 Planos de Empréstimo

- Cálculo baseado em:
  - Valor do empréstimo
  - Taxa de juros
  - Prazo
  - Criar automaticamente cronograma de pagamento

### 6.4 Suposições Financeiras

- Avaliar suposições como:
  - Aumentar/diminuir renda
  - Aumentar/diminuir despesas
  - Alterar taxa de juros
- Ver impacto na capacidade de alcançar meta

## 7. Notas Importantes

- **Módulo Premium Necessário**: Este recurso é apenas para usuários Premium
- **Previsão é apenas para referência**: Baseada em suposição de renda e despesas estáveis
- **Pode criar múltiplos planos**: Você pode criar múltiplos planos (empréstimo, suposição, combinação) para comparar
- **Baseline é salvo**: Plano financeiro inicial (baseline) é salvo ao criar meta, usado para comparar com planos posteriores
- **Cálculo Automático**: Renda e despesas fixas recuperadas automaticamente de itens recorrentes ativos, incluindo pagamentos de empréstimo bancário
- **Excluir Meta**: Ao excluir meta, todos os planos relacionados também são excluídos e não podem ser restaurados

