# Lista de Tareas

## 1. Propósito

El módulo **Lista de Tareas** le ayuda a gestionar tareas recurrentes y rastrear el progreso de finalización, incluyendo:
- Tareas recurrentes basadas en tiempo (diarias/semanales/mensuales/anuales)
- Tareas recurrentes basadas en métricas (millas/horas/veces...)
- Recordatorios cuando están vencidas
- Rastrear historial de finalización
- Registrar gastos (si corresponde)

Este módulo le ayuda a nunca olvidar tareas importantes como mantenimiento del auto, cambio de filtros, controles periódicos, etc.

## 2. Cuándo usar

Use este módulo cuando tenga:
- Tareas que se repiten según un horario (ej. cambiar filtro de agua cada 3 meses)
- Tareas que se repiten basadas en métricas (ej. cambiar aceite del motor cada 3.000 millas)
- Necesita recordatorios automáticos cuando están vencidas
- Desea rastrear historial de finalización
- Necesita registrar gastos relacionados

## 3. Pantallas relacionadas

- Pantalla Lista de Tareas
- Seleccionar tipo de tarea (Basada en tiempo / Basada en métricas)
- Agregar nueva tarea
- Editar tarea
- Confirmar tarea basada en métricas
- Historial de tareas
- Lista de tareas vencidas (lista de campana)

## 4. Uso principal

### 4.1 Agregar tarea basada en tiempo

1. Vaya a **Funciones** → Seleccione **Lista de Tareas**
2. Toque el botón **➕** (FAB) en la esquina inferior derecha
3. Seleccione **Tarea Basada en Tiempo**
4. Complete la información:
   - **Nombre de la Tarea**: (requerido, ej. "Cambiar filtro de agua")
   - **Ciclo de repetición**: Ingrese número y seleccione unidad (Día/Semana/Mes/Año)
   - **Próxima fecha de vencimiento**: Seleccione fecha (solo se permite seleccionar desde mañana)
   - **Hora de recordatorio**: Seleccione hora (requerido, ej. 08:00)
   - **Esta tarea causa gastos**: (Opcional) Marque si hay gastos
     - Si está marcado: Seleccione **Categoría** (requerido)
   - **Nota**: Información adicional (opcional)
5. Toque **Guardar**

### 4.2 Agregar tarea basada en métricas

1. Vaya a **Funciones** → Seleccione **Lista de Tareas**
2. Toque el botón **➕** (FAB)
3. Seleccione **Tarea Basada en Métricas**
4. Complete la información:
   - **Nombre de la Tarea**: (requerido, ej. "Cambiar aceite del motor")
   - **Ciclo**: Ingrese número (ej. 3.000)
   - **Unidad**: Ingrese unidad (ej. "Millas")
   - **Último valor de métrica completado**: Ingrese valor actual (ej. 12.500)
   - **Esta tarea causa gastos**: (Opcional) Marque si hay gastos
     - Si está marcado: Seleccione **Categoría** (requerido)
   - **Nota**: Información adicional (opcional)
5. Toque **Guardar**

### 4.3 Confirmar tarea basada en métricas

1. Vaya a la lista de tareas
2. Encuentre la tarea basada en métricas (tipo METRIC) para confirmar
3. Toque el botón **Confirmar** en la tarjeta (solo se muestra si `isActive = true`)
4. Complete la información:
   - **Valor de métrica actual**: Ingrese valor actual (requerido, debe ser ≥ último valor de métrica completado)
   - **Nota**: (Opcional)
5. Muestre **Delta** calculado automáticamente (valor actual - último valor completado)
6. Toque **Confirmado**
7. (Si la tarea tiene gastos) Seleccione **Agregar gasto** o **Cancelar**

**Nota**: Las tareas basadas en tiempo (tipo CYCLE) no tienen botón "Confirmar" en la tarjeta. La confirmación solo se realiza en la pantalla "Tareas Vencidas" (lista de campana).

### 4.4 Ver lista y detalles

1. Vaya a **Funciones** → Seleccione **Lista de Tareas**
2. Use la **barra de búsqueda** para buscar por nombre de tarea
3. Use los **chips de filtro** para filtrar:
   - **Todas**: Muestra todas las tareas
   - **Basadas en tiempo**: Muestra solo tareas tipo CYCLE
   - **Basadas en métricas**: Muestra solo tareas tipo METRIC
4. Toque la tarjeta de tarea para ver detalles y editar

### 4.5 Editar tarea

1. Vaya a la lista de tareas
2. Toque la tarjeta de tarea para editar
3. Actualice la información:
   - **Nota**: Si hay historial, el **Ciclo** (CYCLE) o **Unidad/Ciclo** (METRIC) está bloqueado y no se puede editar
4. Toque **Guardar**

### 4.6 Ver historial

1. Vaya a la lista de tareas
2. Toque el vínculo **Ver historial ›** de la tarea para ver
3. Use los **chips de filtro** para filtrar por tiempo:
   - **Todas**: Muestra todo el historial
   - **Este mes**: Muestra solo historial del mes actual
   - **Mes pasado**: Muestra solo historial del mes anterior
   - **Últimos 3 meses**: Muestra solo historial de los últimos 3 meses

### 4.7 Desactivar/activar tarea

1. Vaya a la lista de tareas
2. Encuentre la tarea para desactivar/activar
3. Cambie el interruptor **Activo** en el pie de la tarjeta
4. Las tareas desactivadas muestran el badge **"Inactiva"** (gris)

### 4.8 Eliminar tarea

1. Vaya a la lista de tareas
2. Toque el icono **Eliminar** (🗑️) en el encabezado de la tarjeta
3. Confirme la eliminación en el diálogo
4. La tarea y todo el historial relacionado se eliminan

## 5. Ejemplos e ilustraciones de UI

### 5.1 TODO-01: Crear tarea basada en tiempo (Cambiar filtro de agua)

**Objetivo**: Crear tarea basada en tiempo para que la app le recuerde automáticamente cuando esté vencida.

**Pasos principales**:
1. Vaya a Funciones → Lista de Tareas → Toque el botón "➕" (FAB)
2. Seleccione "Tarea Basada en Tiempo"
3. Ingrese nombre de tarea: "Cambiar filtro de agua"
4. Ingrese ciclo: "3" meses
5. Seleccione próxima fecha de vencimiento: 01/03/2026
6. Seleccione hora de recordatorio: 08:00
7. Marque "Esta tarea causa gastos", seleccione categoría "Servicios públicos"
8. Ingrese nota: "Cambiar filtro #1 y #2"
9. Toque "Guardar"

**Ilustración de UI - Pantalla Agregar Tarea Basada en Tiempo**:

```text
┌──────────────────────────────────────────────┐
│ <  Agregar Tarea Basada en Tiempo                      │
├──────────────────────────────────────────────┤

Nombre de la Tarea
[ Cambiar filtro de agua            ]

Ciclo de repetición
Cada [ 3 ] [ Mes ▼ ]
(Unidad: Día / Semana / Mes / Año)

Próxima fecha de vencimiento
[ 01 / 03 / 2026    ▼ ]
Nota: 
Fecha de vencimiento por primera vez.
Las fechas posteriores se calcularán automáticamente según el ciclo que ingrese.

Hora de recordatorio
[ 08 : 00           ▼ ]

──────────────────────────────────────────────
[✓] Esta tarea causa gastos

┌─────────────────────────────────────┐
│ Categoría *                           │
│ [Servicios públicos ▼] [+ Crear nuevo]       │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Nota (opcional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Cancelar ]                         [ Guardar ]
└──────────────────────────────────────────────┘
```

---

### 5.2 TODO-02: Crear tarea basada en métricas (Cambiar aceite del motor)

**Objetivo**: Crear tarea basada en métricas para rastrear mantenimiento del auto basado en kilometraje.

**Pasos principales**:
1. Vaya a Funciones → Lista de Tareas → Toque el botón "➕" (FAB)
2. Seleccione "Tarea Basada en Métricas"
3. Ingrese nombre de tarea: "Cambiar aceite del motor"
4. Ingrese ciclo: "3.000", Unidad: "Millas"
5. Ingrese último valor de métrica completado: "12.500"
6. Marque "Esta tarea causa gastos", seleccione categoría "Mantenimiento del auto"
7. Ingrese nota: "Cambiar aceite + filtro de aceite"
8. Toque "Guardar"

**Ilustración de UI - Pantalla Agregar Tarea Basada en Métricas**:

```text
┌──────────────────────────────────────────────┐
│ <  Agregar Tarea Basada en Métricas                    │
├──────────────────────────────────────────────┤

Nombre de la Tarea
[ Cambiar aceite del motor                        ]

Ciclo
Cada [ 3.000 ] Unidad [ Millas ]
(Unidad: Millas / Horas / Veces / ...)

Último valor de métrica completado
[ 12.500 ]

──────────────────────────────────────────────
[✓] Esta tarea causa gastos

┌─────────────────────────────────────┐
│ Categoría *                           │
│ [Mantenimiento del auto ▼] [+ Crear nuevo] │
└─────────────────────────────────────┘

──────────────────────────────────────────────
Nota (opcional)
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
[ Cancelar ]                         [ Guardar ]
└──────────────────────────────────────────────┘
```

---

### 5.3 TODO-03: Ver lista y detalles

**Objetivo**: Ver resumen de tareas, filtrar por tipo, buscar y ver detalles de cada tarea.

**Pasos principales**:
1. Vaya a Funciones → Lista de Tareas
2. Muestre lista con barra de búsqueda y chips de filtro
3. Use filtros: "Todas", "Basadas en tiempo", "Basadas en métricas"
4. Use barra de búsqueda para buscar por nombre de tarea
5. Toque la tarjeta de tarea para ver detalles

**Ilustración de UI - Pantalla Lista de Tareas**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Atrás]  Lista de Tareas                        [🔔]        │
└─────────────────────────────────────────────────────────┘
│  🔍 Buscar...                                             │
│                                                          │
│  [Todas] [Basadas en tiempo] [Basadas en métricas]                     │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Tarjeta: Cambiar filtro de agua                      │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Cambiar filtro de agua    [Completada] [🗑️]   │ │    │
│  │ │                                              │ │    │
│  │ │ 📅 Ciclo: Cada 3 meses                     │ │    │
│  │ │ ✅ Última completada: 01/12/2025                │ │    │
│  │ │ 📅 Próxima fecha de vencimiento: 01/03/2026                 │ │    │
│  │ │ ⏳ 76 días restantes                          │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Ver historial ›                     [⚪ Activo]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Tarjeta: Cambiar aceite del motor                            │    │
│  │ ┌─────────────────────────────────────────────┐ │    │
│  │ │ Cambiar aceite del motor                   [🗑️]      │ │    │
│  │ │                                              │ │    │
│  │ │ 📏 Rastrear por: Millas                           │ │    │
│  │ │ ✅ Última confirmada: 02/12/2025                │ │    │
│  │ │ 🔢 Último valor de métrica: 12.500 millas          │ │    │
│  │ │ 🎯 Próxima vencida: 15.500 millas                    │ │    │
│  │ │ ⏳ ~300 millas restantes                      │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ [✓ Confirmar]                                  │ │    │
│  │ │ ───────────────────────────────────────────── │ │    │
│  │ │ Ver historial ›                     [⚪ Activo]│ │    │
│  │ └─────────────────────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  [+ FAB]                                                 │
└─────────────────────────────────────────────────────────┘
```

---

### 5.4 TODO-04: Confirmar tarea basada en métricas (Cambiar aceite del motor)

**Objetivo**: Confirmar finalización de tarea basada en métricas ingresando valor de métrica actual.

**Pasos principales**:
1. Vaya a la lista de tareas
2. Encuentre la tarea "Cambiar aceite del motor" (tipo METRIC)
3. Toque el botón "Confirmar"
4. Ingrese valor de métrica actual: "14.520"
5. Muestre delta calculado automáticamente: "+2.020 millas"
6. Ingrese nota: "Aceite + filtro de aceite cambiados"
7. Toque "Confirmado"

**Ilustración de UI - Diálogo Confirmar Tarea Basada en Métricas**:

```text
┌──────────────────────────────────────────────┐
│  Confirmar Tarea Basada en Métricas                   │
├──────────────────────────────────────────────┤

Nombre de la Tarea:
Cambiar aceite del motor   (solo lectura)

Rastrear por:
Millas   (solo lectura)

Último valor de métrica completado:
12.500 millas   (solo lectura)

──────────────────────────────────────────────
Valor de métrica actual
[ 14.520 ] millas

Delta:
+2.020 millas   (automático)

──────────────────────────────────────────────
Nota
[                                          ]
[                                          ]
[                                          ]

──────────────────────────────────────────────
        [ No confirmado ]    [ Confirmado ]
└──────────────────────────────────────────────┘
```

---

### 5.5 TODO-05: Editar tarea y ver historial

**Objetivo**: Editar información de tarea y ver historial de finalización.

**Pasos principales**:
1. Vaya a la lista de tareas
2. Toque la tarjeta de tarea "Cambiar filtro de agua"
3. Muestre advertencia: "⚠️ El ciclo está bloqueado porque hay historial" (si existe historial)
4. Edite próxima fecha de vencimiento, hora de recordatorio, nota
5. Toque "Guardar"
6. Toque "Ver historial ›" para ver historial con filtros

**Ilustración de UI - Pantalla Historial de Tareas**:

```text
┌─────────────────────────────────────────────────────────┐
│  [← Atrás]  Historial de Tareas - Cambiar filtro de agua          │
└─────────────────────────────────────────────────────────┘
│  [Todas] [Este mes] [Mes pasado] [Últimos 3 meses]        │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Cambiar filtro de agua            [Completada]      │    │
│  │                                                  │    │
│  │ 📅 Ciclo: Cada 3 meses                         │    │
│  │ ✅ Completada el: 01/12/2025 – 09:10             │    │
│  │ 📝 Nota: Cambiar filtro #1 y #2                │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │ Cambiar filtro de agua            [Completada]      │    │
│  │                                                  │    │
│  │ 📅 Ciclo: Cada 3 meses                         │    │
│  │ ✅ Completada el: 01/09/2025 – 08:45             │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

---

### 5.6 TODO-06: Desactivar y eliminar tarea

**Objetivo**: Desactivar o eliminar tarea cuando ya no sea necesaria.

**Pasos principales**:
1. Vaya a la lista de tareas
2. Encuentre la tarea para desactivar
3. Toque el interruptor "Activo" para desactivar
4. Muestre badge "Inactiva" aparecer
5. Toque el interruptor nuevamente para reactivar
6. Toque el icono Eliminar (🗑️) para eliminar tarea
7. Confirme eliminación en el diálogo

---

### 5.7 TODO-07: Confirmar tarea basada en métricas y agregar gasto

**Objetivo**: Confirmar tarea basada en métricas y agregar automáticamente gasto relacionado.

**Pasos principales**:
1. Vaya a la lista de tareas
2. Encuentre la tarea "Cambiar aceite del motor" (tipo METRIC, hasCost = true)
3. Toque el botón "Confirmar"
4. Ingrese valor de métrica actual: "14.520"
5. Ingrese nota: "Aceite + filtro de aceite cambiados"
6. Toque "Confirmado"
7. Muestre diálogo "¿Causó gasto?" abrirse automáticamente
8. Toque "Agregar gasto"
9. Muestre pantalla "Agregar gasto" con nota y categoría prellenadas
10. Ingrese monto: €45
11. Toque "Guardar"

**Ilustración de UI - Diálogo ¿Causó Gasto?**:

```text
┌──────────────────────────────────────────────┐
│  ¿Causó gasto?                           │
├──────────────────────────────────────────────┤
¿Desea agregar un gasto para esta
finalización?

        [ Cancelar ]         [ Agregar gasto ]
└──────────────────────────────────────────────┘
```

## 6. Lógica y reglas

### 6.1 Tipos de tareas

- **Basada en tiempo (tipo CYCLE)**:
  - Se repite según horario (Día/Semana/Mes/Año)
  - Tiene notificaciones de recordatorio cuando está vencida
  - La confirmación solo se realiza en la pantalla "Tareas Vencidas" (lista de campana)
  - No tiene botón "Confirmar" en la tarjeta

- **Basada en métricas (tipo METRIC)**:
  - Se repite basada en hitos de métricas (millas/horas/veces/Otros)
  - No tiene notificaciones (MVP1)
  - Tiene botón "Confirmar" en la tarjeta (solo se muestra si `isActive = true`)
  - Confirmación ingresando valor de métrica actual

### 6.2 Estado de tarea

- **PENDIENTE**: Próxima (aún no vencida)
  - No se muestra badge: `nextDueDate - hoy > 7 días`
  - Muestra badge "Próxima" (amarillo): `0 < nextDueDate - hoy ≤ 7 días`
- **VENCIDA**: Vencida (rojo) - `nextDueDate < hoy` y no confirmada
- **NO COMPLETADA**: No realizada (naranja) - Vencida pero no confirmada
- **COMPLETADA**: Completada (verde) - Confirmada
- **CANCELADA**: Cancelada (gris) - Esta ocurrencia fue cancelada
- **INACTIVA**: Inactiva (gris) - `isActive = false`

### 6.3 Bloquear ciclo/unidad

- Si hay historial (registros de historial):
  - **Tipo CYCLE**: El ciclo está bloqueado, no se puede editar
  - **Tipo METRIC**: La unidad y el ciclo están bloqueados, no se pueden editar
- Muestra advertencia: "⚠️ El ciclo está bloqueado porque hay historial" o "⚠️ La unidad está bloqueada porque hay historial"

### 6.4 Confirmar tarea basada en métricas

- **Validación**:
  - El valor de métrica actual debe ser ≥ último valor de métrica completado
  - Si es inválido: Muestra error "El valor de métrica actual debe ser ≥ último valor de métrica completado"
- **Actualización automática**:
  - `lastMetricValue` = valor actual
  - `nextMetricValue` = valor actual + ciclo
  - `lastCompletedDate` = hoy
- **Gastos**:
  - Si `hasCost = true`: Muestra diálogo "¿Causó gasto?" después de confirmación exitosa
  - Navega a pantalla "Agregar gasto" con `initialNote`, `initialCategoryId`, `todoHistoryId`

### 6.5 Notificaciones

- **Tipo CYCLE**: 
  - Las notificaciones se programan cuando la tarea se crea/edita
  - Las notificaciones se cancelan cuando la tarea se desactiva o elimina
  - Las notificaciones se reprograman cuando se reactiva (si `nextDueDate >= hoy`)
- **Tipo METRIC**: No tiene notificaciones (MVP1)

### 6.6 Calcular próxima fecha de vencimiento

- **Tipo CYCLE**: 
  - Próxima fecha de vencimiento calculada automáticamente basada en ciclo después de confirmación
  - Ejemplo: Ciclo 3 meses, Fecha de vencimiento 01/03/2026 → Después de confirmación, próxima fecha de vencimiento = 01/06/2026
- **Tipo METRIC**: 
  - Próxima vencida = valor actual + ciclo
  - Ejemplo: Valor actual 14.520 millas, Ciclo 3.000 millas → Próxima vencida = 17.520 millas

## 7. Notas importantes

1. **Botón Confirmar**:
   - **Tareas basadas en tiempo (CYCLE)**: No tienen botón "Confirmar" en la tarjeta. La confirmación solo se realiza en la pantalla "Tareas Vencidas" (lista de campana).
   - **Tareas basadas en métricas (METRIC)**: Tienen botón "Confirmar" en la tarjeta (solo se muestra si `isActive = true`).

2. **Icono de campana**: El icono de campana en el encabezado navega a la pantalla "Tareas Vencidas" (lista de campana), donde los usuarios pueden confirmar tareas vencidas (solo para tipo CYCLE).

3. **Bloquear ciclo/unidad**: Si hay historial, el ciclo (CYCLE) o la unidad/ciclo (METRIC) está bloqueado y no se puede editar para asegurar consistencia de datos.

4. **Validación de métricas**: Al confirmar una tarea basada en métricas, el valor de métrica actual debe ser ≥ último valor de métrica completado. Si no, la app muestra un error y previene la confirmación.

5. **Gastos causados**: Si una tarea tiene gastos (`hasCost = true`), la app pregunta después de confirmación exitosa si desea agregar un gasto. Si selecciona "Agregar gasto", la app prellena automáticamente la nota y la categoría.

6. **Eliminar tarea**: Al eliminar una tarea, también se elimina todo el historial relacionado (eliminación en cascada). Las notificaciones también se cancelan.

7. **Desactivar**: Al desactivar una tarea tipo CYCLE, las notificaciones se cancelan. Al reactivar, las notificaciones se reprograman (si `nextDueDate >= hoy`).

8. **Acceso Premium**: Este módulo requiere acceso Premium. Si no tiene Premium, la app muestra un diálogo solicitando actualización.

