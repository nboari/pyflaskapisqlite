# pyflaskapisqlite
Demo de api hecha en python con flask y sqlite

## Empezando
### Instalando los paquetes necesarios para correr la Api
* Para distribuciones basadas en debian (ej: ubuntu, mint,etc):
```
sudo apt-get update
sudo apt-get install python pip git 
sudo pip install Flask
```
* Para distribuciones basadas en redhat (ej: fedora, centOS,etc):
```
sudo dnf install python pip git 
sudo pip install Flask
```

### Creando la base de datos con sqllite 
* Ingresar desde la terminal al directorio donde se clono el repositorio.
* Crear la base de datos que utilizara la Api desde la consola con el siguiente codigo:
```
sqlite3 gimnasio.db
```
* Dentro del entorno de sqlite ejecutamos el comando para crear la tabla
```
sqlite> create table cliente (
   ...> id int not null primary key,
   ...> dni int not null,
   ...> nombre varchar(25) not null,
   ...> apellido varchar(25) not null);
```
* Validamos que se haya creado correctamente la tabla
```
sqlite> .tables
cliente
```
* Insertamos algunos cliente y hacemos una consulta a la base
```
sqlite> insert into cliente values (1,11111111,"Cliente","Uno");
sqlite> insert into cliente values (2,22222222,"Cliente","Dos");
sqlite> select * from cliente
sqlite> select * from cliente;
1|11111111|Cliente|Uno
2|22222222|Cliente|Dos
```
Para salir del entorno de sqlite 
```
sqlite> .quit
```

## Ejecutando
### Inicializamos el api
En la terminal ejecutar el siguiete comando
```
python cliente.py
```



