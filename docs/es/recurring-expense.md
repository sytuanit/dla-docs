# Gastos Recurrentes

## 1. Propósito

El módulo **Gastos Recurrentes** le ayuda a gestionar gastos periódicos con ciclos fijos como:
- Facturas de electricidad, agua, gas
- Internet, televisión por cable
- Seguro
- Matrícula escolar
- Alquiler
- Otros gastos recurrentes

Este módulo crea automáticamente **Ocurrencias** basadas en el ciclo que configure y le recuerda cuando el pago está vencido.

## 2. Cuándo usar

Use este módulo cuando tenga:
- Gastos fijos según horario (semanal, quincenal o mensual)
- Necesite rastrear y confirmar cuándo se realizó el pago
- Desee cálculo automático en presupuesto mensual

## 3. Pantallas relacionadas

- Lista de gastos recurrentes
- Agregar nuevo gasto recurrente
- Editar gasto recurrente
- Historial de ocurrencias

## 4. Uso principal

### 4.1 Agregar nuevo gasto recurrente

1. Vaya a **Funciones** → Seleccione **Gastos Recurrentes**
2. Toque el botón **+** (FAB) en la esquina inferior derecha
3. Complete la información:
   - **Categoría**: Seleccione una categoría o cree una nueva
   - **Cantidad**: Ingrese el monto del gasto (puede dejarse vacío, ingresar al confirmar)
   - **Ciclo**: Seleccione Semanal / Quincenal / Mensual
   - **Fecha**: Seleccione la fecha en el ciclo (ej. día 15 de cada mes)
   - **Fecha de inicio**: (Solo para ciclo quincenal) Seleccione fecha de inicio
   - **Nota**: Información adicional (opcional)
4. Toque **Guardar**

### 4.2 Confirmar pago

1. Vaya a la lista de gastos recurrentes
2. Encuentre el elemento con badge **"Pendiente de confirmación"** (amarillo)
3. Toque el elemento para abrir el diálogo de confirmación
4. Complete:
   - **Cantidad real**: (si es diferente a la esperada)
   - **Nota**: (opcional)
5. Toque **Confirmar**

### 4.3 Editar gasto recurrente

1. Vaya a la lista de gastos recurrentes
2. Toque el elemento a editar
3. Seleccione **Editar** del menú
4. Actualice la información
5. Toque **Guardar**

### 4.4 Ver historial

1. Vaya a la lista de gastos recurrentes
2. Toque un elemento
3. Seleccione **Historial** para ver todas las ocurrencias pasadas

### 4.5 Desactivar/activar gasto

1. Vaya a la lista de gastos recurrentes
2. Encuentre el elemento a desactivar/activar
3. Cambie el interruptor **Activo** en el lado derecho del elemento

## 5. Ejemplos e ilustraciones de UI

### 5.1 Ejemplo 1: Crear gasto recurrente mensual (Factura de electricidad)

**Escenario**: Desea rastrear la factura mensual de electricidad para que la aplicación le recuerde automáticamente cuando el pago está vencido.

**Pasos**:
1. Vaya a la pantalla de Funciones, seleccione "Gastos Recurrentes"
2. Toque el botón "➕ Agregar nuevo" en la esquina inferior derecha
3. Seleccione categoría "Servicios públicos" (o cree nueva si no está disponible)
4. Ingrese cantidad: €18
5. Seleccione ciclo "Mensual"
6. Seleccione "Seleccionar día del mes", ingrese 15
7. Nota automáticamente completada "Factura mensual de electricidad" (puede editarse)
8. Toque "Guardar"

**Resultado**: La aplicación muestra mensaje de éxito y regresa a la lista. El nuevo elemento aparece con información completa, y la aplicación le recordará automáticamente el día 15 de cada mes.

**Pantalla "Agregar gasto recurrente"**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Agregar Gasto Recurrente        │
├─────────────────────────────────────────┤
│  Categoría *                              │
│  [Servicios públicos ▼] [+ Crear nuevo]             │
│                                         │
│  Cantidad (EUR) *                          │
│  [€18]                                  │
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
│  │ Día del mes: [15]                │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Nota                                    │
│  ┌───────────────────────────────────┐ │
│  │ Factura mensual de electricidad           │
│  └───────────────────────────────────┘ │
│                                         │
│  [Cancelar]                  [Guardar]       │
└─────────────────────────────────────────┘
```

---

### 5.2 Ejemplo 2: Confirmar gasto vencido y actualizar cantidad real

**Escenario**: Es día de pago de factura de agua (10), pero la cantidad realmente a pagar es €6.30 (reducida) en lugar de €7.20 como estaba configurado.

**Pasos**:
1. Abra la aplicación o vaya a la pantalla "Gastos Recurrentes"
2. La aplicación detecta automáticamente la ocurrencia vencida y muestra el diálogo de confirmación
3. El diálogo muestra cantidad estándar: €7.20
4. Actualice la cantidad real a €6.30
5. Ingrese nota: "Este mes ahorré agua" (opcional)
6. Toque "Confirmar pago"

**Resultado**: La aplicación actualiza la ocurrencia confirmada con cantidad real €6.30, crea automáticamente la próxima ocurrencia y actualiza el saldo financiero actual (resta €6.30).

**Diálogo de confirmación de gasto**:

```text
┌─────────────────────────────────────────┐
│  Confirmar pago                           │
├─────────────────────────────────────────┤
│  Factura de agua                              │
│  Mensual (10.)                         │
│  Fecha de vencimiento: Hoy                        │
│                                         │
│  Cantidad real *                         │
│  [€6.30]                                   │
│                                         │
│  Nota                                    │
│  [Este mes ahorré agua]               │
│                                         │
│  [Cancelar este]    [Confirmar pago]        │
└─────────────────────────────────────────┘
```

---

### 5.3 Ejemplo 3: Desactivar gasto recurrente cuando ya no es aplicable

**Escenario**: Alquila temporalmente durante 2 meses sin apartamento, por lo que desea desactivar el gasto "Alquiler" en lugar de eliminarlo completamente.

**Pasos**:
1. Vaya a la pantalla "Gastos Recurrentes"
2. Encuentre el elemento "Alquiler" en la lista
3. Toque el interruptor "Activo" en el lado derecho del elemento
4. La aplicación muestra diálogo de confirmación: "¿Está seguro de que desea desactivar este gasto?"
5. Toque el botón "Desactivar" para confirmar

**Resultado**: La tarjeta "Alquiler" cambia a estado "Inactivo" (gris), el interruptor cambia a "Inactivo". La aplicación ya no crea nuevas ocurrencias para este gasto. Puede reactivar tocando el interruptor "Inactivo" → "Activo".

**Lista con interruptor**:

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Gastos Recurrentes           │
├─────────────────────────────────────────┤
│  ┌───────────────────────────────────┐ │
│  │ Alquiler              [⚪ Inactivo]   │ │
│  │ €1,080                            │
│  │ Mensual - 1.                     │
│  │ (Desactivado)                     │
│  │                                    │
│  │ [Editar] [Historial] [Eliminar]         │
│  └───────────────────────────────────┘ │
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
  - Agrega nuevo gasto
  - Alcanza la fecha en el ciclo
  - Comienza nuevo mes

### 6.3 Estado de ocurrencia

- **PENDIENTE**: Pendiente de confirmación (muestra badge amarillo)
- **COMPLETADO**: Confirmado (muestra badge verde)
- **CANCELADO**: Cancelado (muestra badge rojo)

### 6.4 Integración con presupuesto

- Al confirmar el gasto, la aplicación actualiza automáticamente el presupuesto del mes actual (si existe)
- El gasto se calcula en "Gastos Recurrentes" en el presupuesto

### 6.5 Notificaciones

- La aplicación envía notificación de recordatorio cuando el pago está vencido
- El tiempo de notificación puede configurarse para cada elemento (`notificationTime1`, `notificationTime2`, por defecto 16:00 y 19:00)

## 7. Notas importantes

- **La cantidad puede dejarse vacía**: Si no conoce la cantidad exacta, puede dejarla vacía e ingresarla al confirmar
- **No se puede eliminar si existe ocurrencia**: Si hay ocurrencias, solo puede desactivar (isActive = false), no eliminar
- **Confirmación tardía**: Puede confirmar ocurrencias pasadas, la aplicación recalcula el presupuesto automáticamente
- **Cambiar ciclo**: Al editar el ciclo, las ocurrencias futuras se recalculan

