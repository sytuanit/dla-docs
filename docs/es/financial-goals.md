# Objetivos Financieros

## 1. Propósito

El módulo **Objetivos Financieros** le ayuda a:
- Establecer objetivos financieros (ej. comprar casa, comprar auto)
- Planificar finanzas para alcanzar objetivos
- Evaluar supuestos financieros
- Comparar escenarios de préstamos
- Rastrear progreso del objetivo

## 2. Cuándo usar

Use este módulo cuando desee:
- Planificar para un objetivo financiero importante
- Evaluar capacidad de préstamo para comprar activos
- Comparar opciones financieras
- Rastrear progreso de ahorro

## 3. Pantallas relacionadas

- Crear objetivo financiero (3 pasos)
- Detalles del objetivo y planes
- Ver plan de préstamo
- Evaluar supuestos
- Evaluar supuestos y préstamo

## 4. Uso principal

### 4.1 Crear objetivo financiero (3 pasos)

#### Paso 1: Ingresar plan financiero

1. Vaya a **Funciones** → Seleccione **Planificación y Supuestos**
2. Toque el botón **➕ Agregar Nuevo** (FAB)
3. Vea información completada automáticamente:
   - **Ingreso Promedio**: Recuperado automáticamente de ingresos recurrentes activos (puede hacer clic para ver desglose)
   - **Gastos Fijos**: Recuperado automáticamente de gastos recurrentes activos + pagos de préstamos (puede hacer clic para ver desglose)
   - **Saldo Actual**: Recuperado automáticamente del saldo actual
4. Ingrese **Gastos de Vida**: Gastos mensuales de vida (comida, transporte, etc.)
5. Vea pronóstico calculado automáticamente:
   - Después de 12 meses
   - Después de 24 meses
   - Después de 36 meses
   (si se mantienen los niveles actuales de ingresos y gastos)
6. Toque **Continuar**

#### Paso 2: Ingresar información del objetivo

1. Ingrese **Nombre del Objetivo**: (ej. "Comprar Casa")
2. Ingrese **Monto Necesario**: Monto total necesario para alcanzar el objetivo
3. Vea **Pago Inicial**: Completado automáticamente desde el saldo actual (puede editarse)
4. Toque **Continuar**

#### Paso 3: Verificar capacidad de alcanzar objetivo

1. Vea información del objetivo: Nombre, Valor del Objetivo, Pago Inicial, Brecha Restante
2. Vea finanzas actuales: Ingreso Promedio, Gastos Promedio, Ahorros Promedio
3. Vea conclusión:
   - "Alcanzará el objetivo en ~X años" (si ahorros > 0)
   - "Con la situación actual, no puede alcanzar el objetivo sin pedir préstamo o mejorar finanzas" (si ahorros <= 0)
4. Vea opciones siguientes:
   - **Ver Opción de Préstamo**: Evaluar capacidad de préstamo
   - **Crear Supuesto de Ingresos/Gastos**: Simular mejora financiera
   - **Combinar Supuesto + Préstamo**: Escenario óptimo
5. Toque **Guardar Objetivo** (puede guardar ahora o crear plan más tarde)

### 4.2 Ver lista y detalles del objetivo

1. Vaya a **Funciones** → Seleccione **Planificación y Supuestos**
2. Vea lista de objetivos creados:
   - Cada objetivo muestra: Nombre, Valor del Objetivo, Pago Inicial Realizado, Brecha Restante
3. (Opcional) Use la barra de búsqueda para encontrar objetivo por nombre
4. Toque un objetivo para ver detalles:
   - **Información del Objetivo**: Nombre, Valor del Objetivo, Pago Inicial, Brecha Restante
   - **Plan Financiero (línea base)**: Haga clic para ver diálogo con ingreso promedio, gastos, ahorros
   - **Lista de Planes Guardados**: Planes de préstamo, supuestos o combinaciones que se han creado

### 4.3 Crear plan de préstamo para objetivo

1. En la pantalla de detalles del objetivo, toque el botón **➕ Agregar Nuevo**
2. La aplicación muestra diálogo para seleccionar tipo de plan, seleccione **"Préstamo"**
3. Ingrese información del préstamo: Monto del Préstamo, Tasa de Interés, Plazo del Préstamo, Nombre del Plan
4. Vea resultados calculados automáticamente: Pago Mensual, Monto Total a Pagar, Tiempo para Alcanzar Objetivo, Asequibilidad
5. Toque **Guardar Plan**

### 4.4 Crear supuesto de ingresos/gastos

1. En la pantalla de detalles del objetivo, toque el botón **➕ Agregar Nuevo**
2. La aplicación muestra diálogo para seleccionar tipo de plan, seleccione **"Supuesto"**
3. Ingrese supuestos:
   - **Aumentar Ingresos**: Monto adicional (o deje en blanco si no hay aumento)
   - **Reducir Gastos**: Monto reducido (o deje en blanco si no hay reducción)
   - Nombre del supuesto
4. Vea resultados calculados automáticamente: Nuevo Ingreso, Nuevos Gastos, Nuevos Ahorros, Nuevo Tiempo para Alcanzar Objetivo
5. Toque **Guardar Supuesto**

### 4.5 Eliminar objetivo financiero

1. Vaya a la pantalla de detalles del objetivo
2. Toque el botón **Eliminar** (icono de eliminar) en la esquina superior derecha de la tarjeta del objetivo
3. La aplicación muestra diálogo de confirmación
4. Toque **Eliminar** para confirmar

**Nota**: Eliminar el objetivo elimina todos los planes relacionados y no se puede deshacer.

## 5. Ejemplos e ilustraciones de UI

### 5.1 PLANNING-01: Crear nuevo objetivo financiero (Comprar Casa)

**Objetivo**: Crear objetivo financiero para planificar y simular la capacidad de alcanzar ese objetivo.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Planificación y Supuestos"
2. Toque el botón "➕ Agregar Nuevo"
3. **Paso 1**: Ingresar plan financiero (ver información completada automáticamente, ingresar gastos de vida, ver pronóstico)
4. **Paso 2**: Ingresar información del objetivo (nombre, monto necesario, pago inicial)
5. **Paso 3**: Verificar capacidad de alcanzar objetivo (ver conclusión y opciones)
6. Toque "Guardar Objetivo"

**Resultado**: Objetivo guardado, regresa a la pantalla de lista de objetivos.

**Ilustración de UI - Paso 1: Ingresar plan financiero**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Crear Objetivo (1/3)            │
├─────────────────────────────────────────┤
│  Plan Financiero                          │
│                                         │
│  Ingreso Promedio *                        │
│  [€1,080]                               │
│  (Por defecto de elementos recurrentes)          │
│  [Ver Desglose]                        │
│                                         │
│  Gastos Fijos *                        │
│  [€824]                                 │
│  (Por defecto de elementos recurrentes)          │
│  [Ver Desglose]                        │
│                                         │
│  Gastos de Vida *                       │
│  [€180]                                 │
│  (Incluye comida, transporte,...)     │
│                                         │
│  Saldo Actual *                       │
│  [€1,800]                               │
│  (Por defecto del saldo actual)         │
│                                         │
│  Pronóstico                                │
│  ┌───────────────────────────────────┐ │
│  │ Después de 12 meses: €2,664             │ │
│  │ Después de 24 meses: €3,528             │ │
│  │ Después de 36 meses: €4,392             │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Continuar] [Cancelar]                     │
└─────────────────────────────────────────┘
```

**Ilustración de UI - Paso 2: Ingresar información del objetivo**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Crear Objetivo (2/3)            │
├─────────────────────────────────────────┤
│  Ingresar Información del Objetivo                 │
│                                         │
│  Nombre del Objetivo *                            │
│  [Comprar Casa]                            │
│  (Ejemplo: Comprar Casa, Comprar Auto,...)     │
│                                         │
│  Monto Necesario *                         │
│  [€72,000]                              │
│  (Monto total necesario para alcanzar el objetivo)   │
│                                         │
│  Pago Inicial                            │
│  [€1,800]                               │
│  (Por defecto = Saldo Actual)            │
│                                         │
│  [Continuar] [Atrás]                       │
└─────────────────────────────────────────┘
```

**Ilustración de UI - Paso 3: Verificar capacidad de alcanzar objetivo**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Crear Objetivo (3/3)            │
├─────────────────────────────────────────┤
│  Verificar Capacidad de Alcanzar Objetivo      │
│                                         │
│  Información del Objetivo                       │
│  ┌───────────────────────────────────┐ │
│  │ Objetivo: Comprar Casa                     │ │
│  │ Valor del Objetivo: €72,000                 │ │
│  │ Pago Inicial: €1,800                │ │
│  │ Brecha Restante: €70,200              │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Sus Finanzas Actuales                  │
│  ┌───────────────────────────────────┐ │
│  │ Ingreso Promedio: €1,080              │ │
│  │ Gastos Promedio: €1,004             │ │
│  │ Ahorros Promedio: €76                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Si mantiene la situación actual           │
│  Ahorros mensuales: €76                   │
│  Necesitará aproximadamente: ~77 años │
│                                         │
│  Conclusión                              │
│  Con la situación actual, no puede     │
│  alcanzar el objetivo sin pedir préstamo o  │
│  mejorar finanzas                     │
│                                         │
│  ¿Qué desea hacer a continuación?         │
│  ┌───────────────────────────────────┐ │
│  │ Ver Opción de Préstamo ›                 │ │
│  │ (Si desea ver si el préstamo ayuda...)│ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ Crear Supuesto de Ingresos/Gastos ›│ │
│  │ (Si desea intentar mejorar...) │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Guardar Objetivo] [Atrás]                     │
└─────────────────────────────────────────┘
```

---

### 5.2 PLANNING-02: Ver lista y detalles del objetivo

**Objetivo**: Ver lista de objetivos creados y ver detalles de cada objetivo con planes guardados.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Planificación y Supuestos"
2. Vea lista de objetivos creados
3. (Opcional) Use la barra de búsqueda para encontrar objetivo por nombre
4. Toque un objetivo para ver detalles
5. Vea información del objetivo, plan financiero (línea base) y lista de planes guardados

**Resultado**: Muestra información completa del objetivo y planes guardados.

**Ilustración de UI - Lista de Objetivos**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Planificación y Supuestos       │
├─────────────────────────────────────────┤
│  [🔍 Buscar por nombre del objetivo]               │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Comprar Casa                           │ │
│  │ 🎯 Valor del Objetivo: €72,000             │ │
│  │ 💰 Pago Inicial: €1,800             │ │
│  │ ⚠️ Brecha Restante: €70,200           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Comprar Auto                             │ │
│  │ 🎯 Valor del Objetivo: €18,000              │ │
│  │ 💰 Pago Inicial: €720               │ │
│  │ ⚠️ Brecha Restante: €17,280           │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [➕ Agregar Nuevo]                           │
└─────────────────────────────────────────┘
```

**Ilustración de UI - Detalles del Objetivo**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Objetivo: Comprar Casa              │
├─────────────────────────────────────────┤
│  Información del Objetivo                       │
│  ┌───────────────────────────────────┐ │
│  │ 🎯 Valor del Objetivo: €72,000              │ │
│  │ 💰 Pago Inicial: €1,800             │ │
│  │ ⚠️ Brecha Restante: €70,200           │ │
│  │                                    │ │
│  │ [🗑️ Eliminar]                         │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [📊 Ver Plan Financiero (línea base)]     │
│                                         │
│  Lista de Planes Guardados                       │
│  ┌───────────────────────────────────┐ │
│  │ Préstamo 80% del valor de la casa            │ │
│  │ Préstamo: €54,000                      │ │
│  │ Tasa de Interés: 8%/año             │ │
│  │ Plazo: 20 años                     │ │
│  │ [Ver Detalles]                     │ │
│  └───────────────────────────────────┘ │
│  ┌───────────────────────────────────┐ │
│  │ Aumentar Ingresos + Reducir Gastos│ │
│  │ Nuevo Ingreso: €1,260                  │ │
│  │ Nuevos Gastos: €968                │ │
│  │ Nuevos Ahorros: €292                   │ │
│  │ [Ver Detalles]                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [➕ Agregar Nuevo]                           │
└─────────────────────────────────────────┘
```

---

### 5.3 PLANNING-03: Crear plan de préstamo para objetivo

**Objetivo**: Crear plan de préstamo para ver si el préstamo ayuda a acortar el tiempo para alcanzar el objetivo y asequibilidad.

**Pasos**:
1. En la pantalla de detalles del objetivo, toque el botón "➕ Agregar Nuevo"
2. Seleccione "Préstamo" en el diálogo
3. Ingrese información del préstamo: Monto del Préstamo, Tasa de Interés, Plazo del Préstamo, Nombre del Plan
4. Vea resultados calculados automáticamente
5. Toque "Guardar Plan"

**Resultado**: Plan de préstamo guardado y aparece en la lista de planes.

**Ilustración de UI**: Pantalla crear plan de préstamo (detalles en pantallas relacionadas).

---

### 5.4 PLANNING-04: Crear supuesto de ingresos/gastos para mejorar capacidad de alcanzar objetivo

**Objetivo**: Crear supuesto sobre aumentar ingresos o reducir gastos para ver si esto ayuda a alcanzar el objetivo más rápido.

**Pasos**:
1. En la pantalla de detalles del objetivo, toque el botón "➕ Agregar Nuevo"
2. Seleccione "Supuesto" en el diálogo
3. Ingrese supuestos: Aumentar Ingresos (si hay), Reducir Gastos (si hay), Nombre del Supuesto
4. Vea resultados calculados automáticamente
5. Toque "Guardar Supuesto"

**Resultado**: Supuesto guardado y aparece en la lista de planes.

**Ilustración de UI**: Pantalla crear supuesto (detalles en pantallas relacionadas).

---

### 5.5 PLANNING-05: Eliminar objetivo financiero

**Objetivo**: Eliminar objetivo financiero cuando ya no sea necesario.

**Pasos**:
1. Vaya a la pantalla de detalles del objetivo
2. Toque el botón "Eliminar" (icono de eliminar)
3. Confirme eliminación en el diálogo

**Resultado**: Objetivo y todos los planes relacionados han sido eliminados.

**Ilustración de UI**: Diálogo confirmar eliminar objetivo.

## 6. Lógica y reglas

### 6.1 Cálculo de pronóstico

- Pronóstico basado en:
  - Ingresos - Gastos Fijos - Gastos de Vida = Ahorros/mes
  - Saldo Actual + (Ahorros/mes × Número de meses)

### 6.2 Objetivos

- Brecha Restante = Monto Necesario - Pago Inicial
- Tiempo Estimado = Brecha Restante / Ahorros Promedio (meses)
- Si ahorros promedio <= 0: No puede alcanzar el objetivo sin pedir préstamo o mejorar finanzas

### 6.3 Planes de Préstamo

- Cálculo basado en:
  - Monto del préstamo
  - Tasa de interés
  - Plazo
  - Crear calendario de pagos automáticamente

### 6.4 Supuestos Financieros

- Evalúe supuestos como:
  - Aumentar/reducir ingresos
  - Aumentar/reducir gastos
  - Cambiar tasa de interés
- Vea impacto en la capacidad de alcanzar objetivo

## 7. Notas importantes

- **Módulo Premium Requerido**: Esta función es solo para usuarios Premium
- **El pronóstico es solo como referencia**: Basado en supuesto de ingresos y gastos estables
- **Puede crear múltiples planes**: Puede crear múltiples planes (préstamo, supuesto, combinación) para comparar
- **La línea base se guarda**: El plan financiero inicial (línea base) se guarda al crear el objetivo, se usa para comparar con planes posteriores
- **Cálculo Automático**: Los ingresos y gastos fijos se recuperan automáticamente de elementos recurrentes activos, incluyendo pagos de préstamos bancarios
- **Eliminar Objetivo**: Al eliminar el objetivo, todos los planes relacionados también se eliminan y no se pueden restaurar

