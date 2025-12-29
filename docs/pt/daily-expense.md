# Despesas Diárias

## 1. Propósito

O módulo **Despesas Diárias** ajuda você a registrar despesas regulares e não fixas, como:
- Alimentação e Restaurantes
- Compras
- Transporte
- Entretenimento
- Outras despesas flexíveis

Diferentemente das **Despesas Recorrentes**, as despesas diárias geralmente variam em valor e frequência, sem ciclo fixo.

## 2. Quando Usar

Use este módulo quando você quiser:
- Registrar despesas aleatórias e não recorrentes
- Rastrear gastos diários para controlar o orçamento
- Analisar tendências de gastos por categoria
- Ver o total de gastos em um período

## 3. Telas Relacionadas

- Lista de despesas diárias
- Adicionar nova despesa
- Editar despesa

## 4. Uso Principal

### 4.1 Adicionar Despesa Diária

1. Vá para **Funções** → Selecione **Despesas Diárias**
2. Toque no botão **+** (FAB) no canto inferior direito
3. Preencha as informações:
   - **Categoria**: Selecione a categoria (ou use a categoria padrão se configurada)
   - **Valor**: Digite o valor gasto
   - **Data**: Selecione a data da despesa (padrão é hoje)
   - **Nota**: Descrição detalhada (opcional)
4. Toque em **Salvar**

### 4.2 Ver Lista de Despesas

1. Vá para **Funções** → Selecione **Despesas Diárias**
2. A lista é exibida de acordo com o layout configurado (2, 3 ou 4 colunas)
3. Use **Pesquisar** para filtrar por categoria ou nota
4. Selecione **Filtro de Tempo**: Hoje / Esta Semana / Este Mês / Mês Passado / Personalizado

### 4.3 Editar Despesa

1. Vá para a lista de despesas diárias
2. Pressione e segure no item para editar
3. Selecione **Editar** no menu
4. Atualize as informações
5. Toque em **Salvar**

### 4.4 Excluir Despesa

1. Vá para a lista de despesas diárias
2. Pressione e segure no item para excluir
3. Selecione **Excluir** no menu
4. Confirme a exclusão

### 4.5 Definir Categoria Padrão

1. Vá para **Configurações** → **Categorias** → **Categorias de Despesas Diárias**
2. Toque na categoria que deseja definir como padrão
3. Selecione **Definir como Padrão**
4. Ao adicionar nova despesa, esta categoria será automaticamente selecionada

## 5. Ilustrações de UI (Wireframe)

### 5.1 Tela de Lista

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Despesas Diárias           │
├─────────────────────────────────────────┤
│  [🔍 Pesquisar...]                      │
│  [Hoje ▼] [Esta Semana] [Este Mês]     │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐           │
│  │ Comida│ │ Compr│ │ Taxi │           │
│  │ Fora  │ │ as   │ │      │           │
│  │       │ │      │ │      │           │
│  │ €1,80 │ │ €7,20│ │ €0,90│           │
│  │       │ │      │ │      │           │
│  │ 15/11 │ │ 15/11│ │ 14/11│           │
│  └──────┘ └──────┘ └──────┘           │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐           │
│  │ Café │ │ Outro│ │      │           │
│  │      │ │      │ │      │           │
│  │      │ │      │ │      │           │
│  │ €0,90│ │ €3,60│ │      │           │
│  │      │ │      │ │      │           │
│  │ 13/11│ │ 12/11│ │      │           │
│  └──────┘ └──────┘ └──────┘           │
│                                         │
│  Total: €14,40                         │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Tela Adicionar/Editar

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Adicionar Despesa Diária   │
├─────────────────────────────────────────┤
│  Categoria *                             │
│  [Comida Fora ▼]                         │
│                                         │
│  Valor *                                 │
│  [€1,80]                                │
│                                         │
│  Data *                                  │
│  [15/11/2024]                           │
│                                         │
│  Nota                                    │
│  [Almoço com amigo]                     │
│                                         │
│  [Salvar] [Cancelar]                    │
└─────────────────────────────────────────┘
```

## 6. Lógica e Regras

### 6.1 Layout de Exibição

- Você pode configurar o número de colunas: 2, 3 ou 4 colunas
- O layout é salvo nas configurações e se aplica a todas as listas de despesas

### 6.2 Filtro de Tempo

- **Hoje**: Mostra apenas despesas de hoje
- **Esta Semana**: Do início da semana até hoje
- **Este Mês**: Do início do mês até hoje
- **Mês Passado**: Todo o mês anterior
- **Personalizado**: Selecione um intervalo de tempo personalizado

### 6.3 Pesquisa

- Pesquisa no **nome da categoria** e **nota**
- Não diferencia maiúsculas/minúsculas
- Pesquisa em tempo real enquanto você digita

### 6.4 Categoria Padrão

- Se você definiu uma categoria padrão, ao abrir a tela de adicionar, essa categoria será automaticamente selecionada
- A nota também pode ser preenchida automaticamente com base na categoria (se configurada)

### 6.5 Total de Despesas

- Total de despesas calculado com base no filtro de tempo selecionado
- Exibido na parte inferior da lista

## 7. Notas Importantes

- **Sem Ciclo**: As despesas diárias não têm ciclo automático, você deve inserir manualmente cada vez
- **Pode Excluir**: Você pode excluir qualquer despesa (diferentemente das despesas recorrentes)
- **Sem Integração com Orçamento**: As despesas diárias não são automaticamente calculadas no orçamento (você deve rastrear você mesmo)
- **Categorias Personalizadas**: Você pode criar novas categorias em Configurações

