# Calculo secuencial vs concurrente con candados

## Compilación

```bash
javac -d bin src/Main.java
```

## Ejecución

```bash
java -cp bin Main # 8 hilos 1000 trabajos
java -cp bin Main 10 # 10 hilos 1000 trabajos
java -cp bin Main 2 10000 # 2 hilos 10000 trabajos
```
