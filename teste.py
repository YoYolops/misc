labels = [
    "Administração",
    "Agronomia",
    "Arquitetura e Urbanismo",
    "Arte e Mídia",
    "Ciência da Computação",
    "Ciências Biológicas",
    "Ciências Contábeis",
    "Ciências Econômicas",
    "Ciências Sociais",
    "Comunicação Social",
    "Design",
    "Direito",
    "Enfermagem",
    "Engenharia Agrícola",
    "Engenharia Ambiental",
    "Engenharia Civil",
    "Engenharia de Alimentos",
    "Engenharia de Biossistemas",
    "Engenharia de Biotecnologia e Bioprocessos",
    "Engenharia de Materiais",
    "Engenharia de Minas",
    "Engenharia de Petróleo",
    "Engenharia de Produção",
    "Engenharia Elétrica",
    "Engenharia Florestal",
    "Engenharia Mecânica",
    "Engenharia Química",
    "Estatística",
    "Farmácia",
    "Filosofia",
    "Física",
    "Geografia",
    "Gestão Pública",
    "História",
    "Letras",
    "Matemática",
    "Medicina",
    "Medicina Veterinária",
    "Meteorologia",
    "Nutrição",
    "Odontologia",
    "Pedagogia",
    "Psicologia",
    "Química"
]

data = [
    38,5, 5, 34, 114, 92, 2, 3, 5, 1,
    53, 138, 73, 8, 25, 128, 24, 1, 2, 2,
    2, 37, 7, 112, 8, 12, 7, 25, 82, 9,
    10, 99, 1, 66, 25, 71, 63, 4, 4, 90,
    4, 6, 24, 46
]

def ordena(lista, lista2):
    trocou = True

    while trocou:
        trocou = False

        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                lista2[i], lista2[i+1] = lista2[i+1], lista2[i]
                trocou = True

    return lista, lista2

l1, l2 = ordena(data, labels)

invL1 = []
invL2 = []
for i in range(len(l1)-1, -1, -1):
    invL1.append(l1[i])
    invL2.append(l2[i])

percentual = []

for i in invL1:
    perc = (100/1567) * i
    percentual.append(round(perc, 2))

print(percentual)

