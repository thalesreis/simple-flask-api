from math import sqrt

def euclidiana(base, id_user1, id_user2):
    si = {}
    for vinho in base[id_user1]:
        if vinho in base[id_user2]: si[vinho] = 1

    if len(si) == 0: return 0

    soma = sum([pow(base[id_user1][item] - base[id_user2][item], 2)
                for item in base[id_user1] if item in base[id_user2]])

    return 1/(1+sqrt(soma))

def getSimilares(base, nota_user):
    similaridade = [
        (euclidiana(base, nota_user, outro_user), outro_user)
        for outro_user in base if outro_user != nota_user
    ]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]

def calculaItensSimilares(notas_user_vinhos):
    result = {}
    for nota_user in notas_user_vinhos:
        # print(notas_user_vinhos[nota_user])
        notas = getSimilares(notas_user_vinhos, nota_user)
        result[nota_user] = notas
    return result