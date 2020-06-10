import requests
from bs4 import BeautifulSoup as bs

xlsx = openpyxl.Workbook()
sheet = xlsx.active
sheet.append(["제목", "평점", "장르", "감독", "배우"])
raw = requests.get("https://movie.naver.com/movie/running/current.nhn")
html = bs(raw.text, 'html.parser')
movie = html.select("div.lst_wrap li")

for i, m in enumerate(movie):
    title = m.select_one("dt.tit a")
    score = m.select_one("div.star_t1 span.num")
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")
    directors = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actors = m.select("dl.info_txt1 dd:nth-of-type(3) a")
    
    genre_list = [g.text for g in genre]
    directors_list = [d.text for d in directors]
    actors_list = [a.text for a in actors]
    
    genre_str = ','.join(genre_list)
    directors_str = ','.join(directors_list)
    actors_str = ','.join(actors_list)
    
    sheet.append([title.text, score.text, genre_str, directors_str, actors_str])

xlsx.save("datasheet.xlsx")
