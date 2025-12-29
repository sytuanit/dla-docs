# Ahorros

## 1. Propósito

El módulo **Ahorros** le ayuda a gestionar cuentas de ahorro, rastrear saldos, tasas de interés y plazos. Este módulo admite:
- Gestión de múltiples cuentas de ahorro
- Seguimiento de tasas de interés y plazos
- Cálculo automático de intereses al vencimiento
- Retiro anticipado (si es necesario)
- Renovación de cuenta

## 2. Cuándo usar

Use este módulo cuando tenga:
- Cuentas de ahorro bancarias
- Necesite rastrear saldos y tasas de interés
- Desee recordatorios al vencimiento
- Necesite gestionar múltiples cuentas de ahorro

## 3. Pantallas relacionadas

- Lista de cuentas de ahorro
- Agregar nueva cuenta
- Editar cuenta
- Detalles de cuenta
- Retiro anticipado

## 4. Uso principal

### 4.1 Crear nueva cuenta de ahorro

1. Vaya a **Funciones** → Seleccione **Ahorros Bancarios**
2. Toque el botón **+** (FAB) en la esquina inferior derecha
3. Vea "Saldo Actual" (puede hacer clic para ver detalles)
4. Seleccione banco:
   - Si existe: Seleccione del menú desplegable
   - Si no: Toque el botón "+" para crear nuevo banco
5. Ingrese monto del depósito (debe ser ≤ Saldo Actual)
6. Ingrese plazo: 1-36 meses
7. Ingrese tasa de interés: %/año (1-100%)
8. Seleccione fecha de inicio (por defecto es hoy, puede seleccionar desde el mes anterior hasta hoy)
9. Vea fecha de vencimiento calculada automáticamente (desde fecha de inicio + plazo)
10. Seleccione plan al vencimiento:
    - Retirar capital e intereses (por defecto)
    - Renovar CAPITAL (intereses a cuenta)
    - Renovar CAPITAL + INTERESES
11. (Opcional) Ingrese nota
12. (Opcional) Seleccione horarios de notificación (por defecto: 10:00 y 19:00)
13. Toque **CREAR CUENTA**

### 4.2 Ver lista y detalles de cuenta

1. Vaya a **Funciones** → Seleccione **Ahorros Bancarios**
2. Vea la pantalla "Lista de Cuentas de Ahorro" con filtro predeterminado "Activo"
3. Vea tarjeta de resumen:
   - Filtro "Activo": Saldo actual, Dinero en ahorros, Intereses esperados, Intereses de este mes
   - Filtro "Completado": Total retirado, Intereses recibidos
4. (Opcional) Use la barra de búsqueda para encontrar cuentas por nombre o código del banco
5. Cambie el filtro entre "Activo" y "Completado"
6. Toque una cuenta de ahorro para ver detalles:
   - Información de cuenta: Banco, Plazo, Tasa de interés, Monto del depósito, Intereses estimados
   - Fecha de inicio y fecha de vencimiento
   - Estado: Activo
   - Plan al vencimiento
   - (Si existe) Historial de renovaciones
   - Botón "RETIRAR" (si está activo)

### 4.3 Retirar cuenta de ahorro

1. Vaya a la lista de cuentas de ahorro, encuentre la cuenta que ha alcanzado o pasado la fecha de vencimiento
2. Toque el botón **RETIRAR** en la tarjeta (o vaya a detalles y luego toque "RETIRAR")
3. Vea el diálogo "RETIRAR CUENTA DE AHORRO" con:
   - Información de cuenta: Banco, Monto del depósito, Plazo, Tasa de interés
   - Fecha de retiro (por defecto = fecha de vencimiento, puede seleccionar fecha diferente)
   - Intereses recibidos (por defecto = intereses estimados, puede editarse)
   - Total recibido (calculado automáticamente = capital + intereses)
4. (Opcional) Edite la fecha de retiro o los intereses recibidos
5. Toque **CONFIRMAR**

### 4.4 Renovar cuenta de ahorro

1. Vaya a la lista de cuentas de ahorro, encuentre la cuenta que ha alcanzado la fecha de vencimiento con plan "Renovar CAPITAL" o "Renovar CAPITAL + INTERESES"
2. Toque el botón **RENOVAR** o "Renovar según lo planeado"
3. Vea el diálogo "RENOVAR CUENTA DE AHORRO" con:
   - Información de cuenta: Banco, Monto del capital, Plazo, Tasa de interés
   - Intereses recibidos (si renueva CAPITAL, los intereses van a la cuenta)
4. (Opcional) Edite la nueva tasa de interés o el nuevo plazo (por defecto = plazo anterior)
5. Toque **CONFIRMAR RENOVACIÓN**

### 4.5 Editar cuenta de ahorro

1. Vaya a los detalles de la cuenta de ahorro activa
2. Toque el botón **Editar** en la esquina superior derecha
3. Edite la información:
   - Banco (si es necesario)
   - Monto del depósito (si aumenta, debe ser ≤ Saldo Actual)
   - Plazo, Tasa de interés
   - Fecha de inicio (si es necesario)
   - Plan al vencimiento
   - Nota, Horarios de notificación
4. Vea la fecha de vencimiento recalculada automáticamente (si cambia el plazo/fecha de inicio)
5. Toque **GUARDAR CAMBIOS**

### 4.6 Crear nuevo banco

1. En la pantalla "Agregar Cuenta de Ahorro" o "Editar Cuenta de Ahorro"
2. Toque el campo "Banco"
3. Toque el botón "+" junto al menú desplegable para crear nuevo banco
4. Vea el diálogo "AGREGAR NUEVO BANCO"
5. Ingrese nombre del banco
6. Ingrese código del banco (máx. 3-4 caracteres, automáticamente en mayúsculas)
7. Seleccione color del icono (del selector de color o paleta)
8. Vea la vista previa del icono
9. Toque **CREAR**

## 5. Ejemplos e ilustraciones de UI

### SAVINGS-01: Crear nueva cuenta de ahorro

**Objetivo**: Crear nueva cuenta de ahorro para rastrear depósito bancario, tasa de interés y fecha de vencimiento.

**Pasos principales**:
1. Vaya a Funciones → Ahorros Bancarios
2. Toque el botón "+" (FAB)
3. Seleccione banco (o cree nuevo)
4. Ingrese monto del depósito, plazo, tasa de interés
5. Seleccione fecha de inicio (por defecto hoy)
6. Seleccione plan al vencimiento
7. (Opcional) Ingrese nota y horarios de notificación
8. Toque "CREAR CUENTA"

**Wireframe - Pantalla Agregar Cuenta de Ahorro**:

```text
┌──────────────────────────────────────────────┐
│ <  Agregar Cuenta de Ahorro                       │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ Tarjeta ]                                      │
│                                               │
│ Saldo Actual                      [ > ]    │
│ €1,872                                        │
│                                               │
│ Banco *                                        │
│ [ Banco Santander ▼ ]                 [ + ] │
│                                               │
│ Monto del Depósito (EUR) *                       │
│ [ €3,600 ]                                    │
│                                               │
│ Plazo *                                        │
│ [ 6 ] Meses                                  │
│                                               │
│ Tasa de Interés *                               │
│ [ 4.8 ] %/año                                │
│                                               │
│ Fecha de Inicio *                                  │
│ [ 20/12/2025 ]                    [📅]        │
│                                               │
│ Fecha de Vencimiento (solo lectura)                      │
│ [ 20/06/2026 ]                                 │
│                                               │
│ Plan al Vencimiento                              │
│ (●) Retirar capital e intereses          │
│ ( ) Renovar CAPITAL                        │
│ ( ) Renovar CAPITAL + INTERESES            │
│                                               │
│ Nota (opcional)                               │
│ [                                      ]      │
│                                               │
│ Hora de Notificación 1                           │
│ [ 10:00 ]                          [🕐]       │
│                                               │
│ Hora de Notificación 2                            │
│ [ 19:00 ]                          [🕐]       │
└──────────────────────────────────────────────┘

        [  CANCELAR  ]       [  CREAR CUENTA  ]
```

---

### SAVINGS-02: Retirar cuenta de ahorro

**Objetivo**: Retirar cuenta de ahorro cuando alcanza la fecha de vencimiento para recibir capital e intereses.

**Pasos principales**:
1. Vaya a la lista de cuentas de ahorro, encuentre la cuenta que ha alcanzado o pasado la fecha de vencimiento
2. Toque el botón "RETIRAR"
3. Vea el diálogo con información de cuenta, fecha de retiro, intereses recibidos
4. (Opcional) Edite la fecha de retiro o los intereses recibidos
5. Toque "CONFIRMAR"

**Wireframe - Diálogo Retirar**:

```text
┌─────────────────────────────────────────┐
│  RETIRAR CUENTA DE AHORRO                │
├─────────────────────────────────────────┤
│  [ICON BANK]  Banco Santander            │
│                                         │
│  Plazo y Tasa de Interés: 6 meses · 4.8%/año │
│  Monto del Depósito: €3,600                 │
│                                         │
│  Fecha de Retiro:                       │
│  [ 20 / 12 / 2025 ]  [📅]               │
│                                         │
│  Intereses Recibidos:                     │
│  [ €86 ]                                │
│                                         │
│  Total Recibido: €3,686                 │
│                                         │
│  [  CONFIRMAR  ]                          │
└─────────────────────────────────────────┘
```

---

### SAVINGS-03: Ver lista y detalles de cuenta

**Objetivo**: Ver resumen de cuentas de ahorro activas y completadas, así como detalles de cada cuenta.

**Pasos principales**:
1. Vaya a Funciones → Ahorros Bancarios
2. Vea la tarjeta de resumen por filtro
3. Use la barra de búsqueda (opcional)
4. Cambie el filtro entre "Activo" y "Completado"
5. Toque la cuenta para ver detalles

**Wireframe - Pantalla de Lista**:

```text
┌──────────────────────────────────────────────┐
│ <  Gestión de Ahorros Bancarios                    │
│                  [ + [FAB] Agregar Cuenta ]      │
└──────────────────────────────────────────────┘

[Chip] Filtro
[ Activo ]   [ Completado ]

┌──────────────────────────────────────────────┐
│  TARJETA DE RESUMEN                                │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Saldo      │  │ Intereses      │         │
│  │ Actual      │  │ Esperados      │         │
│  │ €1,872       │  │ €197          │         │
│  └──────────────┘  └──────────────┘         │
│  ┌──────────────┐  ┌──────────────┐         │
│  │ Dinero en     │  │ Intereses de este │         │
│  │ Ahorros      │  │ mes      │         │
│  │ €12,600      │  │ €68           │         │
│  └──────────────┘  └──────────────┘         │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│  🔍 Barra de Búsqueda                               │
│  [ 🔍 Buscar... ]                            │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ [ICON BANK] Banco Santander      [Icono Eliminar] │
│                                              │
│ €3,600         |  6 meses @ 4.8%           │
│                                              │
│ Intereses Estimados: €86                     │
│ Vencimiento: 20/12/2025   (5 días restantes)  │
│                    🔔 Próximo a vencer               │
│                                              │
│                    [ RETIRAR ]             │
└──────────────────────────────────────────────┘
```

**Wireframe - Pantalla de Detalles**:

```text
┌──────────────────────────────────────────────┐
│ [ICON BANK]  Banco Santander          [ Editar ]│
│                                              │
│ Plazo y Tasa de Interés: 6 meses · 4.8%/año  │
│ Monto del Depósito: €3,600                       │
│ Intereses Estimados: €86                     │
│                                              │
│ Fecha de Inicio: 20/06/2025                       │
│ Fecha de Vencimiento: (5 días restantes) 20/12/2025 │
│                                              │
│ Estado: Activo                               │
│                                              │
│ Plan al Vencimiento:                           │
│ (●) Retirar capital e intereses         │
│                                              │
│                    [  RETIRAR  ]           │
└──────────────────────────────────────────────┘
```

---

### SAVINGS-04: Renovar cuenta de ahorro

**Objetivo**: Renovar cuenta de ahorro según lo planeado cuando alcanza la fecha de vencimiento.

**Pasos principales**:
1. Encuentre la cuenta que ha alcanzado la fecha de vencimiento con plan "Renovar CAPITAL" o "Renovar CAPITAL + INTERESES"
2. Toque el botón "RENOVAR"
3. Vea el diálogo con información de cuenta e intereses recibidos
4. (Opcional) Edite la nueva tasa de interés o el nuevo plazo
5. Toque "CONFIRMAR RENOVACIÓN"

**Resultado**: La cuenta antigua se actualiza, se crea nueva cuenta vinculada con rootSavingId a la cuenta antigua. Si renueva CAPITAL, los intereses se agregan al saldo actual. Si renueva CAPITAL + INTERESES, tanto el capital como los intereses se renuevan.

---

### SAVINGS-05: Crear nuevo banco

**Objetivo**: Crear nuevo banco para usar al crear cuentas de ahorro.

**Pasos principales**:
1. En la pantalla "Agregar Cuenta de Ahorro" o "Editar Cuenta de Ahorro"
2. Toque el botón "+" junto al menú desplegable "Banco"
3. Ingrese nombre del banco, código del banco
4. Seleccione color del icono
5. Vea la vista previa del icono
6. Toque "CREAR"

**Wireframe - Diálogo Crear Banco**:

```text
┌─────────────────────────────────────────┐
│  AGREGAR NUEVO BANCO                            │
├─────────────────────────────────────────┤
│  NOMBRE DEL BANCO                               │
│  [ Banco ABC ]                            │
│                                         │
│  CÓDIGO DEL BANCO                               │
│  [ ABC ]                                 │
│                                         │
│  COLOR DEL ICONO                              │
│  [ 🎨 ]  #FF5722                         │
│                                         │
│  VISTA PREVIA DEL ICONO                            │
│  ┌─────────┐                             │
│  │   ABC   │  (Fondo: #FF5722)      │
│  └─────────┘                             │
│                                         │
│  [  CANCELAR  ]    [  CREAR  ]           │
└─────────────────────────────────────────┘
```

---

### SAVINGS-06: Editar cuenta de ahorro

**Objetivo**: Editar información de cuenta de ahorro activa (banco, monto, plazo, tasa de interés, plan de vencimiento).

**Pasos principales**:
1. Vaya a los detalles de la cuenta de ahorro activa
2. Toque el botón "Editar"
3. Edite la información necesaria
4. Vea la fecha de vencimiento recalculada automáticamente (si cambia el plazo/fecha de inicio)
5. Toque "GUARDAR CAMBIOS"

**Resultado**: La información de la cuenta se actualiza, los intereses estimados se recalculan basándose en la nueva tasa de interés. Si cambia el monto, el saldo actual se ajusta en consecuencia.

## 6. Lógica y reglas

### 6.1 Cálculo de intereses

- Los intereses se calculan por la fórmula: `Monto × Tasa de Interés × (Plazo / 12)`
- Los intereses se calculan al vencimiento o al retirar anticipadamente

### 6.2 Estado

- **Activo (ACTIVE)**: La cuenta de ahorro está activa, no ha alcanzado la fecha de vencimiento o no ha sido procesada
- **Completado (COMPLETED)**: La cuenta ha sido retirada
- **Renovado (ROLLED_OVER)**: La cuenta ha sido renovada, se creó nueva cuenta

### 6.3 Retiro y renovación

- **Retiro**: Al retirar, el capital + intereses se agregan al saldo actual, crea automáticamente "Ingreso Extra" con categoría "Intereses de Ahorros"
- **Retiro Anticipado**: Puede retirar antes de la fecha de vencimiento, los intereses recibidos pueden ser menores que los intereses estimados
- **Renovar CAPITAL**: Los intereses se agregan al saldo actual, el capital se renueva con nuevo plazo
- **Renovar CAPITAL + INTERESES**: Tanto el capital como los intereses se renuevan, el saldo actual no cambia
- **Historial de Renovaciones**: Las renovaciones se guardan y se muestran en los detalles de la cuenta, vinculadas a través de `rootSavingId`

### 6.4 Notificaciones

- La aplicación envía notificación de recordatorio cuando llega la fecha de vencimiento
- El horario de notificación puede configurarse para cada cuenta (`notificationTime1`, `notificationTime2`, por defecto 10:00 y 19:00)

## 7. Notas importantes

- **Módulo Premium Requerido**: Esta función es solo para usuarios Premium
- **Tasa de Interés**: Ingrese la tasa de interés por año (%/año), del 1 al 100%
- **Plazo**: Calculado en meses, de 1 a 36 meses
- **Fecha de Vencimiento**: Calculada automáticamente desde fecha de inicio + plazo
- **Monto del Depósito**: Debe ser ≤ Saldo Actual, al crear la cuenta se resta automáticamente del saldo actual
- **Fecha de Inicio**: Solo puede seleccionar desde el inicio del mes anterior hasta hoy
- **Notificaciones**: Las notificaciones se envían en la fecha de vencimiento a 2 horarios (por defecto 10:00 y 19:00), pueden personalizarse para cada cuenta
- **Badge "Próximo a vencer"**: Se muestra cuando ≤ 7 días hasta la fecha de vencimiento
- **Badge "Vencido"**: Se muestra cuando ha llegado la fecha de vencimiento
- **Eliminar Cuenta**: Al eliminar cuenta activa, el monto del capital se agrega de vuelta al saldo actual. Eliminar cuenta raíz elimina toda la cadena de renovaciones
- **Tarjeta de Resumen**: Cambia por filtro, muestra información agregada para cuentas activas o completadas

