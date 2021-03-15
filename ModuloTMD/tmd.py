#coding: utf-8

import time, hashlib, requests, json

class TmdAPI:

    url = 'https://api.themoviedb.org/3/search/movie?api_key=aca091ff25f57defc404ef8edf229ea0&query='
    #urlGen = 'https://api.themoviedb.org/3/genre/movie/list?api_key=aca091ff25f57defc404ef8edf229ea0&language=en-US'

    
    def request_filme(self, filme):
        filme.replace(" ", "+")
        req = self.url + filme

        return requests.get(req).text

    def listaDeGeneros(self):
        req = self.urlGen
        return requests.get(req).text

    ''' Filtra os resultados e devolve apenas os dados necessários para a aplicação '''
    def filme(self, json_str):
        jsonResponse = json.loads(json_str)

        nomeGeneros = ''
        filme = json.loads(json_str)['results'][0]
        filme_out = {}
        filme_out['status'] = 200
        filme_out['titulo'] = filme['original_title']
        filme_out['resumo'] = filme['overview']
        filme_out['data'] = filme['release_date']
        filme_out['img_url'] = "http://image.tmdb.org/t/p/w185/" + filme['poster_path']
    

        return json.dumps(filme_out)

