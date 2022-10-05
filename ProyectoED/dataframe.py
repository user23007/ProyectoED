import pandas as pd
#import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import wkt
import networkx as nx

#-----Pone el archivo en un DataFrame-----
datos = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv', sep=';')
print(datos)

#-----Poligono de la ciudad de Medellín-----
poligono = pd.read_csv('https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/poligono_de_medellin.csv', sep=';')
print(poligono)

#-----Ingresamos los datos a un grafo-----
DG = nx.DiGraph()
for row in datos.iterrows():
    DG.add_edge(row[1]["origin"],row[1]["destination"],harassmentRisk = row[1]["harassmentRisk"])

#-----Imprime todos los grafos-----
#print(DG.nodes(data=True))

#-----Imprime un mapa de los grafos, sin embargo, es muy pesado y demora demasiado en cargar-----
#nx.draw_circular(DG, node_color="lightblue", edge_color="gray", font_size=24, width=2, with_labels=True, node_size=3500)

#-----Imprime los caminos más cortos según el riesgo-----
print(list(nx.dijkstra_path(DG, source="(-75.5764633, 6.1939332)", target="(-75.5764425, 6.1942731)", weight="harassmentRisk")))


print("Prueba finalizada")
