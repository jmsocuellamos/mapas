def plot_spain_regions(shpfile):
  """
  Función para represntar gráficamente la geometría correspondiente a 
  las regiones de la CE. En este caso no graficamos ninguna variable.

  Parámetros:
    - shpfile: geometria que deseamos representar

  Devuelve:
    Representación de la geometría recolocando las islas canarias
  """
  # Selección de canarias
  canarias = ["ES7"]
  spain_n3_canarias = shpfile[shpfile["NUTS_ID"].isin(canarias)]
  spain_n3_resto = shpfile[~shpfile["NUTS_ID"].isin(canarias)]
  # Represenatción gráfica
  fig, ax = plt.subplots()
  # Añade ax para recolocar canarias
  ax_canarias = fig.add_axes([0.5, 0.15, 0.5, 0.12])
  # mapas de cada uno
  spain_n3_resto.plot(facecolor = 'white', edgecolor='black', ax=ax)
  spain_n3_canarias.plot(facecolor = 'white', edgecolor='black', ax=ax_canarias)
  # Configuración de ejes
  ax.set_axis_off()
  ax_canarias.set(yticks=[],xticks=[])
  fig.set_size_inches(8, 8)

def plot_spain_ccaa(shpfile):
  """
  Función para represntar gráficamente la geometría correspondiente a 
  las CCAA. En este caso no graficamos ninguna variable.

  Parámetros:
    - shpfile: geometria que deseamos representar

  Devuelve:
    Representación de la geometría recolocando las islas canarias 
  """
  # Selección 
  canarias = ["ES70"]
  spain_n3_canarias = shpfile[shpfile["NUTS_ID"].isin(canarias)]
  spain_n3_resto = shpfile[~shpfile["NUTS_ID"].isin(canarias)]
  # Represenatción gráfica
  fig, ax = plt.subplots()
  # Añade ax para recolocar canarias
  ax_canarias = fig.add_axes([0.5, 0.15, 0.5, 0.12])
  # mapas de cada uno
  spain_n3_resto.plot(facecolor = 'white', edgecolor='black', ax=ax)
  spain_n3_canarias.plot(facecolor = 'white', edgecolor='black', ax=ax_canarias)
  # Configuración de ejes
  ax.set_axis_off()
  ax_canarias.set(yticks=[],xticks=[])
  fig.set_size_inches(8, 8)

def plot_spain_provincias(shpfile):
  """
  Función para represntar gráficamente la geometría correspondiente a 
  las provincias. En este caso no graficamos ninguna variable.

  Parámetros:
    - shpfile: geometria que deseamos representar

  Devuelve:
    Representación de la geometría recolocando las islas canarias
  """
  # Selección 
  canarias = [35,38]
  spain_n3_canarias = shpfile[shpfile["CPRO"].isin(canarias)]
  spain_n3_resto = shpfile[~shpfile["CPRO"].isin(canarias)]
  # Represenatción gráfica
  fig, ax = plt.subplots()
  # Añade ax para recolocar canarias
  ax_canarias = fig.add_axes([0.5, 0.15, 0.5, 0.12])
  # mapas de cada uno
  spain_n3_resto.plot(facecolor = 'white', edgecolor='black', ax=ax)
  spain_n3_canarias.plot(facecolor = 'white', edgecolor='black', ax=ax_canarias)
  # Configuración de ejes
  ax.set_axis_off()
  ax_canarias.set(yticks=[],xticks=[])
  fig.set_size_inches(8, 8)
