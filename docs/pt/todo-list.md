# Lista de Tarefas

## 1. Propósito

O módulo **Lista de Tarefas** ajuda você a gerenciar tarefas recorrentes e rastrear o progresso de conclusão, incluindo:
- Tarefas recorrentes baseadas em tempo (diárias/semanais/mensais/anuais)
- Tarefas recorrentes baseadas em métricas (milhas/horas/vezes...)
- Lembretes quando vencidas
- Rastreamento de histórico de conclusão
- Registro de despesas (se aplicável)

Este módulo ajuda você a nunca perder tarefas importantes como manutenção de carro, substituição de filtros, verificações periódicas, etc.

## 2. Quando Usar

Use este módulo quando você tiver:
- Tarefas que se repetem em um cronograma (ex.: Substituir filtro de água a cada 3 meses)
- Tarefas que se repetem com base em métricas (ex.: Trocar óleo do carro a cada 3.000 milhas)
- Necessidade de lembretes automáticos quando vencidas
- Desejo de rastrear histórico de conclusão
- Necessidade de registrar despesas associadas

## 3. Telas Relacionadas

- Tela de lista de tarefas
- Selecionar tipo de tarefa (Baseada em Tempo / Baseada em Métrica)
- Adicionar nova tarefa
- Editar tarefa
- Confirmar tarefa baseada em métrica
- Histórico de tarefas
- Lista de tarefas vencidas (lista de sino)

## 4. Uso Principal

### 4.1 Adicionar Tarefa Baseada em Tempo

1. Vá para **Funções** → Selecione **Lista de Tarefas**
2. Toque no botão **+** (FAB) no canto inferior direito
3. Selecione **Tarefa Baseada em Tempo**
4. Preencha as informações:
   - **Nome da Tarefa**: (obrigatório, ex.: "Substituir filtro de água")
   - **Ciclo de Recorrência**: Digite número e selecione unidade (Dia/Semana/Mês/Ano)
   - **Próxima Data de Vencimento**: Selecione data (permite apenas selecionar a partir de amanhã)
   - **Horário do Lembrete**: Selecione horário (obrigatório, ex.: 08:00)
   - **Esta tarefa gera despesas**: (Opcional) Marque se houver despesas
     - Se marcado: Selecione **Categoria** (obrigatório)
   - **Nota**: Informações adicionais (opcional)
5. Toque em **Salvar**

### 4.2 Adicionar Tarefa Baseada em Métrica

1. Vá para **Funções** → Selecione **Lista de Tarefas**
2. Toque no botão **+** (FAB)
3. Selecione **Tarefa Baseada em Métrica**
4. Preencha as informações:
   - **Nome da Tarefa**: (obrigatório, ex.: "Trocar óleo do carro")
   - **Ciclo**: Digite número (ex.: 3.000)
   - **Unidade**: Digite unidade (ex.: "Milhas")
   - **Último Valor de Métrica Concluído**: Digite valor atual (ex.: 12.500)
   - **Esta tarefa gera despesas**: (Opcional) Marque se houver despesas
     - Se marcado: Selecione **Categoria** (obrigatório)
   - **Nota**: Informações adicionais (opcional)
5. Toque em **Salvar**

### 4.3 Confirmar Tarefa Baseada em Métrica

1. Vá para a lista de tarefas
2. Encontre a tarefa baseada em métrica (tipo METRIC) para confirmar
3. Toque no botão **Confirmar** no card (apenas mostrado quando `isActive = true`)
4. Preencha as informações:
   - **Valor de Métrica Atual**: Digite valor atual (obrigatório, deve ser ≥ último valor de métrica concluído)
   - **Nota**: (Opcional)
5. Veja **Delta** calculado automaticamente (valor atual - último valor concluído)
6. Toque em **Confirmado**
7. (Se a tarefa tiver despesas) Selecione **Adicionar Despesa** ou **Cancelar**

**Nota**: Tarefas baseadas em tempo (tipo CYCLE) não têm botão "Confirmar" no card. A confirmação é feita apenas na tela "Tarefas Vencidas" (lista de sino).

### 4.4 Ver Lista e Detalhes

1. Vá para **Funções** → Selecione **Lista de Tarefas**
2. Use **Barra de pesquisa** para pesquisar por nome da tarefa
3. Use **Filtros** para filtrar:
   - **Todas**: Mostrar todas as tarefas
   - **Baseada em Tempo**: Mostrar apenas tarefas do tipo CYCLE
   - **Baseada em Métrica**: Mostrar apenas tarefas do tipo METRIC
4. Toque em um card de tarefa para ver detalhes e editar

### 4.5 Editar Tarefa

1. Vá para a lista de tarefas
2. Toque no card da tarefa para editar
3. Atualize as informações:
   - **Nota**: Se houver histórico, **Ciclo** (CYCLE) ou **Unidade/Ciclo** (METRIC) estarão bloqueados e não poderão ser editados
4. Toque em **Salvar**

### 4.6 Ver Histórico

1. Vá para a lista de tarefas
2. Toque no link **Ver Histórico ›** da tarefa para ver
3. Use **Filtros** para filtrar por tempo:
   - **Todas**: Mostrar todo o histórico
   - **Este Mês**: Mostrar apenas histórico do mês atual
   - **Mês Passado**: Mostrar apenas histórico do mês anterior
   - **Últimos 3 Meses**: Mostrar apenas histórico dos últimos 3 meses

### 4.7 Desativar/Ativar Tarefa

1. Vá para a lista de tarefas
2. Encontre a tarefa para desativar/ativar
3. Alterne o interruptor **Ativo** no rodapé do card
4. Tarefas desativadas mostrarão um badge **"Inativo"** (cinza)

### 4.8 Excluir Tarefa

1. Vá para a lista de tarefas
2. Toque no ícone **Excluir** (🗑️) no cabeçalho do card
3. Confirme a exclusão no diálogo
4. A tarefa e todo o histórico relacionado serão excluídos

## 5. Exemplos e Ilustrações de UI

### TODO-01: Criar Tarefa Baseada em Tempo (Substituir Filtro de Água)

**Objetivo**: Criar uma tarefa baseada em tempo para que o aplicativo lembre automaticamente quando estiver vencida.

**Passos Principais**:
1. Vá para Funções → Lista de Tarefas → Toque no botão "+" (FAB)
2. Selecione "Tarefa Baseada em Tempo"
3. Digite nome da tarefa: "Substituir filtro de água"
4. Digite ciclo: "3" meses
5. Selecione próxima data de vencimento: 01/03/2026
6. Selecione horário do lembrete: 08:00
7. Marque "Esta tarefa gera despesas", selecione categoria "Utilidades"
8. Digite nota: "Substituir filtro #1 e #2"
9. Toque em "Salvar"

---

### TODO-02: Criar Tarefa Baseada em Métrica (Trocar Óleo do Carro)

**Objetivo**: Criar uma tarefa baseada em métrica para rastrear manutenção de carro com base na quilometragem.

**Passos Principais**:
1. Vá para Funções → Lista de Tarefas → Toque no botão "+" (FAB)
2. Selecione "Tarefa Baseada em Métrica"
3. Digite nome da tarefa: "Trocar óleo do carro"
4. Digite ciclo: "3.000", unidade: "Milhas"
5. Digite último valor de métrica concluído: "12.500"
6. Marque "Esta tarefa gera despesas", selecione categoria "Manutenção de Carro"
7. Digite nota: "Trocar óleo + filtro de óleo"
8. Toque em "Salvar"

---

### TODO-03: Ver Lista e Detalhes

**Objetivo**: Ver visão geral de tarefas, filtrar por tipo, pesquisar e ver detalhes de cada tarefa.

**Passos Principais**:
1. Vá para Funções → Lista de Tarefas
2. Veja a lista com barra de pesquisa e filtros
3. Use filtros: "Todas", "Baseada em Tempo", "Baseada em Métrica"
4. Use a barra de pesquisa para pesquisar por nome da tarefa
5. Toque em um card de tarefa para ver detalhes

---

### TODO-04: Confirmar Tarefa Baseada em Métrica (Trocar Óleo do Carro)

**Objetivo**: Confirmar conclusão de uma tarefa baseada em métrica digitando o valor de métrica atual.

**Passos Principais**:
1. Vá para a lista de tarefas
2. Encontre a tarefa "Trocar óleo do carro" (tipo METRIC)
3. Toque no botão "Confirmar"
4. Digite valor de métrica atual: "14.520"
5. Veja delta calculado automaticamente: "+2.020 milhas"
6. Digite nota: "Trocado óleo + filtro de óleo"
7. Toque em "Confirmado"

---

### TODO-05: Editar Tarefa e Ver Histórico

**Objetivo**: Editar informações da tarefa e ver histórico de conclusão.

**Passos Principais**:
1. Vá para a lista de tarefas
2. Toque no card da tarefa "Substituir filtro de água"
3. Veja aviso: "⚠️ Ciclo está bloqueado porque há histórico" (se houver histórico)
4. Edite próxima data de vencimento, horário do lembrete, nota
5. Toque em "Salvar"
6. Toque em "Ver Histórico ›" para ver histórico com filtros

---

### TODO-06: Desativar e Excluir Tarefa

**Objetivo**: Desativar ou excluir uma tarefa quando não for mais necessária.

**Passos Principais**:
1. Vá para a lista de tarefas
2. Encontre a tarefa para desativar
3. Toque no interruptor "Ativo" para desligar
4. Veja badge "Inativo" aparecer
5. Toque no interruptor novamente para reativar
6. Toque no ícone Excluir (🗑️) para excluir a tarefa
7. Confirme a exclusão no diálogo

---

### TODO-07: Confirmar Tarefa Baseada em Métrica e Adicionar Despesa

**Objetivo**: Confirmar uma tarefa baseada em métrica e adicionar automaticamente a despesa relacionada.

**Passos Principais**:
1. Vá para a lista de tarefas
2. Encontre a tarefa "Trocar óleo do carro" (tipo METRIC, hasCost = true)
3. Toque no botão "Confirmar"
4. Digite valor de métrica atual: "14.520"
5. Digite nota: "Trocado óleo + filtro de óleo"
6. Toque em "Confirmado"
7. Veja o diálogo "Despesa Gerada?" abrir automaticamente
8. Toque em "Adicionar Despesa"
9. Veja a tela "Adicionar Despesa" com nota e categoria pré-preenchidas
10. Digite valor: €45
11. Toque em "Salvar"

## 6. Lógica e Regras

### 6.1 Tipos de Tarefa

- **Baseada em Tempo (tipo CYCLE)**:
  - Repete em um cronograma (Dia/Semana/Mês/Ano)
  - Tem notificações de lembrete quando vencida
  - Confirmação feita apenas na tela "Tarefas Vencidas" (lista de sino)
  - Sem botão "Confirmar" no card

- **Baseada em Métrica (tipo METRIC)**:
  - Repete com base em marcos de métrica (Milhas/Horas/Vezes/Outro)
  - Sem notificações (MVP1)
  - Tem botão "Confirmar" no card (apenas mostrado quando `isActive = true`)
  - Confirmação digitando valor de métrica atual

### 6.2 Status da Tarefa

- **PENDING**: Próxima (ainda não vencida)
  - Sem badge mostrado: `nextDueDate - hoje > 7 dias`
  - Mostrar badge "Próxima" (amarelo): `0 < nextDueDate - hoje ≤ 7 dias`
- **OVERDUE**: Vencida (vermelho) - `nextDueDate < hoje` e não confirmada
- **NOT_COMPLETED**: Não feita (laranja) - Vencida mas não confirmada
- **COMPLETED**: Concluída (verde) - Confirmada
- **CANCELLED**: Cancelada (cinza) - Esta ocorrência foi cancelada
- **INACTIVE**: Inativa (cinza) - `isActive = false`

### 6.3 Bloquear Ciclo/Unidade

- Se houver histórico (registros de histórico):
  - **Tipo CYCLE**: Ciclo está bloqueado, não pode ser editado
  - **Tipo METRIC**: Unidade e ciclo estão bloqueados, não podem ser editados
- Mostrar aviso: "⚠️ Ciclo está bloqueado porque há histórico" ou "⚠️ Unidade está bloqueada porque há histórico"

### 6.4 Confirmar Tarefa Baseada em Métrica

- **Validação**:
  - Valor de métrica atual deve ser ≥ último valor de métrica concluído
  - Se inválido: Mostrar erro "Valor de métrica atual deve ser ≥ último valor de métrica concluído"
- **Atualização Automática**:
  - `lastMetricValue` = valor atual
  - `nextMetricValue` = valor atual + ciclo
  - `lastCompletedDate` = hoje
- **Despesas**:
  - Se `hasCost = true`: Mostrar diálogo "Despesa Gerada?" após confirmação bem-sucedida
  - Navegar para tela "Adicionar Despesa" com `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Notificações

- **Tipo CYCLE**: 
  - Notificações são agendadas ao criar/editar tarefa
  - Notificações são canceladas ao desativar ou excluir tarefa
  - Notificações são reagendadas ao reativar (se `nextDueDate >= hoje`)
- **Tipo METRIC**: Sem notificações (MVP1)

### 6.6 Calcular Próxima Data de Vencimento

- **Tipo CYCLE**: 
  - Próxima data de vencimento calculada automaticamente com base no ciclo após confirmação
  - Exemplo: Ciclo 3 meses, data de vencimento 01/03/2026 → Após confirmação, próxima data de vencimento = 01/06/2026
- **Tipo METRIC**: 
  - Próximo vencimento = valor atual + ciclo
  - Exemplo: Valor atual 14.520 milhas, ciclo 3.000 milhas → Próximo vencimento = 17.520 milhas

## 7. Notas Importantes

1. **Botão Confirmar**:
   - **Tarefas baseadas em tempo (CYCLE)**: Sem botão "Confirmar" no card. A confirmação é feita apenas na tela "Tarefas Vencidas" (lista de sino).
   - **Tarefas baseadas em métrica (METRIC)**: Tem botão "Confirmar" no card (apenas mostrado quando `isActive = true`).

2. **Ícone de Sino**: O ícone de sino no cabeçalho navega para a tela "Tarefas Vencidas" (lista de sino) onde os usuários podem confirmar tarefas vencidas (apenas para tipo CYCLE).

3. **Bloquear Ciclo/Unidade**: Se houver histórico, o ciclo (CYCLE) ou unidade/ciclo (METRIC) estarão bloqueados e não poderão ser editados para garantir consistência dos dados.

4. **Validação de Métrica**: Ao confirmar uma tarefa baseada em métrica, o valor de métrica atual deve ser ≥ último valor de métrica concluído. Se não, o aplicativo mostrará um erro e impedirá a confirmação.

5. **Despesas Geradas**: Se uma tarefa tiver despesas (`hasCost = true`), após confirmação bem-sucedida, o aplicativo perguntará se você quer adicionar uma despesa. Se escolher "Adicionar Despesa", o aplicativo preencherá automaticamente a nota e a categoria.

6. **Excluir Tarefa**: Ao excluir uma tarefa, todo o histórico relacionado também será excluído (exclusão em cascata). As notificações também serão canceladas.

7. **Desativar**: Ao desativar uma tarefa do tipo CYCLE, as notificações serão canceladas. Ao reativar, as notificações serão reagendadas (se `nextDueDate >= hoje`).

8. **Acesso Premium**: Este módulo requer Acesso Premium. Se você não tiver Premium, o aplicativo mostrará um diálogo solicitando upgrade.

