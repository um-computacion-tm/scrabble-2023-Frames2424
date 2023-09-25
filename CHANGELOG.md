
### Versión 0.0.1 - 12 de septiembre de 2023
- Inicialización de la primera versión con un historial de cambios.
- Se introdujo un nuevo parámetro en la clase Board, permitiendo recuperar una lista que contiene los valores individuales de cada letra en una palabra escrita.
- Hubo cambios en los nombres de dos funciones de la clase Board, empleando "verificar" para indicar que estas funciones comprueban la existencia de la palabra en la matriz.
- Incorporación de tres funciones adicionales:
  1. `wordCurrentPoints`: Retorna una lista con los valores individuales de las letras en la última palabra escrita en la matriz.
  2. `writeVerticalWord`: Permite escribir verticalmente en la matriz la palabra seleccionada (aún no se ha realizado la verificación, lo cual se planifica en futuras actualizaciones). Esta función calcula el valor de cada casilla y multiplica las letras individuales en caso de caer en una casilla de doble o triple letra.
  3. `writeHorizontalWord`: Posibilita escribir horizontalmente en la matriz la palabra elegida (aún no se ha verificado, lo cual se llevará a cabo en futuras actualizaciones). Esta función también calcula el valor de cada casilla y multiplica las letras individuales si se encuentra en una casilla de doble o triple letra.

### Versión 0.0.2 - 12 de septiembre de 2023
- Se efectuó una modificación en la estructura de los valores de las Tiles; antes se presentaban como una lista y ahora se han reemplazado por un diccionario para facilitar el acceso a sus valores individuales.
- La letra K se incorporó a la bolsa de letras para ampliar las posibles combinaciones.
- Se realizaron ajustes en las pruebas junto con las funciones, eliminando algunas pruebas que ya no se alinean con el enfoque planeado para el desarrollo del juego.

Si necesitas más ajustes o cambios específicos en el texto, por favor, házmelo saber.

### Versión 0.0.3 - 13 de septiembre 2023 
-  Es mi cumpleaños 
## Versión 0.0.3a - 18 de septiembre 2023 
-  Se unificaron y optimizaron funciones de game.

## Versión 0.0.4 - 25 septiembre 2023 
- Es posible calcular el puntaje individual de cada palabra. 