import json

with open("GioMovies.json") as json_data:
    data = json.load(json_data)

tam_association = len(data['topicMap']['association'])
tam_topic = len(data['topicMap']['topic'])


######################################################################################################

print("a) Quais são os tipos de gênero de filmes, sem repetição?:\n")
lista_genero = []


for i in range(0,tam_association):
    if data['topicMap']['association'][i]['instanceOf']['topicRef']['@href'] == "#filme-genero":
        genero = data['topicMap']['association'][i]['member'][-1]['topicRef']['@href'][1:]
        
        for j in range (0,tam_topic):
            if data['topicMap']['topic'][j]['@id'] == genero:
                nome_genero = data['topicMap']['topic'][j]['baseName']['baseNameString']
        
                if(nome_genero not in lista_genero):
                    lista_genero.append(nome_genero)
                    print(nome_genero)



######################################################################################################

print("\n\nb) Quais são os títulos dos filmes que foram produzidos em 2000, ordenados alfabeticamente?\n")
lista_filmes2000 = []
for i in range (0,tam_association):
    if data['topicMap']['association'][i]['instanceOf']['topicRef']['@href'] == "#filme-ano":
        if data['topicMap']['association'][i]['member'][-1]['topicRef']['@href'][-4:] == '2000':
            id_filme = data['topicMap']['association'][i]['member'][0]['topicRef']['@href'][1:]
            
            for j in range (0,tam_topic):
                if data['topicMap']['topic'][j]['@id'] == id_filme:
                    lista_filmes2000.append(data['topicMap']['topic'][j]['baseName']['baseNameString'])

lista_filmes2000.sort()
print(lista_filmes2000)



######################################################################################################


print("\n\nc) Quais são os títulos em inglês dos filmes que tem a palavra “especial” na sinopse?\n")

for i in range(0,tam_topic):
    if 'occurrence' in data['topicMap']['topic'][i]:
        if type(data['topicMap']['topic'][i]['occurrence']) == list:
            if data['topicMap']['topic'][i]['occurrence'][0]['scope']['topicRef']['@href'] == '#ingles':    
                tam_occurrence = len(data['topicMap']['topic'][i]['occurrence'])
                for j in range (0,tam_occurrence):
                    if 'resourceData' in data['topicMap']['topic'][i]['occurrence'][j]:
                        if 'especial' in data['topicMap']['topic'][i]['occurrence'][j]['resourceData']:
                            print(data['topicMap']['topic'][i]['occurrence'][0]['resourceData'])
                


######################################################################################################


print("\n\nd) Quais são os sites dos filmes que são do tipo “thriller”?\n")

for i in range(0,tam_association):
    if data['topicMap']['association'][i]['instanceOf']['topicRef']['@href'] == "#filme-genero":
        if data['topicMap']['association'][i]['member'][1]['topicRef']['@href'] == '#thriller':
            id_filme =  data['topicMap']['association'][i]['member'][0]['topicRef']['@href'][1:]
            for j in range(0,tam_topic): 
                if data['topicMap']['topic'][j]['@id'] == id_filme:
                    if 'resourceRef' in data['topicMap']['topic'][j]['occurrence'][-1]:
                        print(data['topicMap']['topic'][j]['occurrence'][-1]['resourceRef']['@href'])



######################################################################################################

print("\n\ne) Quantos filmes contém mais de 3 atores como elenco de apoio?\n")

num_filmes = 0
num_atores = 0

for i in range(0,tam_topic):
    if 'occurrence' in data['topicMap']['topic'][i]:
        if type(data['topicMap']['topic'][i]['occurrence']) == list:
            tam_occurrence = len(data['topicMap']['topic'][i]['occurrence'])
            for j in range (0,tam_occurrence):
                if 'scope' in data['topicMap']['topic'][i]['occurrence'][j]:
                    if data['topicMap']['topic'][i]['occurrence'][j]['scope']['topicRef']['@href'] == '#elencoApoio':
                        num_atores += 1
            
                if num_atores >= 3:
                    num_filmes += 1
                    num_atores = 0
                    break

print(num_filmes)



######################################################################################################

print("\n\nf) Quais são os ID dos filmes que tem o nome de algum membro do elenco citado na sinopse?\n")

lista_idfilme_nome_sinopse = []

for i in range(0,tam_association):
    if data['topicMap']['association'][i]['instanceOf']['topicRef']['@href'] == "#filme-elenco":
        id_filme = data['topicMap']['association'][i]['member'][0]['topicRef']['@href'][1:]
        id_ator = data['topicMap']['association'][i]['member'][1]['topicRef']['@href'][1:]
        for j in range(0,tam_topic):
            if data['topicMap']['topic'][j]['@id'] == id_ator:
                nome_ator = data['topicMap']['topic'][j]['baseName']['baseNameString']
                for k in range (0,tam_topic):
                    if data['topicMap']['topic'][k]['@id'] == id_filme:
                        if 'occurrence' in data['topicMap']['topic'][k]:
                            if type(data['topicMap']['topic'][k]['occurrence']) == list:
                                tam_occurrence = len(data['topicMap']['topic'][k]['occurrence'])
                                for l in range (0,tam_occurrence):
                                    if 'resourceData' in data['topicMap']['topic'][k]['occurrence'][l]:
                                        if nome_ator in data['topicMap']['topic'][k]['occurrence'][l]['resourceData']:
                                            if id_filme not in lista_idfilme_nome_sinopse:
                                                lista_idfilme_nome_sinopse.append(id_filme)
                                                print(id_filme)



