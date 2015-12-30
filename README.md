## Servicio web de Scopus

### Host
IP del contenedor donde se aloja el servicio

### Métodos

#### Verbo HTTP
GET

#### Ruta
/red

#### Parámetros
- datosJson : json cuyas llaves corresponden a nombres de autores y los valores a listas de eids correspondientes a los papers 

#### Respuesta
Json que contiene la porción del código que reconoce D3 como los nodos y aristas de un grafo, además el json tiene 3 medidas de la red: 
cluster coefficient, average path length y average degree





