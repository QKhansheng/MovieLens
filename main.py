import preLoadcsv
import utils
import connDB

if __name__ == '__main__':
    genres, years = preLoadcsv.getAllgenresAndyears(utils.utilFilepath("ml-latest-small\movies.csv"))
    i = 1
    gen_label = "Genres:"
    year_label = "year:"
    #help some to choose a movie
    print("______Movies' Pannel______")
    for gen in genres:
        fmt = "{}{}".format(gen, "| ")
        gen_label += fmt
    print(gen_label)
    for year in years:
        fmt = "{}{}".format(year, "| ")
        year_label += fmt
    print(year_label)
    print("Sorted by: Rating| Datetime| Number of comments")
    choose_genres = input("Please choose a Genre:")
    choose_year = input("Please choose a year:")
    id_list = preLoadcsv.grepMovies(choose_genres, choose_year)
    for movie_id in id_list:
        result = connDB.select_movies(movie_id)
        print(result.fetchall())







