# Recetas

## 1. Propósito

El módulo **Recetas** permite guardar **recetas de cocina** (nombre, ingredientes, elaboración), tipos de **proteína**, **valoración con estrellas** y organizar platos en **colecciones**. Los datos se comparten con **Planificación de menús** al asignar platos a cada comida de la semana.

## 2. Cuándo usarlo

- Quieres un cuaderno personal de recetas.
- Quieres agrupar platos por tema con **colecciones**.
- Vas a usar **Planificación de menús** — necesitas al menos algunos platos guardados.

## 3. Pantallas relacionadas

- **Funciones** → **Cocina y gastronomía** → **Recetas**
- Pestañas **Recetas** / **Colecciones**
- **Añadir receta** / **Editar receta**
- **Detalle de colección**

## 4. Uso principal

### 4.1 Lista y búsqueda

**Funciones** → **Recetas** → buscar con **Buscar recetas...**; pestaña **Colecciones** con búsqueda propia.

### 4.2 Nueva receta

**+** (FAB) → **Nombre del plato** (obligatorio), **Tipos de proteína** (opcional, separados por comas), **Valoración**, **Ingredientes** (al menos uno con nombre), **Elaboración**, **Colecciones** → **Guardar**.

### 4.3 Editar / eliminar

Toca un plato; **Guardar**. **Eliminar** con aviso si el plato está en un **plan de comidas**.

### 4.4 Colecciones

Pestaña **Colecciones** → **Crear colección**; abrir colección → **Añadir recetas**; **Renombrar** / **Eliminar** (no borra las recetas).

## 5. Ejemplos y bocetos

### 5.1 RECIPE-01

**Objetivo**: Guardar “Sopa tom yum” en la colección “Tailandés”.

```text
[ Recetas ]  [ Colecciones ]
[ Buscar recetas...________________________ ]

┌────────────────────────────────────────────┐
│ Sopa tom yum                       [ x ]  │
│ ★★★★☆  ·  Proteína: Marisco               │
│ 5 ingredientes  ·  Colección: Tailandés  │
└────────────────────────────────────────────┘
                                             [ + ]
```

### 5.2 RECIPE-02: Buscar “sopa”

```text
[ Buscar...  sopa__________________________ ]
```

## 6. Lógica y reglas

- **Al menos un ingrediente** obligatorio.
- Eliminar plato usado en el plan: confirmación; se quita del plan.
- **Colecciones**: un plato puede estar en varias.

## 7. Notas importantes

- **Premium**: puede mostrarse en **Funciones**.
- Guía para usuario final, sin rutas técnicas.
