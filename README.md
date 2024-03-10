# Mapas y códigos

## Mapas eurostat
Ficheros comprimidos con datos shp de eurostat para el año 2021 (https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data):
* NUTS_LB_2021_3035.shp.zip: Ficheros de puntos. NUTS 1: major socio-economic regions, NUTS 2: basic regions for the application of regional policies, NUTS 3: small regions for specific diagnoses. Additionally a NUTS 0 level, usually co-incident with national boundaries are also available.  CSR 3035. Resolución 20 metros.
* NUTS_RG_2021_3035.shp.zip: poligonos. NUTS 1: major socio-economic regions, NUTS 2: basic regions for the application of regional policies, NUTS 3: small regions for specific diagnoses. Additionally a NUTS 0 level, usually co-incident with national boundaries are also available. CSR 3035. Resolución 20 metros.
* LAU_RG_01M_2021_3025.shp.zip: poligonos a escala de municipaios de toda la Unión Europea con CRS 3035.

La asignación de provincias no se corresponde con la oficial de españa y no se peude utilziar ese mapa para cargar datos del INE.

## Mapas INE

Mapas descargados de https://gadm.org/download_country.html.

Niveles de agregación para España:

* ESP_0: España
* ESP_1: Comunidades
* ESP_2: Provincias
* ESP_3: Comarcas
* ESP_4: Municipios

The coordinate reference system is longitude/latitude and the WGS84 datum

## Códigos INE
Los ficheros .csv contiene la información de códigos y nombres correspondientes al INE

* ccaa_ine.csv: códigos y nombres de las CCAA
* provincias_ine.csv: códigos y nombres de las provincias
* mucicipios_ine.csv: códigos y nombres de los municipios con asignacióna provincia y CCAA. también se encuentra disponible el NATCODE de eurostat que identifica la unidad administrativa. Es un código numérico con 11 digítos como 34104646017 donde:
  
  * los dos primeros identifican el país: 34
  * los dos siguientes identifican la CCAA: 10
  * los dos siguientes identifican la provincia: 46
  * los últimos cinco identifican el municipio: 46017
  
## Códigos EUROSTAT
Fichero CSV con estructura administrativa de Eurostat. Las variables consideradas son:

* NATCODE: Código para identificar la unidad administativa con los 1 dígitos que hemos visto antes.
* NAMEUNIT: Nombre de la unidad administrativa (municipios)
* CODNUT1: Código de la región europea según definición eurostat
* CODNUT2: Código CCAA según eurostat 
* CODNUT3: Código provincia eurostat
* CODMUN: Código municipio eurostat
* CodINE: Código municipio INE
* PROVINCIA: Nombre de la provincia (Eurostat)
* LITMUN: Nombre del municipio (Eurostat)

Como la codificación de provincias no se corresponde con la oficla de españa solo podremos trabajar estos datos en la escala regiones CE, CCAA y municipios.
