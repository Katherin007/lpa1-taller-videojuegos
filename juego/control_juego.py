import random
import pygame
from typing import Optional, List

from .figura import Figura
from .jugador import Jugador
from .enemigo import Enemigo
from .proyectil import Proyectil

class ControlJuego:
    """
    Gestiona el estado general del juego, coordinando todos los elementos.

    Se encarga de la inicialización, actualización, renderizado y gestión de
    eventos del juego. También maneja la lógica de colisiones, sistema de puntos
    y transiciones de estado (juego activo/game over).

    Attributes
    ----------
    pantalla : pygame.Surface
        Superficie principal donde se renderiza el juego
    puntos : int
        Puntuación actual del jugador
    jugador : Optional[Jugador]
        Instancia del jugador (None hasta inicialización)
    enemigo : Optional[Enemigo]
        Instancia del enemigo (None hasta inicialización)
    fuente : pygame.font.Font
        Fuente para renderizar texto de la interfaz
    clock : pygame.time.Clock
        Reloj para controlar la tasa de refresco del juego
    jugando : bool
        Estado que indica si el juego está en curso
    tiempo_desde_ultimo_dano : float
        Tiempo transcurrido desde el último daño recibido por el jugador
    cooldown_dano : float
        Tiempo mínimo entre daños que puede recibir el jugador

    Examples
    --------
    >>> pantalla = pygame.display.set_mode((800, 600))
    >>> game_manager = ControlJuego(pantalla)
    >>> game_manager.ejecutar()  # Inicia el bucle principal del juego
    """

    def __init__(self, pantalla: pygame.Surface):
        """
        Inicializa el gestor del juego con la superficie de renderizado.

        Parameters
        ----------
        pantalla : pygame.Surface
            Superficie de pygame donde se renderizará el juego

        Raises
        ------
        TypeError
            Si pantalla no es una instancia de pygame.Surface
        """
        if not isinstance(pantalla, pygame.Surface):
            raise TypeError("pantalla debe ser una instancia de pygame.Surface")

        self.pantalla = pantalla
        self.puntos = 10
        self.jugador: Optional[Jugador] = None
        self.enemigos: List[Enemigo] = []
        self.enemigo: Optional[Enemigo] = None
        self.tiempo_enemigo = 0.0     # Acumulador de tiempo para nuevos enemigos
        self.intervalo_enemigo = 5.0  # Cada 5 segundos
        self.MAX_ENEMIGOS = 10  # 👈 Límite máximo
        self.tiempo_ultimo_enemigo = pygame.time.get_ticks()
        self.intervalo_creacion = 2000 # Intervalo de 2 segundos (en milisegundos)
        # Sistema de fuentes para la interfaz de usuario
        self.fuente = pygame.font.Font(None, 36)  # Fuente por defecto, tamaño 36
        self.fuente_pequena = pygame.font.Font(None, 24)  # Fuente para instrucciones
        
        self.clock = pygame.time.Clock()
        self.jugando = True
        self.tiempo_desde_ultimo_dano = 0.0
        self.cooldown_dano = 1.0  # 1 segundo de cooldown para recibir daño

        # Inicializar el estado del juego
        self.inicializar_juego()

    def inicializar_juego(self) -> None:
        """
        Configura los objetos iniciales del juego.

        Crea al jugador y al enemigo en posiciones estratégicas y establece
        las relaciones entre ellos (el enemigo persigue al jugador).

        Notes
        -----
        El jugador se coloca en la parte izquierda de la pantalla y el enemigo
        en la parte superior central para un gameplay balanceado.
        """
        width = self.pantalla.get_width()
        height = self.pantalla.get_height()

        # Crear jugador (verde) en la parte izquierda de la pantalla
        self.jugador = Jugador(self.pantalla, width // 4, height // 2, (0, 255, 0))
        
        # Crear enemigo (rojo) en la parte superior central
        enemigo_inicial = Enemigo(self.pantalla, width // 2, height // 4, (255, 0, 0))
        enemigo_inicial.establecer_objetivo(self.jugador)
        self.enemigos.append(enemigo_inicial)
        self.enemigo = enemigo_inicial

    def manejar_eventos(self) -> None:
        """
        Procesa todos los eventos de pygame en el frame actual.

        Gestiona eventos del sistema (como QUIT) y eventos de entrada del usuario
        (como clics del mouse para disparar).

        Notes
        -----
        Solo el clic izquierdo del mouse está configurado para disparar.
        El evento QUIT cambia el estado del juego para terminar el bucle principal.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.jugando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.jugador: # Clic izquierdo
                    self.jugador.disparar(event.pos)

    def actualizar(self, dt: float) -> None:
        """
        Actualiza la lógica del juego en cada frame.

        Realiza las siguientes operaciones:
        1. Actualiza cooldowns globales
        2. Actualiza estado de jugador y enemigo
        3. Verifica colisiones proyectil-enemigo
        4. Verifica colisiones jugador-enemigo
        5. Gestiona respawn del enemigo
        6. Verifica condiciones de fin del juego

        Parameters
        ----------
        dt : float
            Tiempo transcurrido desde la última actualización en segundos

        Raises
        ------
        ValueError
            Si dt no es un valor positivo
        """
        if dt <= 0:
            raise ValueError("dt debe ser un valor positivo")

        if not self.jugando:
            return

        # 1. Actualizar cooldown de daño al jugador
        self.tiempo_desde_ultimo_dano += dt

        # 2. Actualizar objetos del juego
        for enemigo in self.enemigos:
            if enemigo.activo:
               enemigo.actualizar(dt)

        # 3. Verificar colisiones entre proyectiles y enemigo
        self._verificar_colisiones_proyectiles()
        

        # 4. Verificar colisión entre jugador y enemigo
        self._verificar_colision_jugador_enemigo()
        

        # 5. Respawnear enemigo si fue destruido
        if self.enemigo and not self.enemigo.activo:
            self.respawnear_enemigo()

        # 6. Verificar fin del juego (puntos agotados)
        if self.puntos <= 0:
            self.jugando = False
            self.puntos = 0  # Asegurar que no sea negativo
            
        # Eliminar enemigos inactivos (opcional)
        self.enemigos = [e for e in self.enemigos if e.activo]
        if self.enemigos:
            self.enemigo = self.enemigos[-1]
        else:
            self.enemigo = None

        self.tiempo_enemigo += dt
        if self.tiempo_enemigo >= self.intervalo_enemigo:
            self.respawnear_enemigo()
            self.tiempo_enemigo = 0.0
            
    def dibujar_texto(self, superficie, texto, tamano, x, y):
        # Configuración básica de la fuente
        try:
            # Intentar cargar una fuente del sistema (ejemplo)
            fuente = pygame.font.SysFont('Arial', tamano, bold=True)
        except:
            # Usar la fuente por defecto si la del sistema falla
            fuente = pygame.font.Font(None, tamano) 
            
        text_surface = fuente.render(texto, True, (255, 255, 255)) # Color blanco
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        superficie.blit(text_surface, text_rect)

    def dibujar_interfaz(self, pantalla):
        # 1. Obtener el número actual de enemigos (POO: Usando el tamaño del grupo)
        num_enemigos = len(self.enemigos)
        
        # 2. Formatear el texto
        mensaje = f"Enemigos: {num_enemigos} / {self.MAX_ENEMIGOS}"
        
        # 3. Dibujar en la esquina superior
        self.dibujar_texto(pantalla, mensaje, 24, 10, 10)
        

            

    def _verificar_colisiones_proyectiles(self) -> None:
        """
        Verifica colisiones entre los proyectiles del jugador y el enemigo.

        Si un proyectil colisiona con el enemigo, le aplica daño y desactiva el proyectil.
        El jugador recibe puntos por cada golpe exitoso.

        Notes
        -----
        Se itera sobre una copia de la lista de proyectiles para evitar problemas
        al modificar la lista durante la iteración.
        """
        for proyectil in self.jugador.proyectiles[:]:  # Copia para iteración segura
            if proyectil.colision(self.enemigo):
                if self.enemigo.recibir_dano():
                    self.puntos += 2  # Recompensa por golpear al enemigo
                proyectil.activo = False

    def _verificar_colision_jugador_enemigo(self) -> None:
        """
        Verifica colisión entre el jugador y el enemigo y aplica daño si es necesario.

        El jugador recibe daño si colisiona con el enemigo y ha pasado el cooldown
        de daño establecido. Cada colisión reduce un punto.
        """
        if (self.jugador.colision(self.enemigo) and 
            self.tiempo_desde_ultimo_dano >= self.cooldown_dano):
            
            self.puntos -= 2
            self.tiempo_desde_ultimo_dano = 0.0

    def respawnear_enemigo(self) -> None:
        """
        Reaparece el enemigo en una posición aleatoria de la pantalla.

        El nuevo enemigo mantiene la referencia al jugador como objetivo
        y reaparece con todos sus atributos reseteados (vida completa, etc.).

        Notes
        -----
        La posición aleatoria evita que el enemigo aparezca demasiado cerca
        de los bordes de la pantalla (margen de 50 píxeles).
        """
        width = self.pantalla.get_width()
        height = self.pantalla.get_height()
        
        # Generar posición aleatoria con margen de seguridad
        x = random.randint(50, width - 50)
        y = random.randint(50, height - 50)

        self.enemigo = Enemigo(self.pantalla, x, y, (255, 0, 0), radio=random.choice([10,15,20,25,30]))
        self.enemigo.establecer_objetivo(self.jugador)
        self.enemigos.append(self.enemigo)

    def pintar(self) -> None:
        """
        Renderiza todos los elementos del juego en la pantalla.

        Según el estado del juego (activo o game over), muestra diferentes
        elementos: interfaz durante el juego, pantalla de fin cuando termina.

        Notes
        -----
        La pantalla se limpia completamente en cada frame antes de dibujar.
        El orden de renderizado es importante para la superposición de elementos.
        """
        # Limpiar pantalla con color negro
        self.pantalla.fill((0, 0, 0))

        if self.jugando:
            self._pintar_juego_activo()
        else:
            self._pintar_game_over()

        # Actualizar la pantalla completa
        pygame.display.flip()

    def _pintar_juego_activo(self) -> None:
        """
        Renderiza la interfaz del juego cuando está activo.

        Incluye:
        - Jugador y enemigo
        - Proyectiles
        - Información de puntos
        - Instrucciones de control
        """
        # Pintar objetos del juego
        self.jugador.pintar()
        for enemigo in self.enemigos:
            if enemigo.activo:
                enemigo.pintar()

        # Mostrar puntos en la esquina superior izquierda
        texto_puntos = self.fuente.render(f"Puntos: {self.puntos}", True, (255, 255, 255))
        self.pantalla.blit(texto_puntos, (10, 10))

        # Mostrar instrucciones de control
        texto_instrucciones = self.fuente_pequena.render(
            "Mueve con mouse - Clic izquierdo para disparar", True, (200, 200, 200))
        self.pantalla.blit(texto_instrucciones, (10, 50))

    def _pintar_game_over(self) -> None:
        """
        Renderiza la pantalla de fin del juego (Game Over).

        Muestra:
        - Texto "GAME OVER" centrado
        - Puntuación final obtenida
        """
        # Texto principal de Game Over
        texto_game_over = self.fuente.render("GAME OVER", True, (255, 0, 0))
        texto_rect = texto_game_over.get_rect(
            center=(self.pantalla.get_width() // 2, self.pantalla.get_height() // 2))
        self.pantalla.blit(texto_game_over, texto_rect)

        # Puntuación final
        texto_puntos_final = self.fuente.render(
            f"Puntos finales: {self.puntos}", True, (255, 255, 255))
        puntos_rect = texto_puntos_final.get_rect(
            center=(self.pantalla.get_width() // 2, self.pantalla.get_height() // 2 + 40))
        self.pantalla.blit(texto_puntos_final, puntos_rect)
        
    def intentar_crear_enemigo(self):
        # 1. Verificar el límite
        if len(self.enemigos) < self.MAX_ENEMIGOS:
            
            tiempo_actual = pygame.time.get_ticks()
            # 2. Verificar el intervalo de tiempo para no crearlos instantáneamente
            if tiempo_actual - self.tiempo_ultimo_enemigo >= self.intervalo_creacion:
                
                # 3. Variación de comportamiento (Velocidad)
                # POO: La lógica de la velocidad se delega al constructor del Enemigo
                velocidad_aleatoria = random.randint(2, 6) # Velocidad entre 2 y 6
                
                # Ejemplo de coordenadas aleatorias
                x = random.randint(50, self.ancho - 50)
                y = 0 # Empieza arriba de la pantalla

                nuevo_enemigo = Enemigo(x, y, velocidad_aleatoria)
                
                # 4. Añadir al grupo
                self.enemigos.add(nuevo_enemigo)
                
                # Actualizar el tiempo
                self.tiempo_ultimo_enemigo = tiempo_actual

    

    def ejecutar(self) -> None:
        """
        Ejecuta el bucle principal del juego.

        Este método contiene el game loop que se ejecuta continuamente hasta
        que el juego termina. Maneja la temporización, eventos, actualización
        y renderizado en cada frame.

        Notes
        -----
        El juego se ejecuta a aproximadamente 60 FPS.
        Después del game over, espera 3 segundos antes de cerrar la aplicación.
        """
        try:
            while True:
                # Calcular delta time (tiempo transcurrido desde el último frame)
                dt = self.clock.tick(60) / 1000.0  # Convertir milisegundos a segundos

                # Procesar eventos de entrada
                self.manejar_eventos()

                # Actualizar lógica del juego si está activo
                if self.jugando:
                    self.actualizar(dt)

                # Renderizar frame actual
                self.pintar()

                # Salir después del game over
                if not self.jugando:
                    # Esperar 3 segundos en pantalla de game over antes de cerrar
                    pygame.time.wait(3000)
                    break

        except Exception as e:
            print(f"Error durante la ejecución del juego: {e}")
        finally:
            pygame.quit()

    def __repr__(self) -> str:
        """
        Representación oficial del ControlJuego para depuración.

        Returns
        -------
        str
            Cadena que representa el estado actual del juego
        """
        estado = "jugando" if self.jugando else "game over"
        jugador_activo = self.jugador.activo if self.jugador else "no inicializado"
        enemigo_activo = self.enemigo.activo if self.enemigo else "no inicializado"
        
        return (f"ControlJuego(puntos={self.puntos}, estado={estado}, "
                f"jugador={jugador_activo}, enemigo={enemigo_activo})")

    def __str__(self) -> str:
        """
        Representación legible del ControlJuego para usuarios.

        Returns
        -------
        str
            Descripción simplificada del estado del juego
        """
        return f"Juego: {self.puntos} puntos - {'Activo' if self.jugando else 'Game Over'}"
