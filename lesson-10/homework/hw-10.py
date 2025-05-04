# import sqlite3
# conn = sqlite3.connect('roster.db')
# cur = conn.cursor()
# cur.execute('''
#     CREATE TABLE IF NOT EXISTS Roster (
#         Name TEXT,
#         Species TEXT,
#         Age INTEGER
#     )
# ''')
# conn.commit()
# conn.close()
# print("Ma'lumotlar bazasi va Roster jadvali muvaffaqiyatli yaratildi.")
################################# 2-misol ########################################
# import sqlite3
# from tabulate import tabulate
# conn = sqlite3.connect('roster.db')
# cur = conn.cursor()
# cur.execute("SELECT * FROM Roster")
# rows = cur.fetchall()
# headers = ["Ism", "Turlar", "Yosh"]
# print("2.Ma'lumotlarni kiritish:\n")
# print("- Ro'yxat jadvalini quyidagi yozuvlar bilan to'ldiring:\n")
# print(tabulate(rows, headers=headers, tablefmt="grid"))
# conn.close()
################################# 3-misol ########################################
# data = {
#     'data_name': 'Jadzia Dax'
# }
# data['data_name'] = 'Ezri Dax'
# print("Yangilangan ism:", data['data_name'])
################################# 4-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 50, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 40, 'species': 'Bajoran'}
# ]
# bajoran_data = [char for char in data if char['species'] == 'Bajoran']
# for char in bajoran_data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 5-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 68, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 67, 'species': 'Bajoran'}
# ]
# data = [char for char in data if char['age'] <= 100]
# for char in data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 6-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 68, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 67, 'species': 'Bajoran'}
# ]
# for char in data:
#     if char['name'] == 'Jadzia Dax' or char['name'] == 'Ezri Dax':
#         char['rank'] = 'Commander'
#     elif char['name'] == 'Kira Nerys':
#         char['rank'] = 'Major'
#     elif char['name'] == 'Worf':
#         char['rank'] = 'Lieutenant'
#     elif char['name'] == 'Bashir Julian':
#         char['rank'] = 'Doctor'
#     elif char['name'] == 'Kassidy Yates':
#         char['rank'] = 'Captain'
#     else:
#         char['rank'] = 'Ensign'
# for char in data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}, Rank: {char.get('rank', 'No rank')}")
################################# 7-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 150, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},


#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 120, 'species': 'Bajoran'}
# ]
# sorted_data = sorted(data, key=lambda char: char['age'], reverse=True)
# for char in sorted_data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 2-Task #########################################
################################# 1-misol ########################################
# data = [
#     {'name': 'Jadzia Dax', 'age': 29, 'species': 'Trill'},
#     {'name': 'Ezri Dax', 'age': 28, 'species': 'Trill'},
#     {'name': 'Kira Nerys', 'age': 30, 'species': 'Bajoran'},
#     {'name': 'Odo', 'age': 150, 'species': 'Changeling'},
#     {'name': 'Worf', 'age': 40, 'species': 'Klingon'},
#     {'name': 'Bashir Julian', 'age': 35, 'species': 'Human'},
#     {'name': 'Kassidy Yates', 'age': 32, 'species': 'Human'},
#     {'name': 'Bajoran Character 1', 'age': 120, 'species': 'Bajoran'}
# ]
# sorted_data = sorted(data, key=lambda char: char['age'], reverse=True)
# for char in sorted_data:
#     print(f"Ism: {char['name']}, Yosh: {char['age']}")
################################# 2-misol ########################################
# books = []
# books.append({'title': 'Deep Space Nine: The Siege', 'author': 'Peter David', 'year': 1994})
# books.append({'title': 'Unity', 'author': 'S.D. Perry', 'year': 2003})
# books.append({'title': 'Avatar, Book One', 'author': 'S.D. Perry', 'year': 2001})
# books.append({'title': 'A Stitch in Time', 'author': 'Andrew J. Robinson', 'year': 2000})
# books.append({'title': 'Rising Son', 'author': 'S.D. Perry', 'year': 2003})
# for book in books:
#     print(f"Sarlavha: {book['title']}, Muallif: {book['author']}, Yili: {book['year']}")
################################# 3-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1984},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'year_published': 1932}
# ]
# for book in books:
#     if book['year_published'] == 1984:
#         book['year_published'] = 1950
# for book in books:
#     print(f"Sarlavha: {book['title']}, Muallif: {book['author']}, Yili: {book['year_published']}")
################################# 4-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'genre': 'Dystopian'},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'genre': 'Dystopian'},
#     {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury', 'genre': 'Dystopian'},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'genre': 'Romance'}
# ]
# for book in books:
#     if book['genre'] == 'Dystopian':
#         print(f"Sarlavha: {book['title']}, Muallif: {book['author']}")
################################# 5-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1950},
#     {'title': 'Brave New World', 'author': 'Aldous Huxley', 'year_published': 1932},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year_published': 1813}
# ]
# books = [book for book in books if book['year_published'] >= 1950]
# for book in books:
#     print(f"Sarlavha: {book['title']}, Muallif: {book['author']}, Yili: {book['year_published']}")
################################# 6-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1950},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year_published': 1813}
# ]
# ratings = {
#     'To Kill a Mockingbird': 4.8,
#     '1984': 4.7,
#     'The Great Gatsby': 4.5
# }
# for book in books:
#     book['rating'] = ratings.get(book['title'], None)  
# for book in books:
#     print(f"Sarlavha: {book['title']}, Reyting: {book['rating']}")
################################# 7-misol ########################################
# books = [
#     {'title': '1984', 'author': 'George Orwell', 'year_published': 1950},
#     {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year_published': 1960},
#     {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year_published': 1925},
#     {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year_published': 1813}
# ]
# sorted_books = sorted(books, key=lambda book: book['year_published'])
# for book in sorted_books:
#     print(f"Sarlavha: {book['title']}, Yili: {book['year_published']}")
# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# import uvicorn
# import webbrowser
# from weather_service import weather
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")
# @app.get("/")
# async def home(request: Request):
#     weather = weather("Tashkent")
#     return templates.TemplateResponse("index.html", {"request": request, "weather": weather})
# if __name__ == "__main__":
#     url = "http://127.0.0.1:8000"
#     webbrowser.open(url)
#     uvicorn.run(app, host="127.0.0.1", port=8000)
# import requests
# def weather(shahar):
#     api_key = "181472b3e6c642ccfbdcb1698c57905c" 
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={shahar}&units=metric&appid={api_key}"
#     response = requests.get(url)
#     malumotlar = response.json()
#     ob_havo = {
#         "Shahar": shahar,
#         "temp": malumotlar["main"]["temp"],
#         "tavsifi": malumotlar["weather"][0]["description"],
#         "namlik": malumotlar["main"]["humidity"],
#         "shamol": malumotlar["wind"]["speed"]
#     }
#     return ob_havo
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Weather App</title>
# </head>
# <body>
#     <h1>Ob-havo: {{ malumotlar.shahar }}</h1>
#     <p>Harorat: {{ malumotlar.temp }} °C</p>
#     <p>Holati: {{ malumotlar.tavsifi }}</p>
#     <p>Namlik: {{ malumotlar.namlik }}%</p>
#     <p>Shamol: {{ malumotlar.shamol }} m/s</p>
# </body>
# </html>
################################# 2-misol ########################################
# import requests
# key = '181472b3e6c642ccfbdcb1698c57905c'
# city = 'Tashkent'
# URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric'

# response = requests.get(URL)

# if response.status_code == 200:
#     malumotlar = response.json()
#     temperatura = malumotlar['main']['temp']
#     namlik = malumotlar['main']['humidity']
#     ob_havo = malumotlar['weather'][0]['description']
#     shamol_tezligi = malumotlar['wind']['speed']
#     print(f"Ob-havo {city}:")
#     print(f"Temperatura: {temperatura}°C")
#     print(f"Namlik: {namlik}%")
#     print(f"Vaziyat: {ob_havo}")
#     print(f"Shamol tezligi: {shamol_tezligi} m/s")
# else:
#     print("Ma'lumotni olib bo'lmadi:", response.status_code, response.text)
################################# 3-misol ########################################
# import requests
# API_KEY = 'd2da6212bcbc1e8f86884b3d4554e633'  
# BASE_URL = "https://api.themoviedb.org/3"
# def kino_qidirish(query):
#     url = f"{BASE_URL}/search/movie"
#     params = {
#         "api_key": API_KEY,
#         "query": query,  
#         "language": "uz"  
#     }
#     response = requests.get(url, params=params)
#     if response.status_code == 200:
#         return response.json()
#     else:
#         print("Ma'lumotni olishda xatolik yuz berdi:", response.status_code)
#         return None
# kino_data = kino_qidirish("Inception")
# if kino_data:
#     for kino in kino_data['results']:
#         print(f"Film nomi: {kino['title']}")
#         print(f"Qisqacha tavsifi: {kino['overview']}")
#         print(f"Chiqarilgan sana: {kino['release_date']}")
#         print(f"O'rtacha reyting: {kino['vote_average']}")
#         print(f"Kinoning ID raqami: {kino['id']}")
#         print("="*50)
################################# 4-misol ########################################
# import requests
# import random
# API_KEY = 'd2da6212bcbc1e8f86884b3d4554e633' 
# BASE_URL = 'https://api.themoviedb.org/3'
# def get_genres():
#     url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
#     response = requests.get(url)
#     genres = response.json().get('genres', [])
#     return {genre['name'].lower(): genre['id'] for genre in genres}
# def recommend_movie_by_genre(genre_name):
#     genres = get_genres()
#     genre_id = genres.get(genre_name.lower())
#     if not genre_id:
#         return f"'{genre_name}' janri topilmadi. Iltimos, boshqa janr kiriting."
#     url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&language=en-US"
#     response = requests.get(url)
#     movies = response.json().get('results', [])
#     if not movies:
#         return f"'{genre_name}' janrida film topilmadi."
#     movie = random.choice(movies)
#     return f"Tavsiya etilgan film: {movie['title']} \n Tavsifi: {movie.get('overview', 'Tavsif yoq')}"
# if __name__ == "__main__":
#     genre_input = input("Qaysi janrda film ko'rmoqchisiz? (masalan: action, comedy, drama): ")
#     recommendation = recommend_movie_by_genre(genre_input)
#     print("\n" + recommendation)
