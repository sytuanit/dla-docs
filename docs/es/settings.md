# Configuración

## 1. Propósito

El módulo **Configuración** le permite configurar la aplicación según sus necesidades personales, incluyendo:
- Idioma y moneda
- Notificaciones
- Categorías
- Copia de seguridad y restauración de datos
- Seguridad (contraseña, Face ID)

## 2. Cuándo usar

Use este módulo cuando desee:
- Cambiar idioma o moneda
- Activar/desactivar notificaciones
- Gestionar categorías (agregar, editar, eliminar, establecer como predeterminada)
- Hacer copia de seguridad o restaurar datos
- Cambiar contraseña o activar Face ID

## 3. Pantallas relacionadas

- Pantalla principal de configuración
- Configuración básica
- Seleccionar idioma
- Seleccionar moneda
- Gestionar categorías
- Hacer copia de seguridad de datos
- Restaurar datos
- Cambiar contraseña
- Activar Face ID / Huella dactilar

## 4. Uso principal

### 4.1 Cambiar idioma

1. Vaya a **Configuración** → **Pantalla e Idioma** → **Idioma**
2. Seleccione el idioma deseado
3. La aplicación se recarga automáticamente con el nuevo idioma

### 4.2 Cambiar moneda

1. Vaya a **Configuración** → **Pantalla e Idioma** → **Moneda**
2. Seleccione el tipo de moneda
3. Todos los montos se mostrarán en la nueva unidad

### 4.3 Activar/desactivar notificaciones

1. Vaya a **Configuración** → **Notificaciones**
2. Cambie el interruptor **Notificaciones**
3. Si está activado, recibirá recordatorios sobre:
   - Ingresos recurrentes vencidos
   - Gastos recurrentes vencidos
   - Cuentas de ahorro vencidas
   - Ocasiones especiales próximas

### 4.4 Gestionar categorías

1. Vaya a **Configuración** → **Categorías**
2. Seleccione el tipo de categoría a gestionar:
   - Ingresos recurrentes
   - Ingresos extra
   - Gastos recurrentes
   - Gastos diarios
3. Agregar/editar/eliminar categorías
4. Establecer categoría predeterminada (para gastos diarios)

### 4.5 Hacer copia de seguridad de datos

1. Vaya a **Configuración** → **Copia de Seguridad y Datos** → **Copia de Seguridad**
2. Seleccione ubicación de almacenamiento (sistema de archivos)
3. Toque **Hacer Copia de Seguridad**
4. Se crea el archivo de copia de seguridad

### 4.6 Restaurar datos

1. Vaya a **Configuración** → **Copia de Seguridad y Datos** → **Restaurar**
2. Seleccione el archivo de copia de seguridad
3. Confirme la restauración
4. **Nota**: La restauración sobrescribe los datos actuales

## 5. Ilustraciones de UI (Wireframe)

### 5.1 Pantalla principal de configuración

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Configuración                    │
├─────────────────────────────────────────┤
│  Pantalla e Idioma                     │
│  ┌───────────────────────────────────┐ │
│  │ Idioma                           │ │
│  │ Español                      →     │ │
│  │                                    │ │
│  │ Moneda                           │ │
│  │ EUR (€)                      →     │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Notificaciones                          │
│  ┌───────────────────────────────────┐ │
│  │ Notificaciones                [ON]  │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Copia de Seguridad y Datos                          │
│  ┌───────────────────────────────────┐ │
│  │ Copia de Seguridad                        →    │ │
│  │                                    │ │
│  │ Restaurar                       →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Categorías                             │
│  ┌───────────────────────────────────┐ │
│  │ Gestionar categorías              →    │ │
│  └───────────────────────────────────┘ │
│                                         │
│  Seguridad                               │
│  ┌───────────────────────────────────┐ │
│  │ Contraseña                        →    │ │
│  │                                    │ │
│  │ Face ID / Huella dactilar          →    │ │
│  └───────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

## 6. Lógica y reglas

### 6.1 Idioma

- Compatible con: Español, English, Tiếng Việt, 日本語
- El cambio de idioma recarga toda la aplicación
- Las categorías del sistema se traducen automáticamente al nuevo idioma

### 6.2 Moneda

- Cada idioma tiene moneda predeterminada (ej. EUR para Español)
- Puede seleccionar otra moneda
- Todos los montos se formatean según la moneda seleccionada

### 6.3 Notificaciones

- Las notificaciones solo funcionan si la aplicación tiene permiso
- El tiempo de notificación depende de cada función y puede configurarse:
  - Ingresos/Gastos recurrentes: `notificationTime1`, `notificationTime2` (por defecto 16:00 y 19:00)
  - Cuentas de ahorro y préstamos: `notificationTime1`, `notificationTime2` (por defecto 10:00 y 19:00)
  - Ocasiones especiales y pasos de preparación: según `reminderTime` que ingrese
  - Puede desactivar notificaciones para cada tipo por separado (en el futuro)

### 6.4 Categorías

- Las categorías del sistema no se pueden eliminar, solo desactivar
- Las categorías de usuario se pueden eliminar (si no están en uso)
- Cada tipo de categoría es independiente (ingresos recurrentes, gastos diarios, etc.)

## 7. Notas importantes

- **Hacer copia de seguridad regularmente**: Debe hacer copia de seguridad periódicamente para evitar pérdida de datos
- **La restauración sobrescribe**: La restauración reemplaza todos los datos actuales
- **Contraseña**: Si olvida la contraseña, puede restablecerla (elimina datos)

