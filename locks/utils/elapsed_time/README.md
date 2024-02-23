# Código para Medición y Formateo de Tiempo

Proporciona un conjunto de funciones para medir y formatear intervalos de tiempo, calcular el tiempo transcurrido en diferentes unidades, e imprimir estos valores de manera legible. Además, incluye una función para crear un temporizador sencillo.

## Tipos de Datos Alias

- `Days`: Representa días como un entero (`int`).
- `Hours`: Representa horas como un entero (`int`).
- `Minutes`: Representa minutos como un entero (`int`).
- `Seconds`: Representa segundos como un número flotante (`float`).

Estos alias de tipos ayudan a mejorar la legibilidad del código y aclarar el tipo de datos que se espera para días, horas, minutos y segundos.

### Funciones

#### `elapsed_time(start: float, end: float) -> Tuple[Days, Hours, Minutes, Seconds]`

**Descripción:**  
Calcula el tiempo transcurrido entre dos marcas de tiempo (en segundos) y lo desglosa en días, horas, minutos y segundos.

**Parámetros:**

- `start (float)`: Marca de tiempo inicial.
- `end (float)`: Marca de tiempo final.

**Retorno:**  
Una tupla que contiene el tiempo transcurrido desglosado en días, horas, minutos y segundos.

---

#### `milis(start: float, end: float) -> float`

**Descripción:**  
Calcula el tiempo transcurrido entre dos marcas de tiempo (en segundos) y lo convierte a milisegundos.

**Parámetros:**

- `start (float)`: Marca de tiempo inicial.
- `end (float)`: Marca de tiempo final.

**Retorno:**  
El tiempo transcurrido en milisegundos.

---

#### `print_elapsed_time(start: float, end: float) -> None`

**Descripción:**  
Imprime el tiempo transcurrido entre dos marcas de tiempo en un formato legible: días, horas, minutos y segundos.

**Parámetros:**

- `start (float)`: Marca de tiempo inicial.
- `end (float)`: Marca de tiempo final.

---

#### `print_time(time_to_print: Optional[float] = None) -> float`

**Descripción:**  
Imprime la fecha y hora actual, o la proporcionada en formato de marca de tiempo UNIX, y devuelve el tiempo impreso como una marca de tiempo UNIX.

**Parámetros:**

- `time_to_print (Optional[float])`: Marca de tiempo UNIX opcional a imprimir. Si no se proporciona, se usa la fecha y hora actuales.

**Retorno:**  
La marca de tiempo UNIX impresa.

---

#### `timer(minutes: int) -> Callable[[], bool]`

**Descripción:**  
Crea y devuelve una función (`still_time`) que, cuando se llama, indica si aún queda tiempo basado en el intervalo de minutos especificado desde su creación.

**Parámetros:**

- `minutes (int)`: Número de minutos para el temporizador.

**Retorno:**  
Una función que devuelve `True` si aún queda tiempo y `False` si el tiempo se ha agotado.

**Uso de la Función Retornada (`still_time`):**

- **Retorno (`bool`):** `True` si aún no ha pasado el tiempo especificado desde la creación del temporizador; `False` en caso contrario.

### Ejemplos de Uso

```python
start_time = time.time()
# Simular una tarea con sleep
time.sleep(5)
end_time = time.time()

print_elapsed_time(start_time, end_time)

current_time_stamp = print_time()
print(f"Current timestamp: {current_time_stamp}")

timer_func = timer(1)  # Temporizador de 1 minuto
while timer_func():
    print("Aún hay tiempo.")
    time.sleep(10)  # Espera de 10 segundos para la próxima comprobación
```

### Notas Adicionales

- La función `timer` es especialmente útil para operaciones que deben realizarse dentro de un período de tiempo limitado, proporcionando una forma sencilla de comprobar si el tiempo límite se ha alcanzado.
- Estas herramientas son aplicables en una variedad de contextos, como temporizadores para juegos, limitadores de tiempo para ejecución de tareas, o simplemente para medir y formatear intervalos de tiempo en aplicaciones.
