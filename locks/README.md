# Sistema de Dispensación de Tickets

## Clases
Se define dos clases para dispensar tickets: `TicketDispenserConcurrent` para entornos concurrentes usando hilos, y `TicketDispenserSerial` para entornos seriales. Ambas clases proporcionan un mecanismo para generar números de ticket de manera secuencial.

### Clase `TicketDispenserConcurrent`

**Descripción:**  
Clase diseñada para ser utilizada en entornos donde múltiples hilos pueden solicitar tickets de manera concurrente. Asegura la operación segura en concurrencia mediante el uso de un candado (`threading.Lock`).

**Métodos:**

- `__init__(self) -> None`  
  **Constructor de la clase.**  
  Inicializa la clase con un número de ticket inicial de 0 y crea un `Lock` para controlar el acceso concurrente al número de ticket.

- `get_ticket(self) -> int`  
  **Devuelve el próximo número de ticket disponible.**  
  Asegura la exclusión mutua en el incremento y devolución del número de ticket usando un bloque `try-finally` para adquirir y liberar el `Lock`, respectivamente. Esto previene condiciones de carrera entre hilos.

### Clase `TicketDispenserSerial`

**Descripción:**  
Clase diseñada para ser utilizada en entornos seriales donde los tickets son solicitados secuencialmente por un único hilo de ejecución. No utiliza mecanismos de sincronización ya que se asume que no hay acceso concurrente.

**Métodos:**

- `__init__(self) -> None`  
  **Constructor de la clase.**  
  Inicializa la clase con un número de ticket inicial de 0. No se requiere sincronización dado el contexto de ejecución serial.

- `get_ticket(self) -> int`  
  **Devuelve el próximo número de ticket disponible.**  
  Incrementa y devuelve el número de ticket sin mecanismos de sincronización adicionales, asumiendo que no hay acceso concurrente.

### Uso Recomendado

- **`TicketDispenserConcurrent`:** Utilice esta clase en aplicaciones donde múltiples hilos necesiten obtener números de ticket de forma segura y concurrente, como en aplicaciones web o sistemas de procesamiento paralelo.

- **`TicketDispenserSerial`:** Esta clase es adecuada para scripts o aplicaciones seriales donde la generación de tickets ocurre en un único hilo de ejecución, eliminando la necesidad de sincronización entre hilos.

### Ejemplo de Uso

```python
# Para entornos concurrentes
dispenser_concurrent = TicketDispenserConcurrent()
# En diferentes hilos, solicitar un ticket
ticket = dispenser_concurrent.get_ticket()

# Para entornos seriales
dispenser_serial = TicketDispenserSerial()
# Solicitar un ticket
ticket = dispenser_serial.get_ticket()
```

### Notas Adicionales

- La correcta elección entre `TicketDispenserConcurrent` y `TicketDispenserSerial` depende del entorno de ejecución específico y si se espera o no acceso concurrente al dispensador de tickets.
- La implementación de `TicketDispenserConcurrent` garantiza la seguridad de la operación en entornos de multihilo mediante el uso explícito de `Lock.acquire()` y `Lock.release()`. Alternativamente, se podría utilizar la declaración `with self.lock:` para un código más limpio y pythonico, lo que automáticamente adquiere y libera el candado, simplificando el manejo de excepciones y la liberación del recurso.
