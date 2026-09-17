import math


# Этап 1
def average_rating(movies):
    summ = 0
    for movie in movies:
        summ += movie['rating']

    return round(summ / len(movies), 1)

def catalog_age_stats(movies, current_year=2026):
    age = []
    for movie in movies:
        age.append(current_year - movie['year'])

    return (max(age), min(age), math.ceil(sum(age) / len(age)))

def duration_in_hours(minutes):
    hour = minutes // 60
    minutes_new = minutes % 60
    return f'{hour}ч {minutes_new}м'

# Этап 2
def rating_tier(rating):
    if rating >= 9:
        rate = "шедевр"
    elif rating >= 7:
        rate = "хорошо"
    elif rating >= 5:
        rate = "средне" if rating != 5 else "норм"
    else:
        rate = "слабо"

    return rate

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

# Этап 3
def no_movies_genres(movies, genres='comedy'):
    print(f'\nФильмы не {genres}:')
    for movie in movies:
        if genres in movie['genres']:
            continue
        print('\t', movie['title'])

def movie_find_rating(movies, rate=9.0):
    i = 0
    while i < len(movies):
        if movies[i]['rating'] > rate:
            print(
                f"Фильм шедевр - {movies[i]['title']}, "
                f"рейтинг - {movies[i]['rating']}"
            )
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    count = 0
    for movie in movies:
        if movie['duration_min'] > threshold:
            count += 1
    return count

# Этап 4
def normalize_title(title):
    title_split = title.split()
    return " ".join(t[0].upper() + t[1:] for t in title_split)

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    genrer_list = sorted([i for i in movie['genres']])
    genres_str = ''
    for i in genrer_list:
        genres_str += ' ' + i
    return (
        f'"{movie["title"]}" ({movie["year"]}) - '
        f'{movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, '
        f'жанры:{genres_str}')

# Этап 5
def titles_sorted_by_rating(movies):
    result = []
    for movie in sorted(movies, key=lambda m: m['rating'], reverse=True):
        result.append(movie['title'])

    return result

def top_n_by_rating(movies, n=3):
    result = sorted(movies, key=lambda m: (-m["rating"], m["title"]))
    return [(m["title"], m["rating"]) for m in result[:n]]

# Этап 6
def count_by_genre(movies):
    dict_count = {}
    for movie in movies:
        for g in movie['genres']:
            dict_count[g] = dict_count.get(g, 0) + 1

    return dict_count

def actor_filmography(movies):
    result = {}
    for movie in movies:
        for actor in movie["actors"]:
            result.setdefault(actor, []).append(movie["title"])
    return result

def high_rating(movies):
    avg = average_rating(movies)
    return {m['title']: m['rating'] for m in movies if m['rating'] > avg}

# Этап 7
def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= movie['genres']
    return genres

def common_actors(movie1, movie2):
    return set(movie1['actors']) & set(movie2['actors'])

def genres_only_in_one(movies_a, movies_b):
    genres_a, genres_b = set(), set()
    for movie in movies_a:
        genres_a |= movie['genres']
    for movie in movies_b:
        genres_b |= movie['genres']
    return genres_a - genres_b

# Этап 8
def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie['rating'] >= min_rating:
            yield movie

def sum_duration_min(movies, min_rating=7.0):
    return sum(m["duration_min"] for m in movies if m["rating"] > min_rating)
    
def build_report(movies):
    print('ОТЧеТ ПО КАТАЛОГУ')
    print('Средний рейтинг:', average_rating(movies))
    print('Средний возраст фильмов:', catalog_age_stats(movies)[2], 'лет')

    print('\nТоп-3 фильма:')
    for t, r in top_n_by_rating(movies):
        movie = next(m for m in movies if m['title'] == t)
        print('  ', format_report_line(movie))

    print('\nФильмов по жанрам:')
    for g, c in sorted(count_by_genre(movies).items(), key=lambda x: -x[1]):
        print(f'  {g} - {c}')

    print('\nВсе жанры каталога:', ', '.join(sorted(all_genres(movies))))