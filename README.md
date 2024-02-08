# Problema

### Prueba Backend
El objetivo de esta prueba es validar las capacidades en Python - Django y API REST del candidato. La prueba consiste en crear un servicio Django el cual publique una API REST en http://localhost:8000 que cumpla con los siguientes requisitos:

### Modelo ChargePoint
- id > Number
- name > String (Máximo 32 caracteres, único)
- status > String (Pudiendo ser sólo [ready, charging, waiting, error])
- created_at > Datetime
- deleted_at > Datetime

### API (endpoints)
- POST /chargepoint > Crea un nuevo cargador
- GET /chargepoint > Listado de cargadores
- GET /chargepoint/:id > Datos del cargador
- DELETE /chargepoint/:id > Elimina un cargador (campo deleted_at)
- PUT /chargepoint/:id > Modifica (Útil para modificar el campo status)

El formato de datos de la API deberá ser JSON. Tener en cuenta los cargadores eliminados en las operaciones que se consideren oportunas.

### Persistencia de datos
Podéis utilizar cualquiera de las siguientes opciones: 
- Relacionales > MariaDB o PostgreSQL
- No relacionales > MongoDB o Redis

El resto está totalmente abierto y bajo vuestro criterio. Se pueden utilizar otras librerías o cualquier herramienta que os facilite el desarrollo.

### Bonus

Como bonus, y sin que sea un requisito para esta prueba, os animamos a desarrollar una segunda parte del proyecto que consistiría en publicar un servicio websocket con Django Channels el cual notifique de todos los cambios de estado de cualquier cargador. 
Por ejemplo, cuando un cargador cambia el estado de ‘ready’ -> ‘charging’, cualquiera que esté suscrito al websocket deberá recibir una notificación indicando el nuevo estado y en que cargador se ha producido.

### Valoración

Se valorará la estructura del proyecto, el código (reutilización, legibilidad, etc) y las herramientas utilizadas pensando que en un futuro el proyecto pueda crecer en modelos y endpoints.

# Solución

Está en el archivo [charge_documentacion.pdf](https://github.com/m4ty4s28/Cargador-coche-electrico/blob/main/charge_documentacion.pdf)
