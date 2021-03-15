#coding: utf-8

from TwitterAPI import TwitterAPI
from datetime import datetime
import json, re

class Tweety:
    keys = {
        "consumer_key":"xpd1AxFKEah0v6zMxjL9Mk9aV",
        "consumer_secret":"1omjTTp8q7rYfvovN1sxX9paAipEMbAKLRSLyfj7Hg9pQYcl7V",
        "token_key":"1361963011582394369-1t6HtH7UYClzx6rBxddp6wan1RX9gL",
        "token_secret":"dYvgSJpwBath4zG2n3aRuth6HNNoQ3xB2Qworr7SHqAo2"
    }

    api = TwitterAPI(keys['consumer_key'],keys['consumer_secret'],
                     keys['token_key'],keys['token_secret'])

    '''end_points'''
    endp = {"search":"search/tweets"}

    '''Realiza uma busca pelo termo e retorna um TwitterResponse'''
    def search_term(self,term):
        return self.api.request(self.endp['search'], {'q':term,
                                                     'lang':'pt'
                                                        })
    
    def filter(self,tw_response):
        jso = []
        for tw in tw_response:
            if(not tw['truncated']):
                twt = {}
                twt['username'] = tw['user']['name']
                twt['nickname'] = tw['user']['screen_name']
                twt['url_foto_perfil'] = tw['user']['profile_image_url']
                twt['conteudo'] = tw['text']
                twt['cardClass'] = "card"
                jso.append(twt)

        return {"twetts":jso}