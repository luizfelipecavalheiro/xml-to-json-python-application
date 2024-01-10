# xml-to-json-python-application
Aplicação com transformação de arquivo XML para JSON contendo consultas JQuery utilizando Python.

1) Rodar o arquivo 'xmlToJson.py' que irá pegar o arquivo 'GioMovies.xtm' (formato XML) e com base nele criar o arquivo 'GioMovies.json', que conterá todos os dados contidos no arquivo XML, porém, no formato JSON, para isso execute o seguinte comando no terminal no diretório que contém os arquivos:
    
    ```$ python3 xmlToJson.py```

2) Para realizar as consultas a seguir:
    
    a) Quais são os tipos de gênero de filmes, sem repetição?
    b) Quais são os títulos dos filmes que foram produzidos em 2000, ordenados alfabeticamente?
    c) Quais são os títulos em inglês dos filmes que tem a palavra “especial” na sinopse?
    d) Quais são os sites dos filmes que são do tipo “thriller”?
    e) Quantos filmes contém mais de 3 atores como elenco de apoio?
    f) Quais são os ID dos filmes que tem o nome de algum membro do elenco citado na sinopse?
 
- Basta executar o arquivo ```consultasGioMovies.py``` com o seguinte comando:

    ```$ python3 consultasGioMovies.py```

3) Para gerar o conjunto de páginas HTML contendo a lista de filmes e suas respectivas informações, basta executar o arquivo geradorHTML.py, que tem como base um template disponível na internet, será gerado o arquivo 'index.html' na raiz do diretório e também a página de cada filme dentro do diretório "paginas", para executar o arquivo, digite no terminal:

    ```$ python3 geradorHTML.py```

   
    Agora que as páginas já foram geradas, para "navegar" por ela, basta abrir com o navegador o arquivo 'index.html'
