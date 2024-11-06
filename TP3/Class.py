class Film:
    def __init__(self, titre, sortie, note):
        self._titre = titre
        self._sortie = sortie
        self._note = note
        self._avis = []

    @property
    def titre(self):
        return self._titre

    @property
    def sortie(self):
        return self._sortie

    @property
    def note(self):
        return self._note

    @property
    def avis(self):
        return self._avis

    def addavis(self, avis):
        self._avis.append(avis)

    def __str__(self):
        return f"Le film '{self._titre}' est sortie le '{self._sortie}', il a la note de '{self._note}' et voici les avis du public l'ayant vu : \n- " + "\n- ".join(self._avis)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class Bibliotheque:
    def __init__(self):
        self._films = []

    @property
    def films(self):
        return self._films

    def ajouter_film(self, film):
        self._films.append(film)

    def afficher_films(self):
        for film in self._films:
            print(film)

    def mostrate(self):
        return max(self._films, key=lambda film: film.note)

    def top3(self):
        return sorted(self._films, key=lambda film: film.note, reverse=True)[:3]

    def lastmovie(self):
        return max(self._films, key=lambda film: datetime.strptime(film.sortie, "%Y-%m-%d"))

    def avrgnote(self):
        return sum(film.note for film in self._films) / len(self._films)

    def to_json_file(self):
        with open('films.json', 'w') as f:
            json.dump([film.to_json() for film in self._films], f)

    def fromjson(self):
        with open('movies.json', 'r') as f:
            data = json.load(f)
            for film_data in data:
                film = Film(**film_data)
                self.ajouter_film(film)
    
class Bibliotheque:
    def __init__(self):
        self._films = []

    @property
    def films(self):
        return self._films

    def ajouter_film(self, film):
        self._films.append(film)

    def afficher_films(self):
        for film in self._films:
            print(film)

    def mostrate(self):
        return max(self._films, key=lambda film: film.note)

    def top3(self):
        return sorted(self._films, key=lambda film: film.note, reverse=True)[:3]

    def lastmovie(self):
        return max(self._films, key=lambda film: datetime.strptime(film.sortie, "%Y-%m-%d"))

    def avrgnote(self):
        return sum(film.note for film in self._films) / len(self._films)

    def to_json_file(self):
        with open('films.json', 'w') as f:
            json.dump([film.to_json() for film in self._films], f)

    def fromjson(self):
        with open('movies.json', 'r') as f:
            data = json.load(f)
            for film_data in data:
                film = Film(**film_data)
                self.ajouter_film(film)