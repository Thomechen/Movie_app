import requests
import pandas as pd
from bs4 import BeautifulSoup

class Movie:
    def __init__(self):
        self.request = requests.session()
        self.movie_list = []
        self.movie_link_list = []
        self.date_list = []
        self.theater_name_list = []
        self.theater_value_list = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69'}
        self.url = 'https://www.vscinemas.com.tw/vsTicketing/ticketing/ticket.aspx'
    def req(self,url): #網頁解析
        soup = BeautifulSoup(self.request.get(url,headers=self.headers).text,'html.parser')
        return soup
    def theater(self): #擷取戲院
        theater_name = self.req(self.url).select('section.moviePlace h3 select#theater option')
        for t in theater_name:
            self.theater_name_list.append(t.text)
            self.theater_value_list.append(t.get('value'))
    def theater_display(self): #顯示戲院名稱
        self.theater()
        for t in range(1,len(self.theater_name_list)):
            print(str(t)+'.'+self.theater_name_list[t])
    def theater_select(self,number): #戲院選擇
        theater_value = self.theater_value_list[number]
        return theater_value
    def title(self,number): #顯示電影名稱
        self.theater()
        titles = self.req(self.url+'?cinema='+self.theater_select(number)).select('ul.movieList a')
        for t in titles:
            self.movie_list.append(t.text)
            self.movie_link_list.append(t.get('href'))
        for t in range(len(self.movie_list)):
            print(str(t)+'.'+self.movie_list[t])
    def title_link(self,number): #電影連結
        link = self.movie_link_list[number]
        return link
    def title_date(self,number): #電影日期
        self.title_link(number)
        date = self.req(self.url+self.title_link(number)).select('div.movieDay')
        for d in date:
            print(d.text)
        
        


m = Movie()
m.theater_display()
s = input('select theater:')
m.title(int(s))
s = input('select movie:')
m.title_date(int(s))


