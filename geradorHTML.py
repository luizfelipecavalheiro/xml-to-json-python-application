import json
from bs4 import BeautifulSoup as Soup


def adicionaTags(filme_id,texto,inicio):
    
    if inicio == True:
        with open("template.html") as file:
            htmlFile = file.read()
            soup = Soup(htmlFile,'html.parser') 
        
        linkTag = soup.find('link')
        newLinkTag = soup.new_tag('link')
        newLinkTag['href'] = "../css/style.css"
        newLinkTag['rel'] = "stylesheet"
        newLinkTag['type'] = "text/css"
        linkTag.insert_after(newLinkTag)

        trTag = soup.find('tr')
        newTrTag = soup.new_tag('tr')
        trTag.insert_after(newTrTag) 

        tdTag = soup.new_tag('td') 
        tdTag['align'] = "center"
        newTrTag.insert(1,tdTag)

        aTag = soup.new_tag('a') 
        aTag['href'] = "../index.html"
        aTag.string = "VOLTAR"
        tdTag.insert(1,aTag)


    else:
        with open("paginas/" + filme_id + ".html") as file:        
            htmlFile = file.read()
            soup = Soup(htmlFile,'html.parser') 


    with open("paginas/" + filme_id + ".html","w") as filmeFile:
        
        trTag = soup.find('tr')
        newTrTag = soup.new_tag('tr')
        trTag.insert_after(newTrTag) 

        tdTag = soup.new_tag('td') 
        tdTag['align'] = "center"
        tdTag.string = texto
        newTrTag.insert(1,tdTag)

        filmeFile.write(str(soup))


# Abre arquivo JSON
with open("GioMovies.json") as json_data:
    data = json.load(json_data)

# Tamanho de cada tópico
tam_association = len(data['topicMap']['association'])
tam_topic = len(data['topicMap']['topic'])

# Abre arquivo HTML
with open("template.html",) as file:
    htmlFile = file.read()
soup = Soup(htmlFile,'html.parser') 

lista_filmes = []
lista_filmes_id = []

for i in range(0,tam_topic):
    if 'instanceOf' in data['topicMap']['topic'][i]:
        if data['topicMap']['topic'][i]['instanceOf']['topicRef']['@href'] == '#Filme':
            lista_filmes.append(data['topicMap']['topic'][i]['baseName']['baseNameString'])
            lista_filmes_id.append(data['topicMap']['topic'][i]['@id'])


#Gera a tabela com os títulos dos filmes
for i in range(0,len(lista_filmes)):
    trTag = soup.find('tr')
    newTrTag = soup.new_tag('tr')
    trTag.insert_after(newTrTag) 

    tdTag = soup.new_tag('td') 
    tdTag['align'] = "center"
    newTrTag.insert(1,tdTag)

    aTag = soup.new_tag('a') 
    aTag['href'] = 'paginas/' + lista_filmes_id[i] + ".html"
    aTag.string = lista_filmes[i]
    tdTag.insert(1,aTag)
 

with open("index.html", "w") as html_file_write:
    html_file_write.write(str(soup))


# Gera a tabela com o conteúdo dos filmes
for i in range(0,tam_topic):
    
    if 'instanceOf' in data['topicMap']['topic'][i]:
        # se o id é igual ao do filme que foi clicado
        if data['topicMap']['topic'][i]['instanceOf']['topicRef']['@href'] == '#Filme':
            filme_id = data['topicMap']['topic'][i]['@id']
    
            #Filme
            adicionaTags(filme_id,data['topicMap']['topic'][i]['instanceOf']['topicRef']['@href'],True)
            #Nome do filme
            adicionaTags(filme_id,data['topicMap']['topic'][i]['baseName']['baseNameString'],False)

            if 'occurrence' in data['topicMap']['topic'][i]:
                if type(data['topicMap']['topic'][i]['occurrence']) == list:
                    tam_occurrence = len(data['topicMap']['topic'][i]['occurrence'])
                    for j in range(0,tam_occurrence):
                        if 'scope' in data['topicMap']['topic'][i]['occurrence'][j]:
                            #adiciona scope
                            adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence'][j]['scope']['topicRef']['@href'],False)
                        
                        if 'resourceData' in data['topicMap']['topic'][i]['occurrence'][j]:
                            #adiciona resourceData
                            adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence'][j]['resourceData'],False)
                        
                        if 'instanceOf' in data['topicMap']['topic'][i]['occurrence'][j]:
                            #adiciona instanceOf
                            adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence'][j]['instanceOf']['topicRef']['@href'],False)
                        
                        if 'resourceRef' in data['topicMap']['topic'][i]['occurrence'][j]:
                            #adiciona resourceRef
                            adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence'][j]['resourceRef']['@href'],False)
                else:
                    if 'scope' in data['topicMap']['topic'][i]['occurrence']:
                        #adiciona scope
                        adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence']['scope']['topicRef']['@href'],False)
                    
                    if 'resourceData' in data['topicMap']['topic'][i]['occurrence']:
                        #adiciona resourceData
                        adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence']['resourceData'],False)
                    
                    if 'instanceOf' in data['topicMap']['topic'][i]['occurrence']:
                        #adiciona instanceOf
                        adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence']['instanceOf']['topicRef']['@href'],False)
                    
                    if 'resourceRef' in data['topicMap']['topic'][i]['occurrence']:
                        #adiciona resourceRef
                        adicionaTags(filme_id,data['topicMap']['topic'][i]['occurrence']['resourceRef']['@href'],False)

            for j in range(0,tam_association):
                if data['topicMap']['association'][j]['member'][0]['topicRef']['@href'][1:] == filme_id:
                    #tipo de association
                    adicionaTags(filme_id,data['topicMap']['association'][j]['instanceOf']['topicRef']['@href'],False)

                    member_id = data['topicMap']['association'][j]['member'][1]['topicRef']['@href'][1:]

                    for k in range (0,tam_topic):
                        if data['topicMap']['topic'][k]['@id'] == member_id:
                            #Nome dos membros
                            adicionaTags(filme_id,data['topicMap']['topic'][k]['baseName']['baseNameString'],False)

