# Copia de Seguridad y Restauración

## 1. Propósito

El módulo **Copia de Seguridad y Restauración** le ayuda a:
- Hacer copia de seguridad de todos los datos de la aplicación en un archivo
- Restaurar datos desde un archivo de copia de seguridad
- Proteger datos contra pérdida por fallos del dispositivo o reinstalación de la aplicación

## 2. Cuándo usar

Use este módulo cuando desee:
- Hacer copia de seguridad de datos antes de reinstalar la aplicación
- Transferir datos a un nuevo dispositivo
- Restaurar datos después de pérdida de datos
- Crear copias de seguridad periódicas

## 3. Pantallas relacionadas

- Pantalla de copia de seguridad
- Pantalla de restauración

## 4. Uso principal

### 4.1 Hacer copia de seguridad de datos

1. Vaya a **Configuración** → **Copia de Seguridad y Datos** → **Copia de Seguridad**
2. Ver información:
   - Número de registros a respaldar
   - Tamaño de archivo esperado
3. Toque **Hacer Copia de Seguridad**
4. Seleccione ubicación de almacenamiento (sistema de archivos)
5. Se crea el archivo de copia de seguridad con nombre: `dla-backup-YYYY-MM-DD-HHmmss.json`
6. Guarde este archivo en un lugar seguro (nube, computadora, etc.)

### 4.2 Restaurar datos

1. Vaya a **Configuración** → **Copia de Seguridad y Datos** → **Restaurar**
2. Seleccione el archivo de copia de seguridad del sistema de archivos
3. Ver información del archivo:
   - Fecha de creación de la copia de seguridad
   - Número de registros
   - Tamaño del archivo
4. **Advertencia**: La restauración sobrescribe todos los datos actuales
5. Toque **Restaurar**
6. Confirme la restauración
7. Espere hasta que se complete el proceso de restauración
8. La aplicación se recarga automáticamente

## 5. Ilustraciones de UI (Wireframe)

### 5.1 Pantalla de copia de seguridad

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Hacer Copia de Seguridad de Datos                   │
├─────────────────────────────────────────┤
│  Información de copia de seguridad                      │
│                                         │
│  ┌───────────────────────────────────┐ │
│  │ Número de registros                  │ │
│  │ 1.234 registros                      │ │
│  │                                    │
│  │ Tamaño esperado                      │ │
│  │ ~2,5 MB                            │ │
│  │                                    │
│  │ Datos a respaldar:              │ │
│  │ • Ingresos recurrentes                 │ │
│  │ • Gastos recurrentes               │ │
│  │ • Gastos diarios                   │ │
│  │ • Presupuesto                           │ │
│  │ • Ahorros                          │ │
│  │ • Préstamos                            │ │
│  │ • Ocasiones especiales                │ │
│  │ • Categorías                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  [Hacer Copia de Seguridad]                               │
└─────────────────────────────────────────┘
```

### 5.2 Pantalla de restauración

```text
┌─────────────────────────────────────────┐
│  ← Atrás    Restaurar Datos                 │
├─────────────────────────────────────────┤
│  Seleccionar archivo de copia de seguridad                      │
│                                         │
│  [Seleccionar archivo...]                       │
│                                         │
│  Información del archivo                       │
│  ┌───────────────────────────────────┐ │
│  │ Archivo: dla-backup-2024-11-15.json │ │
│  │                                    │ │
│  │ Creado: 15/11/2024 10:30         │ │
│  │                                    │ │
│  │ Número de registros: 1.234         │ │
│  │                                    │ │
│  │ Tamaño: 2,5 MB                       │ │
│  └───────────────────────────────────┘ │
│                                         │
│  ⚠️ Advertencia                             │
│  La restauración sobrescribe todos los datos actuales     │
│  datos. ¿Está seguro?                    │
│                                         │
│  [Restaurar] [Cancelar]                     │
└─────────────────────────────────────────┘
```

## 6. Lógica y reglas

### 6.1 Formato de archivo de copia de seguridad

- El archivo de copia de seguridad está en formato JSON
- Nombre de archivo: `dla-backup-YYYY-MM-DD-HHmmss.json`
- Contiene todos los datos: usuario, categorías, transacciones, presupuestos, etc.

### 6.2 Datos respaldados

- Todas las tablas en la base de datos
- Incluye tanto datos del sistema como datos del usuario
- No incluye: configuración de la aplicación, preferencias (idioma, moneda)

### 6.3 Restauración

- La restauración elimina todos los datos actuales
- Luego importa datos desde el archivo de copia de seguridad
- La aplicación se recarga automáticamente después de completar la restauración

### 6.4 Validación

- La aplicación verifica el formato del archivo antes de restaurar
- Verifica compatibilidad de versión (si existe)
- Muestra error si el archivo es inválido

## 7. Notas importantes

- **Hacer copia de seguridad regularmente**: Debe hacer copia de seguridad periódicamente (semanal o mensual)
- **Guardar en múltiples lugares**: Guarde el archivo de copia de seguridad en múltiples lugares (nube, computadora, USB)
- **La restauración pierde datos actuales**: Asegúrese de haber hecho copia de seguridad de los datos actuales antes de restaurar
- **No se puede deshacer**: Después de la restauración no se puede deshacer

