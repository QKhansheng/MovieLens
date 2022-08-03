import csv
import utils

def grepMovies(genres, year):
    id_list = list()
    csv_path = utils.utilFilepath("ml-latest-small\movies.csv")
    with open(csv_path, 'r', encoding="utf-8") as csvfile:
        lines = csv.DictReader(csvfile)
        for line in lines:
            if year in line["title"] and genres in line["genres"]:
                id_list.append(line["movieId"])
    return id_list
    # return list(line for line in lines if year in line["title"] and genres in line["genres"])

def getAllgenresAndyears(csv_path):
    gen_all = set()
    years_all = set()
    with open(csv_path, 'r', encoding="utf-8") as csvfile:
        lines = csv.DictReader(csvfile)
        for line in lines:
            for gen in line["genres"].split("|"):
                gen_all.add(gen)
            try:
                year = int(line["title"].split()[-1][1:5])
            except TypeError as type_err:
                pass
            except ValueError as val_err:
                pass
            finally:
                years_all.add(year)
            # years_all.add(line["title"].split()[-1][1:5])
    return sorted(gen_all), sorted(years_all)

if __name__ == '__main__':
    year = "2017"
    genres = "Action"
    id_list = list()
    csv_path = utils.utilFilepath("ml-latest-small\movies.csv")
    with open(csv_path, 'r', encoding="utf-8") as csvfile:
        lines = csv.DictReader(csvfile)
        print(list(line for line in lines if year in line["title"] and genres in line["genres"]))
    print(id_list)