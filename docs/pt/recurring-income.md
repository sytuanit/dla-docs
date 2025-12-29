# Renda Recorrente

## 1. Propósito

O módulo **Renda Recorrente** ajuda você a gerenciar fontes de renda regulares, como:
- Salário mensal
- Renda de aluguel
- Pensão
- Dividendos de investimentos
- Outras rendas recorrentes

Este módulo cria automaticamente **ocorrências** com base no ciclo que você configura e lembra quando é hora de receber o pagamento.

## 2. Quando Usar

Use este módulo quando você tiver:
- Renda fixa em um cronograma (semanal, quinzenal ou mensal)
- Necessidade de rastrear e confirmar quando o pagamento é recebido
- Desejo de cálculo automático no orçamento mensal

## 3. Telas Relacionadas

- Lista de renda recorrente
- Adicionar nova renda recorrente
- Editar renda recorrente
- Histórico de ocorrências

## 4. Uso Principal

### 4.1 Adicionar Nova Renda Recorrente

1. Vá para **Funções** → Selecione **Renda Recorrente**
2. Toque no botão **+** (FAB) no canto inferior direito
3. Preencha as informações:
   - **Categoria**: Selecione ou crie uma nova categoria
   - **Valor**: Digite o valor da renda (pode ser deixado em branco, digite ao confirmar)
   - **Ciclo**: Selecione Semanal / Quinzenal / Mensal
   - **Data**: Selecione a data no ciclo (ex.: dia 15 de cada mês)
   - **Data de Início**: (Apenas para ciclo quinzenal) Selecione a data de início
   - **Nota**: Informações adicionais (opcional)
4. Toque em **Salvar**

### 4.2 Confirmar Pagamento Recebido

1. Vá para a lista de renda recorrente
2. Encontre o item com o badge **"Confirmação Pendente"** (amarelo)
3. Toque no item para abrir o diálogo de confirmação
4. Preencha:
   - **Valor Real**: (se diferente do esperado)
   - **Nota**: (opcional)
5. Toque em **Confirmar**

### 4.3 Editar Renda Recorrente

1. Vá para a lista de renda recorrente
2. Toque no item para editar
3. Selecione **Editar** no menu
4. Atualize as informações
5. Toque em **Salvar**

### 4.4 Ver Histórico

1. Vá para a lista de renda recorrente
2. Toque em um item
3. Selecione **Histórico** para ver todas as ocorrências passadas

### 4.5 Desativar/Ativar Renda

1. Vá para a lista de renda recorrente
2. Encontre o item para desativar/ativar
3. Alterne o interruptor **Ativo** no lado direito do item

## 5. Exemplos e Ilustrações de UI

### 5.1 Exemplo 1: Criar Renda Recorrente Mensal (Salário)

**Cenário**: Você deseja rastrear o salário mensal para que o aplicativo lembre automaticamente quando é hora de receber o pagamento.

**Passos**:
1. Vá para a tela Funções, selecione "Renda Recorrente"
2. Toque no botão "➕ Adicionar Novo" no canto inferior direito
3. Selecione a categoria "Salário" (ou crie nova se não disponível)
4. Digite o valor: €3.600
5. Selecione o ciclo "Mensal"
6. Selecione "Selecionar dia do mês", digite 5
7. Nota preenchida automaticamente "Salário mensal" (pode ser editada)
8. Toque em "Salvar"

**Resultado**: O aplicativo exibe mensagem de sucesso e retorna à lista. O novo item aparece com todas as informações, e o aplicativo lembrará automaticamente no dia 5 de cada mês.

---

### 5.2 Exemplo 2: Confirmar Renda Devida e Atualizar Valor Real

**Cenário**: É dia de pagamento (dia 5), mas o valor real recebido é €3.780 (aumento de salário) em vez de €3.600 conforme definido.

**Passos**:
1. Abra o aplicativo ou vá para a tela "Renda Recorrente"
2. O aplicativo detecta automaticamente a ocorrência devida e mostra o diálogo de confirmação
3. O diálogo exibe o valor padrão: €3.600
4. Atualize o valor real para €3.780
5. Digite a nota: "Este mês tem bônus" (opcional)
6. Toque em "Confirmar Recebido"

**Resultado**: O aplicativo atualiza a ocorrência confirmada com o valor real €3.780, cria automaticamente a próxima ocorrência e atualiza o saldo financeiro atual.

---

### 5.3 Exemplo 3: Cancelar Ocorrência de Renda Quando Pagamento Não Recebido

**Cenário**: É dia de pagamento de aluguel (dia 1), mas o inquilino não transferiu o dinheiro, então o pagamento não foi recebido.

**Passos**:
1. Abra o aplicativo ou vá para a tela "Renda Recorrente"
2. O aplicativo mostra o diálogo de confirmação para a ocorrência devida
3. Toque no botão "Cancelar Este"
4. Digite o motivo: "Inquilino não transferiu o dinheiro" (obrigatório)
5. Toque em "Confirmar Cancelamento"

**Resultado**: A ocorrência cancelada muda para o status "Cancelado", mostra o motivo do cancelamento e o aplicativo cria automaticamente a próxima ocorrência. O saldo financeiro não muda porque nenhum pagamento foi recebido.

## 6. Lógica e Regras

### 6.1 Ciclo e Data

- **Semanal**: Selecione o dia da semana (1=Segunda, 7=Domingo)
- **Quinzenal**: Selecione o dia da semana + data de início específica
- **Mensal**: Selecione o dia do mês (1-31)

### 6.2 Criar Ocorrências Automaticamente

- O aplicativo cria automaticamente **ocorrência** quando:
  - Adicionando nova renda
  - Alcançando a data no ciclo
  - Novo mês começa

### 6.3 Status da Ocorrência

- **PENDING**: Confirmação pendente (mostra badge amarelo)
- **COMPLETED**: Confirmado (mostra badge verde)
- **CANCELLED**: Cancelado (mostra badge vermelho)

### 6.4 Integração com Orçamento

- Ao confirmar a renda, o aplicativo atualiza automaticamente o orçamento do mês atual (se existir)
- A renda é calculada em "Renda Recorrente" no orçamento

### 6.5 Notificações

- O aplicativo envia notificação de lembrete quando o pagamento está devido
- O horário da notificação pode ser configurado para cada item (`notificationTime1`, `notificationTime2`, padrão 16:00 e 19:00)

## 7. Notas Importantes

- **Valor pode ser deixado em branco**: Se você não souber o valor exato, pode deixar em branco e digitar ao confirmar
- **Não pode excluir quando ocorrência existe**: Se houver ocorrências, você só pode desativar (isActive = false), não pode excluir
- **Confirmação tardia**: Você pode confirmar ocorrências passadas, o aplicativo recalculará automaticamente o orçamento
- **Alterar ciclo**: Ao editar o ciclo, as ocorrências futuras serão recalculadas

