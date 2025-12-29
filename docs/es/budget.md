# Presupuesto

## 1. Propósito

El módulo **Presupuesto** le ayuda a planificar y rastrear gastos mensuales y asegura que no exceda su presupuesto establecido. Este módulo calcula automáticamente basándose en:
- Sus ingresos recurrentes
- Sus gastos recurrentes
- Gastos diarios reales

## 2. Cuándo usar

Use este módulo cuando desee:
- Planificar gastos mensuales
- Controlar que no exceda el presupuesto
- Rastrear tasa de ahorro
- Ver análisis de gastos por categoría
- Comparar presupuestos entre meses

## 3. Pantallas relacionadas

- Crear presupuesto (primera vez o copiar del mes anterior)
- Ver resumen del presupuesto
- Historial de presupuesto por mes
- Sugerencia de copia del mes anterior

## 4. Uso principal

### 4.1 Crear presupuesto por primera vez (Caso A)

1. Vaya a **Funciones** → Seleccione **Presupuesto**
2. Si no existe presupuesto, la aplicación abre automáticamente la pantalla **Crear Presupuesto**
3. La aplicación calcula y muestra automáticamente:
   - **Ingresos Recurrentes**: Total de todos los ingresos recurrentes activos (solo lectura, muestra desglose detallado)
   - **Gastos Recurrentes**: Total de todos los gastos recurrentes activos (solo lectura, muestra desglose detallado)
   - **Presupuesto Total (antes de ahorros)**: Calculado automáticamente = Ingresos Recurrentes - Gastos Recurrentes
4. Ingrese **Tasa de Ahorro**: % de ahorros (0-100%, requerido)
5. Vea **Monto de Ahorro** y **Presupuesto de Gastos** calculados automáticamente
6. Toque **Guardar Presupuesto**

### 4.2 Copiar presupuesto del mes anterior (Caso C)

1. Vaya a **Funciones** → Seleccione **Presupuesto**
2. Si el mes actual no tiene presupuesto, pero el mes anterior sí, la aplicación muestra la pantalla **Sugerencia de Copiar Presupuesto**
3. Seleccione una de las opciones:
   - **Copiar todo el presupuesto del mes anterior**: La aplicación copia automáticamente la tasa de ahorro, recalcula ingresos/gastos recurrentes desde datos actuales y crea el presupuesto inmediatamente
   - **Copiar y Ajustar**: La aplicación navega a la pantalla Crear Presupuesto con la tasa de ahorro prellenada del mes anterior, puede ajustar antes de guardar
   - **Crear Nuevo Presupuesto**: Ejecutar el flujo de crear presupuesto desde cero (Caso A)
4. Si se selecciona "Copiar y Ajustar", ajuste la tasa de ahorro si es necesario
5. Toque **Guardar Presupuesto**

**Nota**: Al copiar, los Ingresos Recurrentes y Gastos Recurrentes se recalculan desde datos recurrentes actuales (no se copian del mes anterior), solo se copia la tasa de ahorro.

### 4.3 Ver resumen del presupuesto (Caso B)

1. Vaya a **Funciones** → Seleccione **Presupuesto**
2. Si el mes actual tiene presupuesto, la aplicación abre la pantalla **Resumen**
3. Ver información:
   - **Presupuesto de Gastos**: Límite de gastos establecido
   - **Usado**: Monto gastado (incluyendo gastos diarios y variaciones de ingresos/gastos)
   - **Restante**: Monto restante en el presupuesto
   - **Tasa de Uso**: % del presupuesto usado (con colores de advertencia)
   - **Variaciones de Ingresos y Gastos del Plan**: Desviaciones del plan original
   - **Gastos Diarios por Categoría**: Análisis detallado de gastos por categoría

### 4.4 Editar presupuesto del mes actual

1. En la pantalla **Resumen del Presupuesto**, toque el botón **"Editar Presupuesto"**
2. La aplicación muestra la pantalla de edición con:
   - **Ingresos Recurrentes** y **Gastos Recurrentes**: Se mantienen los valores antiguos (solo lectura)
   - **Tasa de Ahorro**: Prellenada desde el presupuesto actual (puede editarse)
3. Cambie la tasa de ahorro si es necesario
4. Vea el monto de ahorro y el presupuesto de gastos actualizados automáticamente
5. Toque **"Guardar Presupuesto"**

**Nota**: Al editar, los Ingresos Recurrentes y Gastos Recurrentes no se recalculan (se mantiene la instantánea antigua), solo se actualizan la tasa de ahorro y el presupuesto de gastos.

### 4.5 Ver historial del presupuesto

1. Vaya a **Funciones** → Seleccione **Presupuesto**
2. Seleccione **Historial** del menú
3. Vea la lista de presupuestos para meses pasados
4. Toque un mes para ver detalles

### 4.6 Ver detalles de gastos por categoría

1. Vaya a la pantalla **Resumen del Presupuesto**
2. Desplácese hacia abajo a la sección **Análisis por Categoría**
3. Toque una categoría
4. Vea la lista de gastos en esa categoría

## 5. Ejemplos e ilustraciones de UI

### 5.1 BUDGET-01: Crear presupuesto por primera vez para el mes actual

**Objetivo**: Crear presupuesto por primera vez para que la aplicación calcule y rastree automáticamente los gastos mensuales basándose en ingresos y gastos recurrentes.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Gestión de Presupuesto"
2. La aplicación detecta automáticamente que no hay presupuesto y muestra la pantalla "Crear Presupuesto"
3. Vea información calculada automáticamente: Ingresos Recurrentes, Gastos Recurrentes, Presupuesto Total (antes de ahorros)
4. Ingrese tasa de ahorro: 20
5. Vea el monto de ahorro y el presupuesto de gastos calculados automáticamente
6. Toque el botón "Guardar Presupuesto"

**Resultado**: Presupuesto guardado para el mes actual, navega automáticamente a la pantalla "Resumen del Presupuesto".

**Ilustración de UI**:

```text
[ Tarjeta: Crear Presupuesto Noviembre 2025 ]
+------------------------------------------------+
||                                                |
|| Ingresos Recurrentes                €1,080         |
||  • Mi Salario (Mensual)         €1,080         |
||                                                |
|| Gastos Recurrentes              €824          |
||  • Electricidad (Mensual)          €31        |
||  • Agua (Mensual)                €15        |
||  • Matrícula para BN (Mensual)       €245       |
||  • Desayuno y Café (Semanal x 4) €32       |
||  • Préstamo de Vivienda (Mensual)     €378      |
||                                                |
|| (Estos datos se recuperan automáticamente)        |
+------------------------------------------------+

[ Tarjeta: Presupuesto Total (antes de ahorros) ]
 ------------------------------------------------
||   €1,080 (Ingresos Recurrentes)                   |
|| - €824 (Gastos Recurrentes)                    |
||-----------------------------------------------|
|| = €256 EUR                                     |
 ------------------------------------------------

[ Tarjeta: Tasa de Ahorro ]
 ------------------------------------------------
|| ¿Cuánto desea ahorrar?                 |
||                                                |
|| Tasa de Ahorro (%)                               |
|| [  Entrada (requerido): 20  ]                    |
||                                                |
|| → Equivale a: €51                              |
 ------------------------------------------------

[ Tarjeta: Presupuesto de Gastos ]
 ------------------------------------------------
||    €256 (Presupuesto Total (antes de ahorros))       |
|| -  €51 (Monto de Ahorro)                        |
||-----------------------------------------------|
|| = €204 EUR                                     |
||                                                |
|| (Incluye comida, transporte, café, compras pequeñas...)
 ------------------------------------------------

[ Botón ]
 -------------------------------
||      Guardar Presupuesto              |
 -------------------------------
```

---

### 5.2 BUDGET-02: Ver resumen del presupuesto del mes actual

**Objetivo**: Ver situación de gastos en comparación con el presupuesto establecido, incluyendo montos usados, montos restantes y análisis por categoría.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Gestión de Presupuesto"
2. La aplicación detecta automáticamente que existe presupuesto y muestra la pantalla "Resumen del Presupuesto"
3. Vea Tarjeta 1 - Presupuesto Mensual: Presupuesto de Gastos, Usado, Restante, Tasa de Uso
4. Vea Tarjeta 2 - Variaciones de Ingresos y Gastos del Plan
5. Vea Tarjeta 3 - Gastos Diarios por Categoría
6. (Opcional) Haga clic en "Presupuesto de Gastos ›" para ver el diálogo detallado con el cálculo del presupuesto

**Resultado**: Muestra información completa del presupuesto del mes actual con barra/anillo de progreso y colores apropiados.

**Ilustración de UI**:

```text
[ Tarjeta 1 – Presupuesto Noviembre 2025 ]
┌──────────────────────────────────────────────┐
│ Presupuesto Noviembre 2025                         │
│                                             │
│ Presupuesto de Gastos ›      €204                 │
│ Usado                  €32                   │
│  • Gastos Diarios              €43          │   
│  • Variación de Ingresos      -€144              │
│  • Variación de Gastos       +€7               │
│ Restante              €94                 │
│                                             │
│                    15.4%                    │
│   (Ha usado 15.4% del presupuesto de gastos de este mes)
│   (Está en proceso de agotar el presupuesto de gastos de este mes)
│                                             │
│                               [Ver Historial]│
└──────────────────────────────────────────────┘

[ Tarjeta 2 – Variaciones de Ingresos y Gastos del Plan ]
┌──────────────────────────────────────────────┐
│ Variaciones de Ingresos y Gastos del Plan        │
│                                              │
│ Ingresos Recurrentes                             │
│  • Mi Salario                 +€72           │
│    (€432 > €360)                             │
│                                              │
│ Gastos Recurrentes                           │
│  • Matrícula para BN              -€4          │
│    (€245 > €252)                             │
│                                              │
│ Variación Total de Ingresos:        +€216          │
│ Variación Total de Gastos:        -€7          │
└──────────────────────────────────────────────┘

[ Tarjeta 3 – Gastos Diarios por Categoría ]
┌──────────────────────────────────────────────┐
│ Gastos Diarios por Categoría                   │
│ (Comida, Transporte, Café, compras pequeñas...)
│                                             │
│ Gastos Diarios Totales: €43                    │
│                                             │
│ Comida              €22    50% [█████---------]│
│ Transporte     €11    25% [███-----------]│
│ Café             €7     17% [██------------]│
│ Compras Pequeñas     €4     8%  [█-------------]│
└──────────────────────────────────────────────┘
```

---

### 5.3 BUDGET-03: Editar presupuesto del mes actual

**Objetivo**: Ajustar la tasa de ahorro para cambiar el presupuesto de gastos del mes actual.

**Pasos**:
1. En la pantalla "Resumen del Presupuesto", toque el botón "Editar Presupuesto"
2. La aplicación muestra la pantalla de edición (similar a la pantalla Crear Presupuesto)
3. Vea información actual: Ingresos Recurrentes, Gastos Recurrentes (se mantienen los valores antiguos)
4. Cambie la tasa de ahorro a 25
5. Vea el monto de ahorro y el presupuesto de gastos actualizados automáticamente
6. Toque el botón "Guardar Presupuesto"

**Resultado**: Presupuesto actualizado, regresa a la pantalla "Resumen del Presupuesto" con nuevos valores.

**Ilustración de UI**: Similar a BUDGET-01 (pantalla Crear Presupuesto), pero los valores de Ingresos Recurrentes y Gastos Recurrentes son solo lectura y se mantienen del presupuesto antiguo.

---

### 5.4 BUDGET-04: Copiar presupuesto del mes anterior cuando comienza nuevo mes

**Objetivo**: Reutilizar el presupuesto del mes anterior para ahorrar tiempo al crear nuevo presupuesto, con opción de ajustar si es necesario.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Gestión de Presupuesto"
2. La aplicación detecta automáticamente que el mes actual no tiene presupuesto, pero el mes anterior sí, muestra la pantalla "Sugerencia de Copiar Presupuesto"
3. Seleccione "Copiar y Ajustar"
4. La aplicación navega a la pantalla Crear Presupuesto con la tasa de ahorro prellenada del mes anterior
5. (Opcional) Ajuste la tasa de ahorro si es necesario
6. Toque el botón "Guardar Presupuesto"

**Resultado**: Nuevo presupuesto creado para el mes actual, navega automáticamente a la pantalla "Resumen del Presupuesto".

**Ilustración de UI**:

```text
[ PANTALLA ]  Presupuesto Diciembre 2025
┌──────────────────────────────────────────────┐
│ Diciembre 2025 no tiene presupuesto                 │
│                                              │
│ ¿Cómo desea crear el presupuesto del nuevo mes?│
├──────────────────────────────────────────────┤
│                                              │
│ 📝 Copiar y Ajustar ›                          │
│    Nota: Copiar y ajustar presupuesto Noviembre 2025│
│                                              │
├──────────────────────────────────────────────┤
│                                              │
│ ➕ Crear Nuevo Presupuesto ›                      │
│   Nota: Ejecutar flujo de crear presupuesto nuevamente        │
│                                              │
└──────────────────────────────────────────────┘
```

Después de seleccionar "Copiar y Ajustar", se muestra la pantalla Crear Presupuesto similar a BUDGET-01, pero la tasa de ahorro está prellenada del mes anterior.

## 6. Lógica y reglas

### 6.1 Casos

- **Caso A**: Crear presupuesto por primera vez (sin presupuesto para ningún mes)
- **Caso B**: El mes actual tiene presupuesto → Mostrar resumen
- **Caso C**: El mes actual no tiene, pero el mes anterior sí → Sugerencia de copia

### 6.2 Cálculo automático

- **Ingresos Recurrentes**: Total de todos los `recurring_income` activos
- **Gastos Recurrentes**: Total de todos los `recurring_expense` activos
- **Gastos Diarios**: Total de `daily_expense` en el mes
- **Presupuesto Total**: Ingresos Recurrentes + Ingresos Extra
- **Ahorros**: Presupuesto Total × Tasa de Ahorro

### 6.3 Integración con otros módulos

- Al confirmar ingreso recurrente → Actualizar presupuesto automáticamente
- Al confirmar gasto recurrente → Actualizar presupuesto automáticamente
- Los gastos diarios se calculan automáticamente en el presupuesto

### 6.4 Advertencia de presupuesto excedido

- La aplicación muestra advertencia cuando los gastos exceden el presupuesto
- La advertencia se muestra en la pantalla de inicio y en notificaciones

### 6.5 Instantánea

- Al crear el presupuesto, la aplicación crea una instantánea de elementos de ingresos/gastos para guardar el estado en ese momento
- La instantánea se usa para comparación y análisis

## 7. Notas importantes

- **Un presupuesto por mes**: Debe crear presupuesto para cada mes
- **Editar presupuesto**: Puede editar el presupuesto del mes actual cambiando la tasa de ahorro. Los Ingresos Recurrentes y Gastos Recurrentes permanecen sin cambios (instantánea) para asegurar precisión
- **Actualización automática**: El presupuesto se actualiza automáticamente cuando confirma ingresos/gastos
- **Copiar del mes anterior**: La función de copia le ayuda a ahorrar tiempo al crear el presupuesto

