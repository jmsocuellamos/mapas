{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red245\green245\blue245;\red0\green0\blue0;
\red101\green76\blue29;\red0\green0\blue109;\red144\green1\blue18;\red15\green112\blue1;\red19\green85\blue52;
\red31\green99\blue128;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c63922\c8235\c8235;\cssrgb\c0\c50196\c0;\cssrgb\c6667\c40000\c26667;
\cssrgb\c14510\c46275\c57647;}
\paperw11900\paperh16840\margl1440\margr1440\vieww30700\viewh12620\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 def\cf0 \strokec4  \cf5 \strokec5 plot_spain_regions\cf0 \strokec4 (\cf6 \strokec6 shpfile\cf0 \strokec4 ):\cb1 \
\cb3   \cf7 \strokec7 """\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   Funci\'f3n para represntar gr\'e1ficamente la geometr\'eda correspondiente a \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   las regiones de la CE. En este caso no graficamos ninguna variable.\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7   Par\'e1metros:\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     - shpfile: geometria que deseamos representar\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7   Devuelve:\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     Representaci\'f3n de la geometr\'eda recolocando las islas canarias\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   """\cf0 \cb1 \strokec4 \
\cb3   \cf8 \strokec8 # Selecci\'f3n de canarias\cf0 \cb1 \strokec4 \
\cb3   canarias = [\cf7 \strokec7 "ES7"\cf0 \strokec4 ]\cb1 \
\cb3   spain_n3_canarias = shpfile[shpfile[\cf7 \strokec7 "NUTS_ID"\cf0 \strokec4 ].isin(canarias)]\cb1 \
\cb3   spain_n3_resto = shpfile[~shpfile[\cf7 \strokec7 "NUTS_ID"\cf0 \strokec4 ].isin(canarias)]\cb1 \
\cb3   \cf8 \strokec8 # Represenatci\'f3n gr\'e1fica\cf0 \cb1 \strokec4 \
\cb3   fig, ax = plt.subplots()\cb1 \
\cb3   \cf8 \strokec8 # A\'f1ade ax para recolocar canarias\cf0 \cb1 \strokec4 \
\cb3   ax_canarias = fig.add_axes([\cf9 \strokec9 0.5\cf0 \strokec4 , \cf9 \strokec9 0.15\cf0 \strokec4 , \cf9 \strokec9 0.5\cf0 \strokec4 , \cf9 \strokec9 0.12\cf0 \strokec4 ])\cb1 \
\cb3   \cf8 \strokec8 # mapas de cada uno\cf0 \cb1 \strokec4 \
\cb3   spain_n3_resto.plot(facecolor = \cf7 \strokec7 'white'\cf0 \strokec4 , edgecolor=\cf7 \strokec7 'black'\cf0 \strokec4 , ax=ax)\cb1 \
\cb3   spain_n3_canarias.plot(facecolor = \cf7 \strokec7 'white'\cf0 \strokec4 , edgecolor=\cf7 \strokec7 'black'\cf0 \strokec4 , ax=ax_canarias)\cb1 \
\cb3   \cf8 \strokec8 # Configuraci\'f3n de ejes\cf0 \cb1 \strokec4 \
\cb3   ax.set_axis_off()\cb1 \
\cb3   ax_canarias.\cf10 \strokec10 set\cf0 \strokec4 (yticks=[],xticks=[])\cb1 \
\cb3   fig.set_size_inches(\cf9 \strokec9 8\cf0 \strokec4 , \cf9 \strokec9 8\cf0 \strokec4 )\
\
\
\cf2 \strokec2 def\cf0 \strokec4  \cf5 \strokec5 plot_spain_ccaa\cf0 \strokec4 (\cf6 \strokec6 shpfile\cf0 \strokec4 ):\cb1 \
\cb3   \cf7 \strokec7 """\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   Funci\'f3n para represntar gr\'e1ficamente la geometr\'eda correspondiente a \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   las CCAA. En este caso no graficamos ninguna variable.\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7   Par\'e1metros:\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     - shpfile: geometria que deseamos representar\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7   Devuelve:\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     Representaci\'f3n de la geometr\'eda recolocando las islas canarias \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   """\cf0 \cb1 \strokec4 \
\cb3   \cf8 \strokec8 # Selecci\'f3n \cf0 \cb1 \strokec4 \
\cb3   canarias = [\cf7 \strokec7 "ES70"\cf0 \strokec4 ]\cb1 \
\cb3   spain_n3_canarias = shpfile[shpfile[\cf7 \strokec7 "NUTS_ID"\cf0 \strokec4 ].isin(canarias)]\cb1 \
\cb3   spain_n3_resto = shpfile[~shpfile[\cf7 \strokec7 "NUTS_ID"\cf0 \strokec4 ].isin(canarias)]\cb1 \
\cb3   \cf8 \strokec8 # Represenatci\'f3n gr\'e1fica\cf0 \cb1 \strokec4 \
\cb3   fig, ax = plt.subplots()\cb1 \
\cb3   \cf8 \strokec8 # A\'f1ade ax para recolocar canarias\cf0 \cb1 \strokec4 \
\cb3   ax_canarias = fig.add_axes([\cf9 \strokec9 0.5\cf0 \strokec4 , \cf9 \strokec9 0.15\cf0 \strokec4 , \cf9 \strokec9 0.5\cf0 \strokec4 , \cf9 \strokec9 0.12\cf0 \strokec4 ])\cb1 \
\cb3   \cf8 \strokec8 # mapas de cada uno\cf0 \cb1 \strokec4 \
\cb3   spain_n3_resto.plot(facecolor = \cf7 \strokec7 'white'\cf0 \strokec4 , edgecolor=\cf7 \strokec7 'black'\cf0 \strokec4 , ax=ax)\cb1 \
\cb3   spain_n3_canarias.plot(facecolor = \cf7 \strokec7 'white'\cf0 \strokec4 , edgecolor=\cf7 \strokec7 'black'\cf0 \strokec4 , ax=ax_canarias)\cb1 \
\cb3   \cf8 \strokec8 # Configuraci\'f3n de ejes\cf0 \cb1 \strokec4 \
\cb3   ax.set_axis_off()\cb1 \
\cb3   ax_canarias.\cf10 \strokec10 set\cf0 \strokec4 (yticks=[],xticks=[])\cb1 \
\cb3   fig.set_size_inches(\cf9 \strokec9 8\cf0 \strokec4 , \cf9 \strokec9 8\cf0 \strokec4 )\cb1 \
\
\
\cf2 \cb3 \strokec2 def\cf0 \strokec4  \cf5 \strokec5 plot_spain_provincias\cf0 \strokec4 (\cf6 \strokec6 shpfile\cf0 \strokec4 ):\cb1 \
\cb3   \cf7 \strokec7 """\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   Funci\'f3n para represntar gr\'e1ficamente la geometr\'eda correspondiente a \cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   las provincias. En este caso no graficamos ninguna variable.\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7   Par\'e1metros:\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     - shpfile: geometria que deseamos representar\cf0 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7   Devuelve:\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7     Representaci\'f3n de la geometr\'eda recolocando las islas canarias\cf0 \cb1 \strokec4 \
\cf7 \cb3 \strokec7   """\cf0 \cb1 \strokec4 \
\cb3   \cf8 \strokec8 # Selecci\'f3n \cf0 \cb1 \strokec4 \
\cb3   canarias = [\cf9 \strokec9 35\cf0 \strokec4 ,\cf9 \strokec9 38\cf0 \strokec4 ]\cb1 \
\cb3   spain_n3_canarias = shpfile[shpfile[\cf7 \strokec7 "CPRO"\cf0 \strokec4 ].isin(canarias)]\cb1 \
\cb3   spain_n3_resto = shpfile[~shpfile[\cf7 \strokec7 "CPRO"\cf0 \strokec4 ].isin(canarias)]\cb1 \
\cb3   \cf8 \strokec8 # Represenatci\'f3n gr\'e1fica\cf0 \cb1 \strokec4 \
\cb3   fig, ax = plt.subplots()\cb1 \
\cb3   \cf8 \strokec8 # A\'f1ade ax para recolocar canarias\cf0 \cb1 \strokec4 \
\cb3   ax_canarias = fig.add_axes([\cf9 \strokec9 0.5\cf0 \strokec4 , \cf9 \strokec9 0.15\cf0 \strokec4 , \cf9 \strokec9 0.5\cf0 \strokec4 , \cf9 \strokec9 0.12\cf0 \strokec4 ])\cb1 \
\cb3   \cf8 \strokec8 # mapas de cada uno\cf0 \cb1 \strokec4 \
\cb3   spain_n3_resto.plot(facecolor = \cf7 \strokec7 'white'\cf0 \strokec4 , edgecolor=\cf7 \strokec7 'black'\cf0 \strokec4 , ax=ax)\cb1 \
\cb3   spain_n3_canarias.plot(facecolor = \cf7 \strokec7 'white'\cf0 \strokec4 , edgecolor=\cf7 \strokec7 'black'\cf0 \strokec4 , ax=ax_canarias)\cb1 \
\cb3   \cf8 \strokec8 # Configuraci\'f3n de ejes\cf0 \cb1 \strokec4 \
\cb3   ax.set_axis_off()\cb1 \
\cb3   ax_canarias.\cf10 \strokec10 set\cf0 \strokec4 (yticks=[],xticks=[])\cb1 \
\cb3   fig.set_size_inches(\cf9 \strokec9 8\cf0 \strokec4 , \cf9 \strokec9 8\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf0 \
}