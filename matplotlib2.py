import matplotlib.pyplot as plt

def carregarDados(nomeArq):
    aux = []
    with open(nomeArq) as cvs:
        cvs.readline()
        for linha in cvs:
            nova = [float(val) for val in linha.split(',')]
            aux.append(nova)
        return aux

dados = carregarDados("california_housing_test.csv")
longitudes = [aux[0] for aux in dados]
latitudes = [aux[1] for aux in dados]
plt.scatter(longitudes,latitudes,s=1)
plt.show()