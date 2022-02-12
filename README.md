Práctica curso Programacion para IA
===================================

Partiendo del código disponible en `05_RPS_More_AI.py`, añada la funcionalidad necesaria para
ofrecer la variante lagarto, Spock del juego piedra, papel o tijeras.

[Práctica curso Programacion para IA](#práctica-curso-programacion-para-ia)
  - [Solución](#solución)
  - [Refactorizaciones](#refactorizaciones)
  - [Testing](#testing)


## Solución

Solución propuesta en [`RPS_spock_lizard.py`](.src/../src/RPS_spock_lizard.py)

## Refactorizaciones

Es necesario refactorizar la función `assess_game()` para conseguir una solución abierta a la extensión y cerrada a la modificación, o principio Open/Closed (OCP) de SOLID.

La inclusión de nuevas categorías en el juego original produce una extensión de la estructura `if-elif-else` que deriva en código cableado, o cierto [input kludge antipattern](https://sourcemaking.com/antipatterns/input-kludge).

Podría haber optado por eliminar la cláusula `if-elif-else` implementando polimorfismo de clase, pero he optado por expresar en el diccionario `Victories` -que ya estaba implementado en el código inicial- las reglas de la lógica del juego de manera declarativa, para mejorar la legibilidad del código. 

No es una solución 100% OCP puesto que si las categorías del juego aumentan no sería viable extender el diccionario, pero confiemos en que la serie _Big Bang Theory_ no goce de una continuación y aumenten el juego con nuevas acciones ;) 

Para ello, he extendido el comportamiento del tipo enumerado `GameAction` implementando lógica de conjuntos (tipo `set` de Python).

Por este motivo, he tenido que refactorizar la función `get_random_computer_action()` para pasar los conjuntos de Python a una estructura accesible por posición (una lista).

## Testing

En todo proceso de refactorización de código es necesario incluir un conunto de casos test en aquellos comportamientos más susceptibles de presentar defectos.

Aunque no he practicado TDD estricta (que es como suelo codificar), he incluído casos test para eliminar defectos del código cuando he estimado que la lógica estaba completada.

