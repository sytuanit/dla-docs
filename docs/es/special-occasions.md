# Ocasiones Especiales

## 1. Propósito

El módulo **Ocasiones Especiales** le ayuda a:
- Gestionar ocasiones especiales durante el año (cumpleaños, festividades, etc.)
- Crear listas de tareas (pasos de preparación)
- Adjuntar listas de compras a cada paso de preparación
- Recordatorios antes de las ocasiones
- Seguimiento del progreso de preparación

## 2. Cuándo usar

Use este módulo cuando desee:
- Gestionar ocasiones especiales durante el año
- Prepararse para ocasiones importantes
- Crear listas de tareas
- Recibir recordatorios antes de las ocasiones

## 3. Pantallas relacionadas

- Lista de ocasiones especiales
- Agregar nueva ocasión especial
- Detalles de ocasión y pasos de preparación
- Agregar paso de preparación
- Seleccionar lista de compras
- Crear nueva lista de compras

## 4. Uso principal

### 4.1 Agregar ocasión especial

1. Vaya a **Funciones** → Seleccione **Ocasiones Especiales**
2. Toque el botón **➕** (FAB)
3. Complete la información:
   - **Nombre de la Ocasión**: (ej. "Cumpleaños de Mamá")
   - **Fecha**: Seleccione día/mes (DatePicker solo selecciona día/mes, no año)
   - **Usar calendario lunar**: (Opcional) Marque si desea usar calendario lunar
     - Si está marcado: Ingrese día y mes lunar, la app calcula automáticamente la próxima fecha solar
   - **Repetir**: Anualmente / Solo este año
   - **Mostrar notificación a las**: Seleccione hora (requerido, ej. 07:00)
   - **Nota**: Información adicional (opcional)
4. (Opcional) Agregue pasos de preparación (ver 4.2)
5. Toque **Guardar**

### 4.2 Agregar paso de preparación

1. Al agregar nueva ocasión: Toque **+ Agregar Paso** en la sección "Pasos de Preparación"
2. O desde detalles de ocasión: Toque **+ Agregar Paso**
3. Complete la información:
   - **¿Cuándo?**: "X días antes" o "El día"
   - **Número de días**: (si se selecciona "X días antes") Ingrese número de días antes de la ocasión
   - **Mostrar notificación a las**: Seleccione hora (requerido)
   - **Repetir diariamente hasta completar**: (Opcional) Marque si desea recordatorios diarios
   - **Contenido**: Nombre del paso (requerido, ej. "Comprar regalo")
   - **Nota**: (Opcional)
   - **Usar lista de compras**: (Opcional) Marque para vincular con lista de compras
4. Toque **Agregar** (o FAB "Aplicar")

### 4.3 Crear lista de compras

1. Al agregar paso de preparación, marque **Usar lista de compras**
2. Se abre automáticamente la pantalla "Seleccionar lista de compras"
3. Toque el FAB **➕** para crear nueva lista de compras
4. Ingrese nombre de la lista de compras
5. Agregue elementos:
   - Ingrese nombre del elemento
   - Toque **➕** para agregar nuevo elemento
6. Toque **Guardar**
7. La nueva lista de compras se selecciona automáticamente y regresa a la pantalla "Agregar paso de preparación"

### 4.4 Marcar paso como completado

1. Vaya a detalles de ocasión especial
2. Encuentre el paso para marcar
3. Toque la casilla [ ] para cambiar a [✓]
4. Si hay lista de compras, toque el nombre de la lista de compras para mostrar elementos y marcar/desmarcar

### 4.5 Ver progreso

1. Vaya a detalles de ocasión especial
2. Muestre la sección "Resumen":
   - Pasos de preparación: Número total de pasos
   - Completados: Número de pasos marcados / Total de pasos
   - Estado: No iniciado / En progreso / Completado

### 4.6 Editar ocasión especial

1. Vaya a detalles de ocasión especial
2. Toque el hipervínculo **Editar ›** en el encabezado
3. Edite la información: Nombre, Fecha, Repetir, Hora de recordatorio, Nota
4. Toque **Guardar**

### 4.7 Editar paso de preparación

1. Vaya a detalles de ocasión especial
2. Toque el paso para editar (haga clic en todo el elemento, excepto el icono Eliminar)
3. Edite la información: Tiempo, Contenido, Lista de compras
4. Toque **Aplicar** (o FAB)

## 5. Ejemplos e ilustraciones de UI

### 5.1 OCCASION-01: Crear nueva ocasión especial (Cumpleaños con pasos de preparación)

**Objetivo**: Crear nueva ocasión especial (cumpleaños) con pasos de preparación para que la app le recuerde automáticamente antes de que ocurra la ocasión.

**Pasos principales**:
1. Vaya a Funciones → Ocasiones Especiales → Toque el botón "➕" (FAB)
2. Ingrese nombre de ocasión, seleccione fecha (01/05), seleccione Repetir "Anualmente", seleccione hora de recordatorio (07:00)
3. Agregue paso de preparación 1: "7 días antes – 08:00" - "Comprar regalo"
4. Agregue paso de preparación 2: "1 día antes – 19:00" - "Pedir pastel"
5. Toque "Guardar"

**Ilustración de UI - Pantalla Agregar Ocasión Especial**:

```text
┌──────────────────────────────────────────────┐
│ <  Agregar Ocasión Especial                      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📝 Información de la Ocasión                      │
│                                               │
│ Nombre de la Ocasión *                       │
│ [ Cumpleaños de An                      ]       │
│                                               │
│ Fecha                                          │
│ [ 01 / 05            ▼ ]                      │
│ (DatePicker solo selecciona día/mes)          │
│                                               │
│ [ ] Usar calendario lunar                        │
│                                               │
│ Repetir                                        │
│ (•) Anualmente                                     │
│ ( ) Solo este año                            │
│                                               │
│ Mostrar notificación a las *                        │
│ [ 07:00        ▼ ]                            │
│                                               │
│ Nota (opcional)                                │
│ [                                      ]      │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ 📋 Pasos de Preparación          [ + Agregar Paso ]│
│ ┌──────────────────────────────────────────┐ │
│ │  1. Comprar regalo                   [Icono Eliminar] │ │
│ │     7 días antes – 08:00                 │ │
│ │ ──────────────────────────────────────── │ │
│ │  2. Pedir pastel                   [Icono Eliminar] │ │
│ │     1 día antes – 19:00                 │ │
│ └──────────────────────────────────────────┘ │
└──────────────────────────────────────────────┘

        [ Cancelar ]                        [ Guardar ]
```

---

### 5.2 OCCASION-02: Crear ocasión especial con calendario lunar (Día de Conmemoración con lista de compras)

**Objetivo**: Crear ocasión especial con calendario lunar (día de conmemoración) con pasos de preparación vinculados a lista de compras para rastrear compra de ofrendas.

**Pasos principales**:
1. Vaya a Funciones → Ocasiones Especiales → Toque el botón "➕" (FAB)
2. Ingrese nombre de ocasión "Día de Conmemoración de Mamá", marque "Usar calendario lunar"
3. Ingrese fecha lunar: 15/11, la app calcula automáticamente fecha solar: 15/12/2025
4. Agregue 3 pasos de preparación, donde el paso 2 tiene vínculo de lista de compras "Comprar ofrendas"
5. Toque "Guardar"

**Ilustración de UI - Seleccionar fecha lunar**:

```text
│ │ │ Fecha lunar                                   │ │ │
│ │ │ Día (1-30)    Mes (1-12)                   │ │ │
│ │ │ [ 15 ]        [ 11 ]                         │ │ │
│ │ │                                               │ │ │
│ │ │ Fecha solar (calculada automáticamente - solo visualización)  │ │ │
│ │ │ [ Texto: 15/12/2025                 ]         │ │ │
│ │ │ (Esta es la PRÓXIMA fecha solar en el futuro)│ │ │
```

---

### 5.3 OCCASION-03: Ver lista y detalles de ocasiones especiales

**Objetivo**: Ver resumen de ocasiones especiales, filtrar por tiempo y ver detalles de cada ocasión con progreso de preparación.

**Pasos principales**:
1. Vaya a Funciones → Ocasiones Especiales
2. Muestre lista con filtros "Todas", "Próximas", "Este mes"
3. Toque la tarjeta de ocasión para ver detalles
4. Muestre resumen: Número de pasos, Completados, Estado
5. Marque paso como completado marcando la casilla

**Ilustración de UI - Pantalla Lista de Ocasiones Especiales**:

```text
┌────────────────────────────────────────────────────────────┐
│ 📅 Lista de Ocasiones Especiales                                  │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ + Agregar Ocasión ]                                     │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔍 Filtro: [ Todas ]  [ Próximas ]  [ Este mes ]      │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Día de Conmemoración de Mamá    [En progreso] [Icono Eliminar] │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 📅 15/12/2025 • 15/11 (Lunar) • 10 días restantes  │ │ │
│ │ │                                                      │ │ │
│ │ │ ✅ Pasos de preparación requeridos:                        │ │ │
│ │ │   [✓] 3 días antes – Listar ofrendas               │ │ │
│ │ │   [ ] 1 día antes – Comprar ofrendas     │ │ │
│ │ │   [ ] El día – Preparar altar / ceremonia        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

**Ilustración de UI - Pantalla Detalles de Ocasión Especial**:

```text
┌─────────────────────────────────────────────────────────┐
│ 📋 Detalles de Ocasión Especial                             │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📌 Día de Conmemoración de Mamá                       [Editar ›]        │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ 15/12/2025 (Solar) • 15/11 (Calendario lunar)      │ │ │
│ │ │ 10 días restantes • Repetir: Anualmente                │ │ │
│ │ │                                                      │ │ │
│ │ │ Nota:                                             │ │ │
│ │ │ Comida pequeña, flores blancas, limitar invitados.          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📊 Resumen                                         │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Pasos de preparación: 3                              │ │ │
│ │ │ Completados: 1 / 3                                 │ │ │
│ │ │ Estado: [En progreso]                            │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Pasos de Preparación                  [ + Agregar Paso ]                  │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ [✓] Listar ofrendas                    [Icono Eliminar]           │ │ │
│ │ │     3 días antes – 08:00                        │ │ │
│ │ │     Completado a las 09:15 – 12/12/2025               │ │ │
│ │ │ ──────────────────────────────────────────────────── │ │ │
│ │ │                                                      │ │ │
│ │ │ [ ] Comprar ofrendas            [Icono Eliminar]            │ │ │
│ │ │     1 día antes – 19:00                      │ │ │
│ │ │     Repetir diariamente hasta completar                  │ │ │
│ │ │     Lista de compras: Comprar ofrendas ›           │ │ │
│ │ │     [✓] Completado 3 / 8 elementos                        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
```

---

### 5.4 OCCASION-04: Agregar paso de preparación con lista de compras

**Objetivo**: Agregar nuevo paso de preparación para ocasión especial y vincularlo con lista de compras para rastrear compras.

**Pasos principales**:
1. Vaya a detalles de ocasión especial → Toque "+ Agregar Paso"
2. Seleccione "¿Cuándo?": "X días antes", ingrese número de días: 1
3. Seleccione hora de recordatorio: 19:00
4. Active "Repetir diariamente hasta completar"
5. Ingrese contenido: "Comprar ofrendas"
6. Marque "Usar lista de compras" → Seleccione lista de compras "Comprar ofrendas"
7. Toque "Agregar"

**Ilustración de UI - Pantalla Agregar Paso de Preparación**:

```text
┌────────────────────────────────────────────────────────────┐
│ ➕ Agregar Paso de Preparación                                     │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ ⏰ Tiempo de Preparación                                    │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ¿Cuándo? * (requerido)                                │ │ │
│ │ │ [ X días antes         ▼ ]                       │ │ │
│ │ │                                                      │ │ │
│ │ │ Número de días * (solo se muestra si "X días antes") │ │ │
│ │ │ [  1  ]  días antes                               │ │ │
│ │ │                                                      │ │ │
│ │ │ Mostrar notificación a las * (requerido)                  │ │ │
│ │ │ [ 19:00        ▼ ]                                 │ │ │
│ │ │                                                      │ │ │
│ │ │ [✓] Repetir diariamente hasta completar                    │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 📝 Contenido                                             │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ Contenido * (requerido)                              │ │ │
│ │ │ [ Comprar ofrendas               ]        │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ 🔗 ¿Vincular con lista de compras?                       │ │
│ │ ┌────────────────────────────────────────────────────┐ │ │
│ │ │ ☑ Usar lista de compras                                    │ │ │
│ │ │ Lista de compras: Comprar ofrendas ›    [Icono Cambiar]  │ │ │
│ │ │ (8 elementos)                                          │ │ │
│ │ └────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                              │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ [ Cancelar ]                        [ Agregar ]             │ │
│ └────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

### 5.5 OCCASION-05: Marcar paso de preparación como completado y mostrar progreso de lista de compras

**Objetivo**: Marcar pasos de preparación como completados y rastrear progreso de lista de compras.

**Pasos principales**:
1. Vaya a detalles de ocasión especial
2. Muestre paso con lista de compras que muestra progreso "Completado 3 / 8 elementos"
3. Toque nombre de lista de compras para ver detalles y marcar/desmarcar elementos
4. Marque casilla del paso para marcar como completado
5. Muestre "Resumen" actualizado en tiempo real

---

### 5.6 OCCASION-06: Editar ocasión especial y pasos de preparación

**Objetivo**: Editar información de ocasión especial y pasos de preparación después de crearlos.

**Pasos principales**:
1. Vaya a detalles de ocasión especial → Toque "Editar ›"
2. Edite nombre de ocasión, nota
3. Toque "Guardar"
4. Toque paso para editar: Cambie tiempo, contenido
5. Toque icono Eliminar para eliminar paso (tiene diálogo de confirmación)

## 6. Lógica y reglas

### 6.1 Datos de calendario lunar

- Puede ingresar tanto fechas solares como lunares
- La app calcula automáticamente la fecha solar correspondiente a la fecha lunar
- Soporta repetición anual según calendario lunar

### 6.2 Repetir

- **Anualmente**: La ocasión se repite cada año (según calendario solar o lunar)
  - Con calendario solar: Cada año calcula nextOccurDate basado en (día/mes) de solarDate
  - Con calendario lunar: Cada año convierte de fecha lunar a fecha solar correspondiente y actualiza nextOccurDate
- **Solo este año**: La ocasión solo es válida en el año actual, no se repite el próximo año

### 6.3 Pasos de preparación

- **¿Cuándo?**: Tiene 2 opciones:
  - **X días antes**: Recordar X días antes de la fecha de la ocasión (debe ingresar número de días)
  - **El día**: Recordar en la fecha de la ocasión (no necesita ingresar número de días)
- **Mostrar notificación a las**: Hora de recordatorio (requerido, formato HH:mm)
- **Repetir diariamente hasta completar**: Si está activado, la notificación se repite diariamente hasta que el usuario marque el paso como completado
- **Vincular lista de compras**: Cada paso puede adjuntar una lista de compras para rastrear progreso de compras

### 6.4 Lista de compras

- La lista de compras puede reutilizarse para múltiples pasos
- Rastrea número de elementos completados / Total de elementos (ej. "Completado 3 / 8 elementos")
- Se muestra en detalles del paso con vínculo "Nombre de lista de compras ›" para ver detalles
- Puede marcar/desmarcar elementos en la lista de compras para actualizar progreso
- El paso de preparación puede marcarse como completado incluso si la lista de compras no está completamente completada

### 6.5 Notificaciones

- **Notificación de ocasión principal**: Creada en `nextOccurDate + reminder_time`
  - Con ocasión ANUAL: La notificación se recrea cuando la app inicia (basado en nextOccurDate recién calculado)
  - Con ocasión UNA VEZ: La notificación se crea solo una vez para el nextOccurDate actual
- **Notificación de paso de preparación**: Calcule fecha de recordatorio basado en:
  - `nextOccurDate` de la ocasión especial
  - `reminderType` y `daysBefore` (si existe)
  - `reminderTime`
- **Notificación de repetición**: Si `repeatDailyUntilComplete = true`:
  - Cree notificación de repetición diaria
  - Use `notificationGroupKey` para agrupar notificaciones de repetición
  - Se cancela automáticamente cuando el usuario marca el paso como completado

## 7. Notas importantes

- **Datos de calendario lunar**: 
  - La app convierte automáticamente a calendario solar para visualización
  - Encuentra "PRÓXIMA fecha solar en el futuro" en comparación con la fecha actual
  - Años futuros: El sistema siempre calcula la fecha solar correspondiente desde (día lunar, mes lunar) para cada año nuevamente
  - Si este año tiene tanto mes regular como mes intercalar del mismo mes: El sistema puede crear 2 recordatorios para evitar que falte algo
- **Repetición anual**: 
  - La ocasión recalcula automáticamente nextOccurDate el próximo año
  - Con calendario lunar: Cada año convierte de fecha lunar a fecha solar correspondiente
- **Hora de recordatorio**: 
  - Debe tener un valor (no puede estar vacío)
  - Debe tener formato correcto HH:mm (00:00 - 23:59)
- **Lista de compras**: 
  - La lista de compras eliminada todavía se muestra en el paso (pero no se puede editar)
  - Puede marcar el paso como completado incluso si la lista de compras no está completamente completada
- **Notificaciones**: 
  - Debe activar notificaciones en Configuración para recibir recordatorios
  - Las notificaciones de repetición se cancelan automáticamente cuando el paso se marca como completado
- **Estado de ocasión**:
  - **No iniciado**: Todos los pasos no están completados (gris)
  - **En progreso**: Al menos 1 paso está completado, pero no todos (azul)
  - **Completado**: Todos los pasos están completados (verde oscuro)
  - Si la ocasión no tiene pasos de preparación: El estado se calcula según la fecha (No iniciado / En curso / Completado)

