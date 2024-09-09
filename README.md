# Personal trainer
This project provides tools for a personal trainer managing multiple people. It automates data collection, reports, analytics and more.


## Steps
1. Input datos
2. Parámetros secundarios
3. Mesociclos
4. Plan de alimentación
5. Plan de ejercicio
7. Seguimiento semanal
8. Seguimiento bisemanal
9. Report final de fase
10. Corregir mesociclos
11. Report final de tratamiento 


## Functionalities:
1. Preguntar datos de input __[gform]__
2. Exportar datos de Input a csv __[pandas]__
3. Generar parámetros secundarios __[python]__
4. Guardar datos a perfil (formato json) __[json]__
5. Generar mesociclos __[python]__
6. Generar plan de ejercicio a partir de json de input __[json]__
7. Generar plan de ejercicio a partir de str __[python]__
8. Preguntar seguimiento semanal __[gform]__
9. Generar seguimiento semanal a partir de input __[pandas]__
10. Preguntar seguimiento bisemanal __[gform]__
11. Generar seguimiento bisemanal a partir de input __[pandas]__
12. Preguntar feedback mesociclo __[gform]__
13. Generar report final de mesociclo __[pandas]__
14. Generar report final de tratamiento __[pandas]__


## Advanced functionalities
- Clasificar cliente a partir de datos de input y parámetros secundarios __[clustering]__
- Autogenerar plan de ejercicio __[cluster -> hausdorff distance]__
- Predecir fases a partir de clasificación __[cluster -> hausdorff distance // modal sequence]__
- Predecir seguimiento semanal a partir de clasificación __[cluster -> hausdorff distance // LSTMs // LLMs]__
- Predecir report final de fase a partir de clasificación __[cluster -> hausdorff distance // LSTMs // LLMs]__
- Predecir report final de tratamiento __[cluster -> hausdorff distance // LSTMs // LLMs]__


