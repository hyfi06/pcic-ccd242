# Calculo secuencial vs concurrente con candados

## Compilación

```bash
javac -d bin src/Concurrent.java
javac -d bin src/Serial.java
```

## Ejecución

```bash
java -cp bin Concurrent # 8 hilos 1000 trabajos
java -cp bin Concurrent 10 # 10 hilos 1000 trabajos
java -cp bin Concurrent 2 10000 # 2 hilos 10000 trabajos
```
```bash
java -cp bin Serial # 1000 trabajos
java -cp bin Serial 10000 # 10000 trabajos
```
