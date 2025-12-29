# Renda Extra

## 1. Propósito

O módulo **Renda Extra** ajuda você a registrar renda não recorrente sem ciclo fixo, como:
- Vendas Online
- Freelance
- Bônus
- Presentes em Dinheiro
- Outras rendas irregulares

Diferentemente da **Renda Recorrente**, a renda extra não tem ciclo automático, você deve inserir manualmente cada vez.

## 2. Quando Usar

Use este módulo quando você quiser:
- Registrar renda aleatória e não recorrente
- Rastrear a renda total em um período
- Analisar tendências de renda extra
- Calcular no orçamento mensal

## 3. Telas Relacionadas

- Lista de renda extra
- Adicionar nova renda
- Editar renda

## 4. Uso Principal

### 4.1 Adicionar Renda Extra

1. Vá para **Funções** → Selecione **Renda Extra**
2. Toque no botão **+** (FAB) no canto inferior direito
3. Preencha as informações:
   - **Categoria**: Selecione ou crie nova categoria
   - **Valor**: Digite o valor recebido
   - **Data**: Selecione a data em que o dinheiro foi recebido (padrão é hoje)
   - **Nota**: Descrição detalhada (opcional)
4. Toque em **Salvar**

### 4.2 Ver Lista de Renda

1. Vá para **Funções** → Selecione **Renda Extra**
2. A lista é exibida de acordo com o layout configurado (1, 2, 3 ou 4 colunas)
3. Use **Pesquisar** para filtrar por categoria ou nota
4. Selecione **Filtro de Tempo**: Hoje / Esta Semana / Este Mês / Mês Passado / Personalizado

### 4.3 Editar Renda

1. Vá para a lista de renda extra
2. Pressione e segure no item para editar
3. Selecione **Editar** no menu
4. Atualize as informações
5. Toque em **Salvar**

### 4.4 Excluir Renda

1. Vá para a lista de renda extra
2. Pressione e segure no item para excluir
3. Selecione **Excluir** no menu
4. Confirme a exclusão

## 5. Ilustrações de UI (Wireframe)

### 5.1 Tela de Lista

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Renda Extra                │
├─────────────────────────────────────────┤
│  [🔍 Pesquisar...]                      │
│  [Este Mês ▼] [Esta Semana] [Hoje]     │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Vendas Online                      │ │
│  │ €18                                │ │
│  │ 15/11/2024                         │ │
│  │                                    │ │
│  │ [Editar] [Excluir]                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Freelance                          │ │
│  │ €36                                │ │
│  │ 14/11/2024                         │ │
│  │                                    │ │
│  │ [Editar] [Excluir]                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Total: €54                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Tela Adicionar/Editar

```text
┌─────────────────────────────────────────┐
│  ← Voltar    Adicionar Renda Extra      │
├─────────────────────────────────────────┤
│  Categoria *                             │
│  [Vendas Online ▼]                       │
│                                         │
│  Valor *                                 │
│  [€18]                                  │
│                                         │
│  Data *                                  │
│  [15/11/2024]                           │
│                                         │
│  Nota                                    │
│  [Vendido Produto A]                     │
│                                         │
│  [Salvar] [Cancelar]                    │
└─────────────────────────────────────────┘
```

## 6. Lógica e Regras

### 6.1 Layout de Exibição

- Você pode configurar o número de colunas: 1, 2, 3 ou 4 colunas
- O layout é salvo nas configurações e se aplica a todas as listas de renda extra

### 6.2 Filtro de Tempo

- **Hoje**: Mostra apenas renda de hoje
- **Esta Semana**: Do início da semana até hoje
- **Este Mês**: Do início do mês até hoje
- **Mês Passado**: Todo o mês anterior
- **Personalizado**: Selecione um intervalo de tempo personalizado

### 6.3 Pesquisa

- Pesquisa no **nome da categoria** e **nota**
- Não diferencia maiúsculas/minúsculas
- Pesquisa em tempo real enquanto você digita

### 6.4 Integração com Orçamento

- A renda extra é calculada em "Renda Extra" no orçamento
- Ajuda você a rastrear a renda mensal total

## 7. Notas Importantes

- **Sem Ciclo**: A renda extra não tem ciclo automático, você deve inserir manualmente cada vez
- **Pode Excluir**: Você pode excluir qualquer renda
- **Integração com Orçamento**: A renda extra é automaticamente calculada no orçamento do mês atual

