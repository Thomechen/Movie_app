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
        for t in range(1,len(self.theater_name_list)): 
            print(str(t)+'.'+self.theater_name_list[t]) #列出電影名稱
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
    def title_date(self): #電影日期
        date = self.req(self.url+self.title_link(int(input('Select Movie:')))).select('div.movieDay h4')
        for d in date:
            self.date_list.append(d.text)
        for d in range(len(self.date_list)):
            print(str(d)+'.'+self.date_list[d]) #電影日期顯示
        if self.date_list[int(input('Select Date:'))] == date[0].text:
            for i in date[0].select('li a'):
                print(i.text)
                
        
        


m = Movie()
m.theater() 
m.title(int(input('select theater:')))
m.title_date()


