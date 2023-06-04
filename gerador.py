import folium
import pandas as pd
from folium.plugins import HeatMap
from branca.colormap import linear

dados = pd.DataFrame({
    'cidade': ["Alta Floresta D'oeste", 'Ariquemes', 'Porto Acre', 'Feira de Santana', 'Itamaraju', 'Belo Horizonte', 'João Monlevade', 'Juiz de Fora', 'Montes Claros', 'Santa Luzia', 'Vespasiano', 'Cariacica', 'Vila Velha', 'São Paulo', 'Cascavel', 'Curitiba', 'Foz do Iguaçu', 'Londrina', 'Balneário Camboriú', 'Blumenau', 'Florianópolis', 'Joinville', 'Palhoça', 'São José', 'Alvorada', 'Bom Jesus', 'Canoas', 'Caxias do Sul', 'Gravataí', 'Porto Alegre', 'Santa Maria', 'Tramandaí', 'Cuiabá', 'Várzea Grande'],
    'anuncios': [2, 1, 1, 1, 1, 33, 1, 2, 1, 4, 2, 1, 1 , 1, 1, 1, 1, 1, 1, 2, 1, 3, 1, 2, 1, 1, 2, 2, 1, 5, 1, 1, 1, 1],
    'latitude': [-11.935540, -9.913682, -9.581628, -12.257486, -17.043447, -19.921075, -19.816930, -19.825741, -19.813470, -19.806700, -19.798604, -19.790741, -20.275330, -20.328436, -24.984390, -25.492157, -26.234302, -26.889977, -27.098628, -27.597300, -26.293494, -27.625290, -27.586730, -29.978930, -29.940090, -29.909676, -30.029490, -29.951850, -29.826650, -30.054687, -29.683530, -29.676780, -15.601, -15.6486],
    'longitude': [-61.996283, -59.553131, -52.058714, -38.966717, -40.343675, -43.945096, -43.269082, -43.940729, -43.939424, -43.797285, -43.931671, -44.340758, -44.297366, -44.322572, -53.479700, -49.265368, -54.592918, -49.363358, -48.660610, -49.082229, -48.501705, -49.066080, -48.662790, -48.825600, -48.668200, -48.667700, -51.080400, -51.166900, -51.179800, -51.179400, -51.160400, -51.088600, -56.0974, -56.1199]
})

# Cria um mapa centrado no Brasil
mapa = folium.Map(location=[-15.788497, -47.879873], zoom_start=4)

# Cria um mapa de calor a partir das coordenadas geográficas e do número de anúncios
dados_mapa = dados[['latitude', 'longitude', 'anuncios']].values.tolist()
HeatMap(dados_mapa, name='anuncios').add_to(mapa)

# Adiciona um controle de camadas ao mapa
folium.LayerControl().add_to(mapa)

mapa.save('mapa.html')