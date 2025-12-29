# Ingresos Extra

## 1. Propósito

El módulo **Ingresos Extra** le ayuda a registrar ingresos no recurrentes sin ciclo fijo como:
- Ventas en línea
- Trabajo freelance
- Bonos
- Regalos en efectivo
- Otros ingresos irregulares

A diferencia de **Ingresos Recurrentes**, los ingresos extra no tienen ciclo automático, debe ingresarlos manualmente cada vez.

## 2. Cuándo usar

Use este módulo cuando desee:
- Registrar ingresos aleatorios no recurrentes
- Rastrear ingresos totales en un período de tiempo
- Analizar tendencias de ingresos extra
- Calcular en presupuesto mensual

## 3. Pantallas relacionadas

- Lista de ingresos extra
- Agregar nuevo ingreso
- Editar ingreso

## 4. Uso principal

### 4.1 Agregar ingreso extra

1. Vaya a **Funciones** → Seleccione **Ingresos Extra**
2. Toque el botón **+** (FAB) en la esquina inferior derecha
3. Complete la información:
   - **Categoría**: Seleccione categoría o cree nueva
   - **Cantidad**: Ingrese el monto recibido
   - **Fecha**: Seleccione fecha en que se recibió el dinero (por defecto es hoy)
   - **Nota**: Descripción detallada (opcional)
4. Toque **Guardar**

### 4.2 Ver lista de ingresos

1. Vaya a **Funciones** → Seleccione **Ingresos Extra**
2. La lista se muestra según su configuración de disposición (1, 2, 3 o 4 columnas)
3. Use **Búsqueda** para filtrar por categoría o nota
4. Seleccione **Filtro de tiempo**: Hoy / Esta semana / Este mes / Mes pasado / Personalizado

### 4.3 Editar ingreso

1. Vaya a la lista de ingresos extra
2. Mantenga presionado el elemento a editar
3. Seleccione **Editar** del menú
4. Actualice la información
5. Toque **Guardar**

### 4.4 Eliminar ingreso

1. Vaya a la lista de ingresos extra
2. Mantenga presionado el elemento a eliminar
3. Seleccione **Eliminar** del menú
4. Confirme la eliminación

## 5. Ilustraciones de UI (Wireframe)

### 5.1 Pantalla de lista

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Ingresos Extra                 │
├─────────────────────────────────────────┤
│  [🔍 Buscar...]                         │
│  [Este mes ▼] [Esta semana] [Hoy]     │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Ventas en línea                        │ │
│  │ €18                                 │ │
│  │ 15/11/2024                          │ │
│  │                                    │ │
│  │ [Editar] [Eliminar]                    │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Trabajo freelance                           │ │
│  │ €36                                 │ │
│  │ 14/11/2024                          │ │
│  │                                    │ │
│  │ [Editar] [Eliminar]                    │
│  └───────────────────────────────────┘ │
│                                         │
│  Total: €54                            │
├─────────────────────────────────────────┤
│                                    [+]   │
└─────────────────────────────────────────┘
```

### 5.2 Pantalla Agregar/Editar

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Agregar Ingreso Extra             │
├─────────────────────────────────────────┤
│  Categoría *                              │
│  [Ventas en línea ▼]                        │
│                                         │
│  Cantidad *                                │
│  [€18]                                  │
│                                         │
│  Fecha *                                  │
│  [15/11/2024]                           │
│                                         │
│  Nota                                    │
│  [Producto A vendido]                        │
│                                         │
│  [Guardar] [Cancelar]                        │
└─────────────────────────────────────────┘
```

## 6. Lógica y reglas

### 6.1 Disposición de visualización

- Puede configurar el número de columnas: 1, 2, 3 o 4 columnas
- La disposición se guarda en configuración y se aplica a todas las listas de ingresos extra

### 6.2 Filtro de tiempo

- **Hoy**: Muestra solo ingresos de hoy
- **Esta semana**: Desde el inicio de la semana hasta hoy
- **Este mes**: Desde el inicio del mes hasta hoy
- **Mes pasado**: Todo el mes anterior
- **Personalizado**: Seleccionar período de tiempo personalizado

### 6.3 Búsqueda

- Busca en **nombre de categoría** y **nota**
- No distingue entre mayúsculas y minúsculas
- Búsqueda en tiempo real mientras escribe

### 6.4 Integración con presupuesto

- Los ingresos extra se calculan en "Ingresos Extra" en el presupuesto
- Le ayuda a rastrear el ingreso mensual total

## 7. Notas importantes

- **Sin ciclo**: Los ingresos extra no tienen ciclo automático, debe ingresarlos manualmente cada vez
- **Se pueden eliminar**: Puede eliminar cualquier ingreso
- **Integración con presupuesto**: Los ingresos extra se calculan automáticamente en el presupuesto del mes actual

