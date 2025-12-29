# Ingresos Recurrentes

## 1. Propósito

El módulo **Ingresos Recurrentes** le ayuda a gestionar fuentes de ingresos regulares como:
- Salario mensual
- Ingresos por alquiler
- Pensión
- Dividendos de inversiones
- Otros ingresos recurrentes

Este módulo crea automáticamente **Ocurrencias** basadas en el ciclo que configure y le recuerda cuando es momento de recibir el pago.

## 2. Cuándo usar

Use este módulo cuando tenga:
- Ingresos fijos según horario (semanal, quincenal o mensual)
- Necesite rastrear y confirmar cuándo se recibió el pago
- Desee cálculo automático en presupuesto mensual

## 3. Pantallas relacionadas

- Lista de ingresos recurrentes
- Agregar nuevo ingreso recurrente
- Editar ingreso recurrente
- Historial de ocurrencias

## 4. Uso principal

### 4.1 Agregar nuevo ingreso recurrente

1. Vaya a **Funciones** → Seleccione **Ingresos Recurrentes**
2. Toque el botón **+** (FAB) en la esquina inferior derecha
3. Complete la información:
   - **Categoría**: Seleccione una categoría o cree una nueva
   - **Cantidad**: Ingrese el monto del ingreso (puede dejarse vacío, ingresar al confirmar)
   - **Ciclo**: Seleccione Semanal / Quincenal / Mensual
   - **Fecha**: Seleccione la fecha en el ciclo (ej. día 15 de cada mes)
   - **Fecha de inicio**: (Solo para ciclo quincenal) Seleccione fecha de inicio
   - **Nota**: Información adicional (opcional)
4. Toque **Guardar**

### 4.2 Confirmar recepción de pago

1. Vaya a la lista de ingresos recurrentes
2. Encuentre el elemento con badge **"Pendiente de confirmación"** (amarillo)
3. Toque el elemento para abrir el diálogo de confirmación
4. Complete:
   - **Cantidad real**: (si es diferente a la esperada)
   - **Nota**: (opcional)
5. Toque **Confirmar**

### 4.3 Editar ingreso recurrente

1. Vaya a la lista de ingresos recurrentes
2. Toque el elemento a editar
3. Seleccione **Editar** del menú
4. Actualice la información
5. Toque **Guardar**

### 4.4 Ver historial

1. Vaya a la lista de ingresos recurrentes
2. Toque un elemento
3. Seleccione **Historial** para ver todas las ocurrencias pasadas

### 4.5 Desactivar/activar ingreso

1. Vaya a la lista de ingresos recurrentes
2. Encuentre el elemento a desactivar/activar
3. Cambie el interruptor **Activo** en el lado derecho del elemento

## 5. Ejemplos e ilustraciones de UI

### 5.1 Ejemplo 1: Crear ingreso recurrente mensual (Salario)

**Escenario**: Desea rastrear el salario mensual para que la aplicación le recuerde automáticamente cuando es momento de recibir el pago.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Ingresos Recurrentes"
2. Toque el botón "➕ Agregar nuevo" en la esquina inferior derecha
3. Seleccione categoría "Salario" (o cree nueva si no está disponible)
4. Ingrese cantidad: €3,600
5. Seleccione ciclo "Mensual"
6. Seleccione "Seleccionar día del mes", ingrese 5
7. Nota automáticamente completada "Salario mensual" (puede editarse)
8. Toque "Guardar"

**Resultado**: La aplicación muestra mensaje de éxito y regresa a la lista. El nuevo elemento aparece con información completa, y la aplicación le recordará automáticamente el día 5 de cada mes.

**Pantalla "Agregar ingreso recurrente"**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Agregar Ingreso Recurrente │
├─────────────────────────────────────────┤
│  Categoría *                              │
│  [Salario ▼] [+ Crear nuevo]                 │
│                                         │
│  Cantidad (EUR) *                          │
│  [€3,600]                               │
│                                         │
│  Ciclo *                                 │
│  ┌──────┐ ┌────────┐ ┌────────┐        │
│  │Semana│ │Quincen│ │Mensual│        │
│  └──────┘ └────────┘ └────────┘        │
│                                         │
│  Fecha de pago en el ciclo                  │
│  ⚪ Fin de mes                         │
│  ⚫ Seleccionar día del mes                  │
│  ┌───────────────────────────────────┐ │
│  │ Día del mes: [5]                 │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Nota                                    │
│  ┌───────────────────────────────────┐ │
│  │ Salario mensual                     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Cancelar]                  [Guardar]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Ejemplo 2: Confirmar ingreso vencido y actualizar cantidad real

**Escenario**: Es día de pago (5), pero la cantidad realmente recibida es €3,780 (aumento de salario) en lugar de €3,600 como estaba configurado.

**Pasos**:
1. Abra la aplicación o vaya a la pantalla "Ingresos Recurrentes"
2. La aplicación detecta automáticamente la ocurrencia vencida y muestra el diálogo de confirmación
3. El diálogo muestra cantidad estándar: €3,600
4. Actualice la cantidad real a €3,780
5. Ingrese nota: "Este mes tiene bono" (opcional)
6. Toque "Confirmar recepción"

**Resultado**: La aplicación actualiza la ocurrencia confirmada con cantidad real €3,780, crea automáticamente la próxima ocurrencia y actualiza el saldo financiero actual.

**Diálogo de confirmación de ingreso**:

```text
┌─────────────────────────────────────────┐
│  Confirmar recepción                        │
├─────────────────────────────────────────┤
│  Salario                                  │
│  Mensual (5.)                          │
│  Fecha de vencimiento: Hoy                        │
│                                         │
│  Cantidad real *                         │
│  [€3,780]                               │
│                                         │
│  Nota                                    │
│  [Este mes tiene bono]                 │
│                                         │
│  [Cancelar este]    [Confirmar recepción]   │
└─────────────────────────────────────────┘
```

---

### 5.3 Ejemplo 3: Cancelar ocurrencia de ingreso cuando no se recibió el pago

**Escenario**: Es día de pago de alquiler (1), pero el inquilino no transfirió dinero, por lo que no se recibió el pago.

**Pasos**:
1. Abra la aplicación o vaya a la pantalla "Ingresos Recurrentes"
2. La aplicación muestra el diálogo de confirmación para la ocurrencia vencida
3. Toque el botón "Cancelar este"
4. Ingrese razón: "Inquilino no transfirió dinero" (requerido)
5. Toque "Confirmar cancelación"

**Resultado**: La ocurrencia cancelada cambia a estado "Cancelado", muestra la razón de cancelación, y la aplicación crea automáticamente la próxima ocurrencia. El saldo financiero no cambia ya que no se recibió ningún pago.

**Diálogo "Cancelar ocurrencia de ingreso"**:

```text
┌─────────────────────────────────────────┐
│  Cancelar este                              │
├─────────────────────────────────────────┤
│  Ingresos por alquiler                            │
│  Mensual (1.)                           │
│  Fecha de vencimiento: Hoy                         │
│                                         │
│  Razón de cancelación *                    │
│  ┌───────────────────────────────────┐ │
│  │ Inquilino no transfirió dinero    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Atrás]        [Confirmar cancelación]         │
└─────────────────────────────────────────┘
```

---

## 6. Lógica y reglas

### 6.1 Ciclo y fecha

- **Semanal**: Seleccionar día de la semana (1=Lunes, 7=Domingo)
- **Quincenal**: Seleccionar día de la semana + fecha de inicio específica
- **Mensual**: Seleccionar día del mes (1-31)

### 6.2 Creación automática de ocurrencias

- La aplicación crea automáticamente **Ocurrencias** cuando:
  - Agrega nuevo ingreso
  - Alcanza la fecha en el ciclo
  - Comienza nuevo mes

### 6.3 Estado de ocurrencia

- **PENDIENTE**: Pendiente de confirmación (muestra badge amarillo)
- **COMPLETADO**: Confirmado (muestra badge verde)
- **CANCELADO**: Cancelado (muestra badge rojo)

### 6.4 Integración con presupuesto

- Al confirmar el ingreso, la aplicación actualiza automáticamente el presupuesto del mes actual (si existe)
- El ingreso se calcula en "Ingresos Recurrentes" en el presupuesto

### 6.5 Notificaciones

- La aplicación envía notificación de recordatorio cuando el pago está vencido
- El tiempo de notificación puede configurarse para cada elemento (`notificationTime1`, `notificationTime2`, por defecto 16:00 y 19:00)

## 7. Notas importantes

- **La cantidad puede dejarse vacía**: Si no conoce la cantidad exacta, puede dejarla vacía e ingresarla al confirmar
- **No se puede eliminar si existe ocurrencia**: Si hay ocurrencias, solo puede desactivar (isActive = false), no eliminar
- **Confirmación tardía**: Puede confirmar ocurrencias pasadas, la aplicación recalcula el presupuesto automáticamente
- **Cambiar ciclo**: Al editar el ciclo, las ocurrencias futuras se recalculan

