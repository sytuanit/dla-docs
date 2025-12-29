# Despesas Recorrentes

## 1. Propósito

O módulo **Despesas Recorrentes** ajuda você a gerenciar despesas periódicas com ciclos fixos, como:
- Contas de eletricidade, água, gás
- Internet, TV a cabo
- Seguro
- Mensalidade escolar
- Aluguel
- Outras despesas recorrentes

Este módulo cria automaticamente **ocorrências** com base no ciclo que você configura e lembra quando o pagamento está devido.

## 2. Quando Usar

Use este módulo quando você tiver:
- Despesas fixas em um cronograma (semanal, quinzenal ou mensal)
- Necessidade de rastrear e confirmar quando o pagamento é feito
- Desejo de cálculo automático no orçamento mensal

## 3. Telas Relacionadas

- Lista de despesas recorrentes
- Adicionar nova despesa recorrente
- Editar despesa recorrente
- Histórico de ocorrências

## 4. Uso Principal

### 4.1 Adicionar Nova Despesa Recorrente

1. Vá para **Funções** → Selecione **Despesas Recorrentes**
2. Toque no botão **+** (FAB) no canto inferior direito
3. Preencha as informações:
   - **Categoria**: Selecione ou crie uma nova categoria
   - **Valor**: Digite o valor da despesa (pode ser deixado em branco, digite ao confirmar)
   - **Ciclo**: Selecione Semanal / Quinzenal / Mensal
   - **Data**: Selecione a data no ciclo (ex.: dia 15 de cada mês)
   - **Data de Início**: (Apenas para ciclo quinzenal) Selecione a data de início
   - **Nota**: Informações adicionais (opcional)
4. Toque em **Salvar**

### 4.2 Confirmar Pagamento Feito

1. Vá para a lista de despesas recorrentes
2. Encontre o item com o badge **"Confirmação Pendente"** (amarelo)
3. Toque no item para abrir o diálogo de confirmação
4. Preencha:
   - **Valor Real**: (se diferente do esperado)
   - **Nota**: (opcional)
5. Toque em **Confirmar**

### 4.3 Editar Despesa Recorrente

1. Vá para a lista de despesas recorrentes
2. Toque no item para editar
3. Selecione **Editar** no menu
4. Atualize as informações
5. Toque em **Salvar**

### 4.4 Ver Histórico

1. Vá para a lista de despesas recorrentes
2. Toque em um item
3. Selecione **Histórico** para ver todas as ocorrências passadas

### 4.5 Desativar/Ativar Despesa

1. Vá para a lista de despesas recorrentes
2. Encontre o item para desativar/ativar
3. Alterne o interruptor **Ativo** no lado direito do item

## 5. Exemplos e Ilustrações de UI

### 5.1 Exemplo 1: Criar Despesa Recorrente Mensal (Conta de Eletricidade)

**Cenário**: Você deseja rastrear a conta mensal de eletricidade para que o aplicativo lembre automaticamente quando o pagamento está devido.

**Passos**:
1. Vá para a tela Funções, selecione "Despesas Recorrentes"
2. Toque no botão "➕ Adicionar Novo" no canto inferior direito
3. Selecione a categoria "Utilidades" (ou crie nova se não disponível)
4. Digite o valor: €18
5. Selecione o ciclo "Mensal"
6. Selecione "Selecionar dia do mês", digite 15
7. Nota preenchida automaticamente "Conta mensal de eletricidade" (pode ser editada)
8. Toque em "Salvar"

**Resultado**: O aplicativo exibe mensagem de sucesso e retorna à lista. O novo item aparece com todas as informações, e o aplicativo lembrará automaticamente no dia 15 de cada mês.

---

### 5.2 Exemplo 2: Confirmar Despesa Devida e Atualizar Valor Real

**Cenário**: É dia de pagamento da conta de água (dia 10), mas o valor real a pagar é €6,30 (diminuído) em vez de €7,20 conforme definido.

**Passos**:
1. Abra o aplicativo ou vá para a tela "Despesas Recorrentes"
2. O aplicativo detecta automaticamente a ocorrência devida e mostra o diálogo de confirmação
3. O diálogo exibe o valor padrão: €7,20
4. Atualize o valor real para €6,30
5. Digite a nota: "Este mês economizou água" (opcional)
6. Toque em "Confirmar Pago"

**Resultado**: O aplicativo atualiza a ocorrência confirmada com o valor real €6,30, cria automaticamente a próxima ocorrência e atualiza o saldo financeiro atual (subtrai €6,30).

---

### 5.3 Exemplo 3: Desativar Despesa Recorrente Quando Não Aplicável

**Cenário**: Você temporariamente não aluga um lugar por 2 meses, então deseja desativar a despesa "Aluguel" em vez de excluí-la completamente.

**Passos**:
1. Vá para a tela "Despesas Recorrentes"
2. Encontre o item "Aluguel" na lista
3. Toque no interruptor "Ativo" no lado direito do item
4. O aplicativo mostra o diálogo de confirmação: "Tem certeza de que deseja desativar esta despesa?"
5. Toque no botão "Desativar" para confirmar

**Resultado**: O card "Aluguel" muda para o status "Inativo" (cinza), o interruptor muda para "Inativo". O aplicativo não cria mais novas ocorrências para esta despesa. Você pode reativar tocando no interruptor "Inativo" → "Ativo".

## 6. Lógica e Regras

### 6.1 Ciclo e Data

- **Semanal**: Selecione o dia da semana (1=Segunda, 7=Domingo)
- **Quinzenal**: Selecione o dia da semana + data de início específica
- **Mensal**: Selecione o dia do mês (1-31)

### 6.2 Criar Ocorrências Automaticamente

- O aplicativo cria automaticamente **ocorrência** quando:
  - Adicionando nova despesa
  - Alcançando a data no ciclo
  - Novo mês começa

### 6.3 Status da Ocorrência

- **PENDING**: Confirmação pendente (mostra badge amarelo)
- **COMPLETED**: Confirmado (mostra badge verde)
- **CANCELLED**: Cancelado (mostra badge vermelho)

### 6.4 Integração com Orçamento

- Ao confirmar a despesa, o aplicativo atualiza automaticamente o orçamento do mês atual (se existir)
- A despesa é calculada em "Despesas Recorrentes" no orçamento

### 6.5 Notificações

- O aplicativo envia notificação de lembrete quando o pagamento está devido
- O horário da notificação pode ser configurado para cada item (`notificationTime1`, `notificationTime2`, padrão 16:00 e 19:00)

## 7. Notas Importantes

- **Valor pode ser deixado em branco**: Se você não souber o valor exato, pode deixar em branco e digitar ao confirmar
- **Não pode excluir quando ocorrência existe**: Se houver ocorrências, você só pode desativar (isActive = false), não pode excluir
- **Confirmação tardia**: Você pode confirmar ocorrências passadas, o aplicativo recalculará automaticamente o orçamento
- **Alterar ciclo**: Ao editar o ciclo, as ocorrências futuras serão recalculadas

