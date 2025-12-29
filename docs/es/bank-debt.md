# Préstamos Bancarios

## 1. Propósito

El módulo **Préstamos Bancarios** le ayuda a gestionar préstamos bancarios, incluyendo:
- Rastrear monto del préstamo, tasa de interés, plazo
- Gestionar calendario de pagos
- Calcular intereses por período (si aplica)
- Gestionar multas por pago tardío
- Liquidación anticipada (si es necesario)

## 2. Cuándo usar

Use este módulo cuando tenga:
- Préstamos bancarios
- Necesite rastrear calendario de pagos
- Desee calcular intereses y multas
- Necesite recordatorios cuando el pago está vencido

## 3. Pantallas relacionadas

- Lista de préstamos
- Agregar nuevo préstamo (4 pasos)
- Editar préstamo
- Detalles del préstamo y calendario de pagos
- Liquidación anticipada

## 4. Uso principal

### 4.1 Agregar nuevo préstamo (4 pasos)

#### Paso 1: Información básica

1. Vaya a **Funciones** → Seleccione **Préstamos Bancarios**
2. Toque el botón **+** (FAB)
3. Complete la información:
   - **Banco**: Seleccione banco o cree nuevo
   - **Nombre del Préstamo**: (ej. "Préstamo Hipotecario")
   - **Monto del Préstamo**: Monto del capital
   - **Fecha de Desembolso**: Fecha en que se recibió el dinero
   - **Plazo**: Número de años
   - **Tipo de Interés**: Tasa promocional/variable o Tasa fija
4. Toque **Siguiente**

#### Paso 2: Configurar tasa de interés

**Si selecciona "Tasa Promocional/Variable":**
- Active **Tiene Tasa Promocional** (si aplica)
- Ingrese **Meses Promocionales** y **Tasa Promocional**
- Agregue períodos de tasa variable:
  - Seleccione año y rango de meses
  - Ingrese tasa de interés (%/año)
  - Seleccione **Variable** o **Fija**

**Si selecciona "Tasa Fija":**
- Ingrese **Tasa Fija** (%/año)

Toque **Siguiente**

#### Paso 3: Configurar multas

1. Active **Tiene Multa por Pago Tardío** (si aplica)
2. Agregue períodos de multa:
   - Seleccione año y rango de meses
   - Ingrese **Tasa de Multa** (%/año)
3. Toque **Siguiente**

#### Paso 4: Confirmar y guardar

1. Revise la información:
   - Monto total a pagar
   - Calendario de pagos esperado
2. Toque **Guardar**

### 4.2 Ver detalles del préstamo

1. Vaya a la lista de préstamos
2. Toque un préstamo
3. Vea la información:
   - Información básica
   - Calendario de pagos
   - Monto pagado / Restante
   - Tasa de interés y multas

### 4.3 Marcar período de pago como pagado

1. Vaya a los detalles del préstamo
2. Encuentre el período de pago vencido (badge "No Pagado")
3. Toque **Marcar como Pagado**
4. Complete la información:
   - **Fecha de Pago Real**: Fecha pagada (por defecto = hoy)
   - **Intereses Pagados Reales**: Intereses realmente pagados (por defecto = intereses planificados)
   - **Nota**: (opcional)
5. Vea **Pago Total Real** calculado automáticamente (capital + intereses reales)
6. Toque **Confirmar**

### 4.4 Actualizar tasa de interés actual

1. Vaya a los detalles del préstamo (solo se muestra si actualmente está en período de tasa variable)
2. Toque **Actualizar Tasa de Interés Actual**
3. Complete la información:
   - **Nueva Tasa de Interés**: Nueva tasa de interés (%/año)
   - **Fecha Efectiva**: Fecha para comenzar a aplicar nueva tasa (por defecto = inicio del período actual)
   - **Nota**: (opcional)
4. Toque **Guardar**
5. Los períodos no pagados desde el período actual en adelante se actualizarán con la nueva tasa de interés

### 4.5 Liquidación anticipada

1. Vaya a los detalles del préstamo
2. Toque **Calcular Monto de Liquidación**
3. **Paso 1 - Ingresar información de prepago:**
   - Seleccione método: **Pago Parcial** o **Liquidación Completa**
   - Seleccione fecha de prepago (por defecto = hoy)
   - Ingrese monto de prepago (si es parcial)
   - Vea **Multa por Pago Anticipado** calculada automáticamente
4. Toque **Siguiente**
5. **Paso 2 - Comparar opciones:**
   - Vea comparación entre "Sin Prepago" y "Prepago"
   - Vea resultados: Ahorro en intereses, reducción de tiempo
6. Toque **Confirmar Prepago**

### 4.6 Editar préstamo

1. Vaya a los detalles del préstamo
2. Toque **Editar** (solo editar nombre, nota, banco)
3. Edite la información editable:
   - **Nombre del Préstamo**: Se puede editar
   - **Banco**: Se puede cambiar
   - **Nota**: Se puede editar
   - **Monto del Préstamo, Fecha de Desembolso, Plazo, Tasa de Interés**: Solo se pueden editar si aún no se han realizado pagos
4. Toque **Guardar**

## 5. Ejemplos e ilustraciones de UI

### LOAN-01: Crear nuevo préstamo (Préstamo Hipotecario con Tasa de Interés Promocional)

**Objetivo**: Crear nuevo préstamo para rastrear préstamo hipotecario, tasa de interés promocional y calendario de pagos mensuales.

**Pasos**:
1. Vaya a **Funciones** → Seleccione **Préstamos Bancarios**
2. Toque el botón **+** (FAB) para agregar nuevo préstamo
3. **Paso 1 - Información básica:**
   - Seleccione banco: Banco Santander
   - Ingrese nombre: "Préstamo Hipotecario - Apartamento Centro"
   - Ingrese monto del préstamo: €180,000
   - Seleccione fecha de desembolso: 01/04/2023
   - Ingrese plazo: 10 años (calculado automáticamente = 120 períodos)
   - Seleccione horarios de notificación: 10:00 y 19:00
   - Seleccione tipo de interés: "Saldo Decreciente"
   - Toque **Siguiente**
4. **Paso 2 - Configurar tasa de interés:**
   - Active "Tiene Período de Interés Promocional"
   - Ingrese: Primeros 6 meses @ 6.0%/año
   - Agregue períodos subsiguientes:
     - Año 1 (meses 7-12): 9.0%/año, variable
     - Año 2 (meses 13-24): 9.5%/año, variable
     - Año 3 en adelante: 10.0%/año, variable
   - Toque **Siguiente**
5. **Paso 3 - Configurar multa por pago anticipado:**
   - Active "Aplicar Multa por Pago Anticipado"
   - Ingrese multas: Años 1-3: 2.0%, Años 4-5: 1.5%, Año 6+: 1.0%
   - Toque **Siguiente**
6. **Paso 4 - Confirmar:**
   - Revise información resumida
   - Toque **Crear Préstamo**

**Resultado**: Préstamo creado exitosamente, calendario de pagos de 120 períodos creado automáticamente, notificaciones programadas.

**Wireframe - Paso 1: Información básica**

```text
┌─────────────────────────────────────────┐
│ <  Agregar Préstamo                              │
├─────────────────────────────────────────┤
│ Nombre del Préstamo *                              │
│ [Préstamo Hipotecario - Apartamento Centro]        │
│                                          │
│ Banco *                                    │
│ [Banco Santander ▼] [+ Crear Nuevo]       │
│                                          │
│ Monto del Préstamo *                            │
│ [€180,000]                               │
│                                          │
│ Fecha de Desembolso *                      │
│ [01/04/2023] [📅]                        │
│                                          │
│ Plazo del Préstamo (años) *                       │
│ [10] años                               │
│ Nota: La aplicación calcula automáticamente = 120 períodos  │
│                                          │
│ Hora de Notificación 1 *                    │
│ [10:00] [🕐]                             │
│                                          │
│ Hora de Notificación 2 *                    │
│ [19:00] [🕐]                             │
│                                          │
│ Tipo de Interés *                          │
│ ● Saldo Decreciente                      │
│ ○ Tasa Fija para Todo el Plazo             │
│                                          │
│ [SIGUIENTE] [CANCELAR]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-02: Ver lista y detalles de préstamos

**Objetivo**: Ver resumen de préstamos, filtrar por estado, buscar y ver detalles de cada préstamo.

**Pasos**:
1. Vaya a **Funciones** → Seleccione **Préstamos Bancarios**
2. Vea la pantalla de lista con filtros "Activo" (por defecto) y "Completado"
3. Cambie entre filtros para ver diferentes resúmenes
4. Use la barra de búsqueda: Ingrese "Centro"
5. Toque el préstamo para ver detalles
6. Vea el calendario de pagos con períodos pagados, período actual y períodos futuros
7. Use la barra de búsqueda en el calendario de pagos: Ingrese "9/2024"

**Resultado**: La lista se muestra correctamente por filtro, los detalles del préstamo muestran información completa y calendario de pagos.

**Wireframe - Lista de Préstamos**

```text
┌─────────────────────────────────────────┐
│ <  Gestión de Préstamos Bancarios                 │
├─────────────────────────────────────────┤
│ [Activo] [Completado]                    │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ Saldo Actual: €148,050          │  │
│ │ Préstamo Original Total: €180,000      │  │
│ │ Intereses Pagados: €1,548              │  │
│ │ Activo: 1 préstamo                     │  │
│ └─────────────────────────────────────┘  │
│                                          │
│ [🔍 Buscar (nombre del préstamo, banco)]            │
│                                          │
│ ┌─────────────────────────────────────┐  │
│ │ [ICON] Banco Santander  [Activo]    │  │
│ │ Préstamo Hipotecario - Apartamento Centro      │  │
│ │ Saldo: €148,050                   │  │
│ │ Original: €180,000                 │  │
│ │ Progreso: 8 / 120 períodos          │  │
│ │ Fecha Final: 01/04/2033               │  │
│ └─────────────────────────────────────┘  │
│                                          │
│                                    [+]   │
└─────────────────────────────────────────┘
```

**Wireframe - Detalles del Préstamo**

```text
┌─────────────────────────────────────────┐
│ <  Detalles del Préstamo                         │
├─────────────────────────────────────────┤
│ [ICON] Banco Santander          [Editar]  │
│ Préstamo Hipotecario - Apartamento Centro           │
│ [Activo]                                 │
│                                          │
│ Préstamo Original: €180,000                 │
│ Saldo Actual: €148,050               │
│ Períodos Pagados: 8 / 120                    │
│ Intereses Pagados: €1,548                    │
│ Tasa de Interés Actual: 9.0%/año        │
│                                          │
│ [Actualizar Interés] [Calcular Liquidación]│
│                                          │
│ Calendario de Pagos                         │
│ [🔍 Buscar período (ej. "5/2025")]     │
│                                          │
│ Período 1 – 05/2023 [Pagado]                │
│ Total: €1.94k • Capital: €900 • Intereses: €1.04k│
│                                          │
│ Período 9 – 01/2024 [No Pagado]            │
│ Capital: €900                        │
│ Intereses: €1,035                        │
│ Total: €1,935                            │
│ Fecha de Vencimiento: 15/01/2024                     │
│ [Marcar como Pagado]                           │
│                                          │
│ Período 10 – 02/2024 [No Vencido]            │
│ Total: €1.94k • Capital: €900 • Intereses: €1.04k│
└─────────────────────────────────────────┘
```

---

### LOAN-03: Marcar período de pago como pagado (Registrar pago)

**Objetivo**: Marcar período de pago como "Pagado" después de realizar el pago al banco.

**Pasos**:
1. Vaya a los detalles del préstamo
2. Encuentre el período actual (Período 9) con badge "No Pagado"
3. Toque **Marcar como Pagado**
4. Complete la información:
   - Fecha de pago real: 15/01/2024 (por defecto = hoy)
   - Intereses pagados reales: €1,035 (por defecto = intereses planificados)
   - Nota: (opcional)
5. Vea el pago total real calculado automáticamente
6. Toque **Confirmar**

**Resultado**: Período 9 actualizado a "Pagado", el saldo disminuye, los períodos pagados aumentan, el saldo actual disminuye.

**Wireframe - Diálogo Marcar como Pagado**

```text
┌─────────────────────────────────────────┐
│ Marcar como Pagado                             │
├─────────────────────────────────────────┤
│ Período 9 – 01/2024          [No Pagado]   │
│                                          │
│ Fecha de Vencimiento (planificada): 15/01/2024          │
│ Capital (fijo): €900                │
│                                          │
│ Fecha de Pago Real *                    │
│ [15/01/2024] [📅]                        │
│                                          │
│ Intereses Pagados Reales *                   │
│ [€1,035]                                 │
│ Nota: Intereses planificados: €1,035           │
│                                          │
│ Pago Total Real =                   │
│   €900 (Capital)                    │
│ + €1,035 (Intereses Reales)              │
│ ────────────────────────────────        │
│ = €1,935                                 │
│                                          │
│ Nota (opcional)                          │
│ [Pagado €50 menos, recibió reducción de intereses...]│
│                                          │
│ [CANCELAR] [CONFIRMAR]                       │
└─────────────────────────────────────────┘
```

---

### LOAN-04: Actualizar tasa de interés actual (Cuando el banco ajusta tasa variable)

**Objetivo**: Actualizar nueva tasa de interés cuando el banco anuncia ajuste de tasa variable.

**Pasos**:
1. Vaya a los detalles del préstamo
2. Vea "Tasa de Interés Actual: 9.0%/año"
3. Toque **Actualizar Tasa de Interés Actual** (solo se muestra si actualmente está en período de tasa variable)
4. Complete la información:
   - Nueva tasa de interés: 10.5%/año
   - Fecha efectiva: 15/01/2024 (por defecto = inicio del período actual)
   - Nota: "Banco ajustó tasa de interés según nueva decisión"
5. Toque **Guardar**

**Resultado**: Tasa de interés actual actualizada, los períodos no pagados desde el período actual en adelante se actualizan con la nueva tasa de interés.

**Wireframe - Diálogo Actualizar Tasa de Interés**

```text
┌─────────────────────────────────────────┐
│ Actualizar Tasa de Interés Actual             │
├─────────────────────────────────────────┤
│ [ICON] Banco Santander                   │
│ Nombre del Préstamo: Préstamo Hipotecario - Apartamento Centro│
│ Período Actual: Período 9 – 01/2024       │
│ Estado: [Activo]                         │
│ Período: Variable (después de promocional)     │
│                                          │
│ Tasa de Interés Actual (aplicando):       │
│ [9.0] %/año (solo lectura)                  │
│                                          │
│ Nueva Tasa de Interés (%/año) *              │
│ [10.5] %/año                            │
│                                          │
│ Fecha Efectiva *                         │
│ [15/01/2024] [📅]                        │
│                                          │
│ Nota (opcional)                          │
│ [Banco ajustó tasa de interés...]         │
│                                          │
│ • La nueva tasa de interés se aplicará a períodos desde    │
│   el Período Actual en adelante.   │
│ • Los períodos previamente pagados permanecen sin cambios. │
│                                          │
│ [CANCELAR] [GUARDAR]                          │
└─────────────────────────────────────────┘
```

---

### LOAN-05: Liquidación anticipada (Pago parcial para reducir intereses)

**Objetivo**: Liquidar parte del préstamo anticipadamente para reducir intereses totales a pagar y acortar el plazo del préstamo.

**Pasos**:
1. Vaya a los detalles del préstamo
2. Toque **Calcular Monto de Liquidación**
3. **Paso 1 - Ingresar información de prepago:**
   - Seleccione método: "Pago Parcial"
   - Seleccione fecha de prepago: 15/01/2024
   - Ingrese monto de prepago: €72,000
   - Vea multa calculada automáticamente: €1,440 (2.0%)
   - Toque **Siguiente**
4. **Paso 2 - Comparar opciones:**
   - Vea comparación entre "Sin Prepago" y "Prepago €72,000"
   - Vea resultados: Ahorrar €27,000 en intereses, reducir 40 períodos
   - Toque **Confirmar Prepago**

**Resultado**: El saldo disminuye, el calendario de pagos se recalcula, el número de períodos disminuye, la fecha final es anterior.

**Wireframe - Paso 1: Ingresar información de prepago**

```text
┌─────────────────────────────────────────┐
│ <  Liquidación Anticipada                      │
├─────────────────────────────────────────┤
│ [ICON] Banco Santander                   │
│ Nombre del Préstamo: Préstamo Hipotecario - Apartamento Centro│
│ Saldo Actual: €180,000                │
│ Período Actual: Período 9 – 01/2024       │
│                                          │
│ ¿Cómo desea liquidar?              │
│ ● Pago Parcial                        │
│ ○ Liquidación Completa                        │
│                                          │
│ Fecha de Prepago *                        │
│ [15/01/2024] [📅]                        │
│                                          │
│ Monto de Prepago *                      │
│ [€72,000]                                │
│                                          │
│ Tasa de Multa Aplicada: 2.0%                │
│ Multa: €1,440                          │
│                                          │
│ [SIGUIENTE]                                   │
└─────────────────────────────────────────┘
```

**Wireframe - Paso 2: Comparar opciones**

```text
┌─────────────────────────────────────────┐
│ <  Comparar Opciones                       │
├─────────────────────────────────────────┤
│ OPCIÓN A: Sin Prepago                 │
│ ────────────────────────────────────────│
│ Intereses Totales Pagados hasta hoy:            │
│   €46,800                               │
│ Intereses Totales Restantes: €46,800       │
│ Períodos Restantes: 112 períodos          │
│ Fecha Final: 01/04/2033                    │
│                                          │
│ OPCIÓN B: Prepago €72,000            │
│ ────────────────────────────────────────│
│ Multa por Pago Anticipado: €1,440           │
│ Intereses Totales Pagados hasta hoy:            │
│   €48,240                               │
│ Intereses Totales Restantes: €19,800       │
│ Períodos Restantes: 72 períodos           │
│ Fecha Final: 01/04/2029                    │
│                                          │
│ RESULTADO DE COMPARACIÓN:                       │
│ • Ahorro en Intereses: €27,000             │
│ • Reducción de Tiempo: 40 períodos (~3.5 años)│
│                                          │
│ [CONFIRMAR PREPAGO]                     │
└─────────────────────────────────────────┘
```

---

### LOAN-06: Editar préstamo (Editar información básica)

**Objetivo**: Editar información básica del préstamo (nombre, banco, nota) después de comenzar los pagos.

**Pasos**:
1. Vaya a los detalles del préstamo
2. Toque **Editar** (solo editar nombre, nota, banco)
3. Edite:
   - Nombre del Préstamo: "Préstamo Hipotecario - Apartamento Centro - Unidad A1-1201"
   - (Opcional) Cambiar banco: Banco BBVA
   - Nota: "Transferido a nuevo banco"
4. Vea campos deshabilitados: Monto del Préstamo, Fecha de Desembolso, Plazo, Tasa de Interés
5. Toque **Guardar**

**Resultado**: Información básica actualizada, otra información sin cambios.

**Nota**: Si el préstamo aún no ha realizado pagos, se pueden editar todas las informaciones (monto, plazo, configuración de interés).

## 6. Lógica y reglas

### 6.1 Tasa Promocional/Variable

- Puede tener período promocional (tasa de interés más baja)
- Después del período promocional, la tasa de interés varía por período
- Cada período puede ser **Variable** (basado en mercado) o **Fija**

### 6.2 Multas por Pago Tardío

- Las multas se calculan por %/año
- Se puede configurar de manera diferente para cada período
- Las multas solo se aplican cuando el pago está tardío

### 6.3 Calendario de Pagos

- La aplicación crea automáticamente el calendario de pagos basándose en:
  - Monto del préstamo
  - Tasa de interés
  - Plazo
- Cada período de pago incluye: Capital + Intereses

### 6.4 Liquidación Anticipada

- Calcular monto restante (capital + intereses + multas si hay)
- Después de la liquidación, el préstamo cambiará a estado "Completado"

### 6.5 Notificaciones

- La aplicación envía notificación de recordatorio cuando el pago está vencido
- El horario de notificación puede configurarse para cada préstamo (`notificationTime1`, `notificationTime2`, por defecto 10:00 y 19:00)

## 7. Notas importantes

- **Tasas de Interés Complejas**: Este módulo admite tasas de interés que cambian por período, requiere configuración cuidadosa
- **No se puede eliminar cuando existe calendario de pagos**: Si existe calendario de pagos, solo puede liquidar, no eliminar
- **Liquidación Anticipada**: Puede requerir tarifas de multa adicionales, depende de la política del banco
- **Calendario de Pagos**: El calendario de pagos se calcula automáticamente, no puede editar directamente

