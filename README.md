# CoderHouse Django Primera Entre Proyecto Final

## Ampliación del proyecto MVT

### Estructura

**Página principal**

- Cuenta con un header que permite un fácil acceso a las aplicaciones que
  componen el proyecto, a su vez que hay un botón que permite fácilmente volver
  a la página principal con el índice de aplicaciones.

**URLs**

- Cada aplicación sigue una estructura simple, con una url base compuesta por
  el nombre de la aplicación, seguido de una url para la funcionalidad de
  búsqueda.

- Ejemplo: ***localhost:8000/'aplicación'/'app-search'/*** ; donde 'aplicación'
  contiene el índice con los elementos actualmente almacenados en la base de
  datos.

## Aplicaciones

Todas las aplicaciones cuentan con la misma estructura de base:

- Un listado con los elementos almacenados dentro de la base de datos.

- Botones de acceso para formularios de búsqueda en base al nombre de los
  elementos en la BD, y otro botón para crear nuevos elementos y almacenarlos
  en la BD.

Actualmente el proyecto se compone por 3 aplicaciones: **Profesionales** (cuyo
nombre dentro del proyecto es 'family'), **Libros** y **Restaurantes**, todas
con funcionalidades muy similares, siendo las mayores diferencias los tipos de
datos que almacenan los modelos de cada una, aún si no hay demasiada variedad
aún.

- **Profesionales** cuenta con los campos: *name* (CharField), *age* (IntegerField), *birth* (DateField), y *job* (CharField).
- **Libros** cuenta con los campos: *book_title* (CharField), *author*
  (CharField), *genre* (CharField), *published* (IntegerField), y *book_length*
  (IntegerField).
- **Restaurantes** cuenta con los campos: *resto_name* (CharField), *category*
  (CharField), *stars* (IntegerField), y *reservation* (BooleanField).
