# Gastos Diarios

## 1. Propósito

El módulo **Gastos Diarios** le ayuda a registrar gastos regulares no fijos como:
- Comida y restaurantes
- Compras
- Transporte
- Entretenimiento
- Otros gastos flexibles

A diferencia de **Gastos Recurrentes**, los gastos diarios a menudo varían en cantidad y frecuencia, sin ciclo fijo.

## 2. Cuándo usar

Use este módulo cuando desee:
- Registrar gastos aleatorios no recurrentes
- Rastrear gastos diarios para controlar el presupuesto
- Analizar tendencias de gastos por categoría
- Ver gastos totales en un período de tiempo

## 3. Pantallas relacionadas

- Lista de gastos diarios
- Agregar nuevo gasto
- Editar gasto

## 4. Uso principal

### 4.1 Agregar gasto diario

1. Vaya a **Funciones** → Seleccione **Gastos Diarios**
2. Toque el botón **+** (FAB) en la esquina inferior derecha
3. Complete la información:
   - **Categoría**: Seleccione categoría (o use categoría predeterminada, si está configurada)
   - **Cantidad**: Ingrese el monto gastado
   - **Fecha**: Seleccione fecha del gasto (por defecto es hoy)
   - **Nota**: Descripción detallada (opcional)
4. Toque **Guardar**

### 4.2 Ver lista de gastos

1. Vaya a **Funciones** → Seleccione **Gastos Diarios**
2. La lista se muestra según su configuración de disposición (2, 3 o 4 columnas)
3. Use **Búsqueda** para filtrar por categoría o nota
4. Seleccione **Filtro de tiempo**: Hoy / Esta semana / Este mes / Mes pasado / Personalizado

### 4.3 Editar gasto

1. Vaya a la lista de gastos diarios
2. Mantenga presionado el elemento a editar
3. Seleccione **Editar** del menú
4. Actualice la información
5. Toque **Guardar**

### 4.4 Eliminar gasto

1. Vaya a la lista de gastos diarios
2. Mantenga presionado el elemento a eliminar
3. Seleccione **Eliminar** del menú
4. Confirme la eliminación

### 4.5 Establecer categoría predeterminada

1. Vaya a **Configuración** → **Categorías** → **Categorías de gastos diarios**
2. Toque la categoría que desea establecer como predeterminada
3. Seleccione **Establecer como predeterminada**
4. Al agregar nuevo gasto, esta categoría se seleccionará automáticamente

## 5. Ilustraciones de UI (Wireframe)

### 5.1 Pantalla de lista

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Gastos Diarios               │
├─────────────────────────────────────────┤
│  [🔍 Buscar...]                         │
│  [Hoy ▼] [Esta semana] [Este mes]    │
├─────────────────────────────────────────┤
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Comida│ │Compr│ │ Taxi │            │
│  │ fuera│ │as │ │      │            │
│  │      │ │      │ │      │            │
│  │ €1.80│ │ €7.20│ │ €0.90│            │
│  │      │ │      │ │      │            │
│  │ 15/11│ │ 15/11│ │ 14/11│            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  ┌──────┐ ┌──────┐ ┌──────┐            │
│  │ Café│ │ Otr│ │      │            │
│  │     │ │os │ │      │            │
│  │      │ │      │ │      │            │
│  │ €0.90│ │ €3.60│ │      │            │
│  │      │ │      │ │      │            │
│  │ 13/11│ │ 12/11│ │      │            │
│  └──────┘ └──────┘ └──────┘            │
│                                         │
│  Total: €14.40                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Pantalla Agregar/Editar

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Agregar Gasto Diario            │
├─────────────────────────────────────────┤
│  Categoría *                              │
│  [Comida fuera ▼]                            │
│                                         │
│  Cantidad *                                │
│  [€1.80]                                   │
│                                         │
│  Fecha *                                  │
│  [15/11/2024]                           │
│                                         │
│  Nota                                    │
│  [Almuerzo con amigo]                     │
│                                         │
│  [Guardar] [Cancelar]                        │
└─────────────────────────────────────────┘
```

### 5.3 Menú (Mantener presionado)

```text
┌─────────────────────────────────────────┐
│  ┌───────────────────────────────────┐ │
│  │ Comida fuera                            │ │
│  │ €1.80                                  │ │
│  │ 15/11/2024                          │
│  │                                     │
│  │ [Editar] [Eliminar]                    │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Lógica y reglas

### 6.1 Disposición de visualización

- Puede configurar el número de columnas: 2, 3 o 4 columnas
- La disposición se guarda en configuración y se aplica a todas las listas de gastos

### 6.2 Filtro de tiempo

- **Hoy**: Muestra solo gastos de hoy
- **Esta semana**: Desde el inicio de la semana hasta hoy
- **Este mes**: Desde el inicio del mes hasta hoy
- **Mes pasado**: Todo el mes anterior
- **Personalizado**: Seleccionar período de tiempo personalizado

### 6.3 Búsqueda

- Busca en **nombre de categoría** y **nota**
- No distingue entre mayúsculas y minúsculas
- Búsqueda en tiempo real mientras escribe

### 6.4 Categoría predeterminada

- Si ha establecido una categoría predeterminada, al abrir la pantalla de agregar, esta categoría se seleccionará automáticamente
- La nota también puede completarse automáticamente según la categoría (si está configurada)

### 6.5 Gastos totales

- Los gastos totales se calculan según el filtro de tiempo actualmente seleccionado
- Se muestra al final de la lista

## 7. Notas importantes

- **Sin ciclo**: Los gastos diarios no tienen ciclo automático, debe ingresarlos manualmente cada vez
- **Se pueden eliminar**: Puede eliminar cualquier gasto (a diferencia de los gastos recurrentes)
- **Sin integración con presupuesto**: Los gastos diarios no se calculan automáticamente en el presupuesto (debe rastrearlos usted mismo)
- **Categorías personalizadas**: Puede crear nuevas categorías en configuración

