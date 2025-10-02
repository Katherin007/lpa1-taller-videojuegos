# Taller Videojuegos

![commits](https://badgen.net/github/commits/UR-CC/lpa1-taller-videojuegos?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/UR-CC/lpa1-taller-videojuegos)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor

- [@estudiante](https://www.github.com/estudiante)

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un videojuego básico utilizando los principios de la **Programación Orientada a Objetos** (POO). Los estudiantes crearán un mundo de juego interactivo donde los jugadores pueden controlar un personaje, explorar escenarios, interactuar con objetos y enemigos, y progresar a través de la historia. El juego se diseñará para enfatizar los conceptos de **POO**, como clases, objetos, herencia, polimorfismo y encapsulamiento. A través de este proyecto, los estudiantes aplicarán sus conocimientos de POO para construir un sistema modular y extensible, sentando las bases para proyectos de software más complejos en el futuro.

El proyecto se dividirá en varias fases, comenzando con la creación de clases para personajes, enemigos y objetos, y luego avanzando hacia la implementación de la lógica del juego, el sistema de combate y la interfaz de usuario básica. Se fomentará el uso de buenas prácticas de programación, como la documentación del código, el control de versiones con Git. Al finalizar el proyecto, los estudiantes habrán ganado experiencia práctica en el diseño y desarrollo de software orientado a objetos, así como en la resolución de problemas y el trabajo en equipo.

#### Objetivos del Proyecto

1.  Aplicar los principios de la programación orientada a objetos (POO), demostrando su capacidad para diseñar e implementar clases, objetos, herencia, polimorfismo y encapsulamiento en el contexto del desarrollo de un videojuego.
2.  Desarrollar un sistema modular y extensible, de manera que sea fácil de modificar y expandir, permitiendo la adición de nuevas funcionalidades y contenido en el futuro.
3.  Implementar la lógica del juego y el sistema de combate funcional y equilibrado, así como la lógica para la interacción con objetos y enemigos en el mundo del juego.
4.  Crear una interfaz de usuario básica que permita al jugador interactuar con el mundo del juego y visualizar la información relevante (puntos de vida, inventario, etc.).
5.  Practicar buenas prácticas de programación como el control de versiones (Git), documentar su código.

## Requerimientos

* **R1.1. Creación de Personaje Jugable**: El sistema debe permitir la creación de un personaje jugable con los siguientes atributos: Puntos de vida, Ataque, Defensa, Nivel, Inventario.

* **R1.2. Creación de Enemigos**: El sistema debe permitir la creación de enemigos con los siguientes atributos: Puntos de vida, Ataque, Defensa, Tipo ("volador", "terrestre").

* **R2.1. Creación de Trampas Explosivas**: El sistema debe permitir la creación de trampas explosivas con atributos de: Alcance de explosión, Daño por explosión.

* **R2.2. Creación de Tesoros**: El sistema debe permitir la creación de tesoros con un atributo de: Valor monetario.

* **R2.3. Creación de Armamento/Defensa**: El sistema debe permitir la creación de objetos de armamento y defensa con atributos de: Aumento de ataque/defensa, Precio de compra/venta.

* **R3.1. Interacción de Combate**: El personaje debe poder atacar y defenderse de los enemigos.

* **R3.2. Recolección de Objetos**: El personaje debe poder recolectar trampas explosivas y tesoros.

* **R3.3. Interacción con Armamento/Defensa**: El personaje debe poder comprar, usar y vender objetos de armamento y defensa.

* **R3.4. Interacción con el Entorno**: El personaje debe poder recolectar objetos y esquivar obstáculos dentro del escenario.

* **R4.1. Generación del Escenario**: El sistema debe generar un escenario desconocido con diferentes áreas explorables.

* **R4.2. Distribución de Elementos**: El sistema debe ubicar aleatoriamente enemigos y objetos dentro del escenario.

* **R4.3. Zonas de Venta**: El sistema debe incluir zonas de venta donde el personaje pueda comprar armamento y mejoras.

* **R5.1. Mecánica de Combate**: El sistema debe implementar un sistema de combate que permita el ataque y la defensa entre el personaje y los enemigos.

* **R5.2. Cálculo de Daño**: El sistema debe calcular el daño infligido en base a los atributos de ataque, defensa y puntos de vida.

* **R5.3. Efectos Especiales**: El sistema debe generar efectos especiales basados en el tipo de ataque y la interacción entre objetos (ej: explosión de trampas).

* **R6.1. Sistema de Experiencia y Nivel**: El personaje debe ganar experiencia al derrotar enemigos y recolectar objetos valiosos, lo que lleva al aumento de nivel.

* **R6.2. Mejora de Atributos**: El sistema debe permitir la mejora de los atributos del personaje (puntos de vida, ataque, defensa) al subir de nivel.

* **R6.3. Acceso a Nuevo Equipamiento**: El sistema debe permitir el acceso a nuevo armamento y defensas a medida que el personaje avanza de nivel.

* **R7.1. Victoria por Exploración**: El juego debe tener una condición de victoria al completar la exploración del mapa del juego.

* **R7.2. Victoria por Combate Final**: El juego debe tener una condición de victoria al derrotar a un jefe final.

* **R7.3. Victoria por Puntaje:**: El juego debe tener una condición de victoria al alcanzar un puntaje determinado.

* **R8.1. Interfaz de Usuario (UI)**: sistema debe proporcionar una interfaz de usuario intuitiva y fácil de usar que muestre información relevante al jugador (puntos de vida, inventario, nivel, etc.).

* **R8.2. Retroalimentación del Jugador**: El sistema debe proporcionar retroalimentación visual y auditiva clara para las acciones del jugador (ej: daño recibido, recolección de objetos, etc.).

#### Opcionales

* **O1. Niveles de Dificultad**: El juego debe permitir la selección de diferentes niveles de dificultad, que afecten a los atributos de los enemigos, la cantidad de objetos y la complejidad del escenario.

* **O2. Gráficos**: El sistema debe utilizar gráficos de alta calidad que sean consistentes con el estilo visual del juego.

* **O3. Efectos de Sonido**: El sistema debe incluir efectos de sonido para las acciones del jugador, los enemigos y el entorno.

* **O4. Sistema de Logros/Desafíos**: El sistema debe incluir un sistema de logros o desafíos para recompensar al jugador por completar tareas específicas.

* **O5. Música de Fondo**: El sistema debe incluir música de fondo que se adapte al ambiente y la acción del juego.

* **O6. Tutorial**: El sistema debe incluir un tutorial interactivo para enseñar a los nuevos jugadores las mecánicas básicas del juego.

* **O7. Ayuda**: El sistema debe proporcionar un sistema de ayuda contextual que explique las funcionalidades y objetos del juego.

* **O8. Sistema de Personalización**: El sistema debe permitir la personalización del personaje, ya sea cambio de vestimenta, o de armas.

* **O9. Multijugador**: Incluir opciones multijugador, se deben definir los modos de juego, la cantidad de jugadores y la comunicación entre ellos.

#### Glosario

- Puntos de vida: Representa la resistencia del personaje/enemigo al daño.
- Ataque: Define el poder de ataque del personaje/enemigo.
- Defensa: Representa la capacidad del personaje/enemigo para resistir el daño.
- Nivel: Indica el progreso del personaje y habilita nuevas habilidades.
- Inventario: Almacena los objetos que el personaje recolecta.
- Tipo: Puede variar según el comportamiento o habilidades del enemigo (ej: volador, terrestre, etc.).
- Trampas explosivas: Deben tener diferentes alcances y efectos negativos sobre el personaje.
- Tesoros: Deben tener diferentes objetos valiosos que se traduzcan en dinero para el personaje al venderlos.
- Armamento/Defensa: El personaje debe poder comprar/vender para mejorar su ataque/defensa.

## Diseño

![Diagrama de Clases](./docs/diagramas.png)

## Instalación

1. Clonar el proyecto

```bash
git clone https://github.com/UR-CC/lpa1-taller-videojuegos.git
cd lpa1-taller-videojuegos
```

2. Crear y activar entorno virtual

```bash
python -m venv venv
venv/bin/activate
```

3. Instalar librerías y dependencias

```bash
pip install -r requirements.txt
```
    
## Ejecución

1. Ejecutar el proyecto

```bash
cd lpa1-taller-videojuegos
python main.py
```
# Juego de Evasión y Disparo

Un juego 2D desarrollado en Python usando PyGame que demuestra principios de **Programación Orientada a Objetos** y **desarrollo de videojuegos**. El jugador controla una bola verde que debe evitar a un enemigo rojo mientras dispara proyectiles para ganar puntos.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyGame](https://img.shields.io/badge/PyGame-2.0+-green.svg)

## Características del Juego

- **Control intuitivo**: Mueve la bola verde con el mouse
- **Sistema de disparo**: Haz clic izquierdo para disparar proyectiles amarillos, en la dirección que se mueve la bola verde
- **IA enemiga**: El enemigo rojo persigue al jugador de manera inteligente (usa la ubicación)
- **Sistema de puntos**: Pierde puntos al tocar al enemigo, gana puntos al dispararle
- **Mecánicas avanzadas**: 

  - Cooldown de disparos
  - Sistema de vida del enemigo
  - Invulnerabilidad temporal tras recibir daño
  - Respawn automático del enemigo

## Arquitectura del Proyecto

El proyecto está diseñado siguiendo principios de **Programación Orientada a Objetos** y **patrones de diseño**:

### Estructura de Clases

```
├── Vector2D          # Manejo matemático de vectores 2D
├── Figura            # Clase base abstracta para entidades
│   ├── Proyectil     # Munición disparada por el jugador
│   ├── Jugador       # Entidad controlada por el usuario
│   └── Enemigo       # IA que persigue al jugador
└── ControlJuego      # Controlador principal del juego
```

- Ver el [Diagrama de Clases](refs/diagrama.md) para más detalles.

### Principios de Diseño Aplicados

- **Herencia**: Todas las entidades del juego heredan de `Figura`
- **Encapsulación**: Cada clase maneja sus propias responsabilidades
- **Polimorfismo**: Método `actualizar()` implementado específicamente en cada clase
- **Composición**: `ControlJuego` contiene y coordina todas las entidades
- **Separación de responsabilidades**: Lógica separada por funcionalidad

Este proyecto es ideal para aprender:

- **Programación Orientada a Objetos** en Python
- **Desarrollo de videojuegos** con [PyGame](https://www.pygame.org/docs/)
- **Patrones de diseño** en software
- **Matemáticas** aplicadas a juegos (vectores, colisiones)
- **Testing** con [pytest](https://docs.pytest.org/en/stable/)

## Instalación y Ejecución

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/clubdecomputacion/evadir-disparar.git
cd evadir-disparar

# Crear/Activar entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install pygame
```

### Ejecución

```bash
# Ejecutar el juego
python main.py
```

## Controles del Juego

| Acción | Control |
|--------|---------|
| Mover jugador | Mouse |
| Disparar | Click izquierdo |
| Salir | Cerrar ventana o Esc |

## Objetivos del Juego

1. **Evitar al enemigo**: No dejes que la bola roja te toque
2. **Disparar al enemigo**: Usa proyectiles para reducir su vida
3. **Ganar puntos**: Cada golpe al enemigo te da +2 puntos
4. **Sobrevivir**: Si tus puntos llegan a 0 **¡Game Over!**

## Configuración del Juego

### Parámetros Modificables

En el código puedes ajustar:

```python
# Configuración de pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Configuración del jugador
VELOCIDAD_JUGADOR = 0.1
COOLDOWN_DISPARO = 0.3  # segundos

# Configuración del enemigo
VELOCIDAD_ENEMIGO = 50  # píxeles/segundo
VIDA_ENEMIGO = 3

# Configuración de proyectiles
VELOCIDAD_PROYECTIL = 300
TIEMPO_VIDA_PROYECTIL = 2.0  # segundos
```

## Fases del Game Loop:

[Game Loop](refs/gameloop.md)

### 1. Fase de Inicialización

- Configuración inicial de PyGame
- Creación del GameManager
- Inicialización de objetos del juego

### 2. Fase de _Input_

- Manejo de eventos de PyGame
- Detección de clicks del mouse
- Control de salida del juego

### 3. Fase de _Update_

- Cálculo de delta time para movimiento consistente
- Actualización del jugador (movimiento suave hacia mouse)
- Gestión de proyectiles (movimiento, limpieza)
- IA del enemigo (persecución inteligente)
- Sistema de respawn

### 4. Fase de _Colisiones_

- Detección proyectil vs enemigo
- Sistema de daño e invulnerabilidad
- Detección jugador vs enemigo
- Actualización de puntuación

### 5. Fase de _Render_

- Limpieza de pantalla
- Renderizado condicional (juego activo vs game over)
- Actualización de display

**Características Destacadas**:

- **Delta Time**: Movimiento independiente de FPS
- **Cooldowns**: Sistemas para limitar disparos y daño continuo
- **Estados**: Manejo de entidades activas/inactivas  
- **IA Básica**: Persecución inteligente del enemigo
- **Gestión de Memoria**: Limpieza automática de proyectiles
- **Game Over**: Transición suave al final del juego

## Estructura de Archivos

```
evadir-disparar/
├── .gitignore              # Archivos a ignorar en git
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
├── main.py                 # Código principal del juego
├── juego/
│   ├── __init__.py
│   ├── control_juego.py    # Controlador principal del juego
│   ├── vector2d.py         # Manejo matemático de vectores 2D
│   ├── figura.py           # Clase base abstracta para entidades
│   ├── jugador.py          # Entidad controlada por el usuario
│   ├── proyectil.py        # Munición disparada por el jugador
│   └── enemigo.py          # IA que persigue al jugador
├── docs/                   # Documentación Técnica
└── refs/                   # Documentación adicional
    ├── diagrama.md         # Diagrama de Clases (mermaid)
    ├── diagrama.pdf
    └── gameloop.md         # Lógica de un juego
```

## Extensiones Futuras

### Funcionalidades Planeadas
- [ ] **Power-ups**: Mejoras temporales para el jugador
- [ ] **Múltiples niveles**: Dificultad progresiva
- [ ] **Diferentes tipos de enemigos**: Con comportamientos únicos
- [ ] **Sistema de puntuación**: High scores y persistencia
- [ ] **Efectos de sonido**: Audio feedback
- [ ] **Partículas**: Efectos visuales al disparar/colisionar
- [ ] **Menú principal**: Interfaz de inicio

### Mejoras Técnicas
- [ ] **Sistema de entidades-componentes**: Arquitectura más flexible
- [ ] **Pool de objetos**: Optimización de memoria para proyectiles
- [ ] **Sistema de eventos**: Comunicación desacoplada entre objetos
- [ ] **Configuración externa**: Archivos JSON para parámetros
- [ ] **Sprites**: Reemplazar formas geométricas con imágenes


