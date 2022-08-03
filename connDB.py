import pandas
import pymysql
from sqlalchemy import create_engine
import utils

def conndb():
    engine = create_engine("mysql+pymysql://root@127.0.0.1:3306/test", max_overflow=5)
    return engine

def select_movies(id):
    conn = conndb()
    result = conn.execute("select * from movies where movieId = {}".format(id))
    return result

def loadCsvtodb():
    moviesCsvPath = utils.utilFilepath("ml-latest-small\movies.csv")
    ratingsCsvPath = utils.utilFilepath("ml-latest-small\ratings.csv")
    linksCsvPath = utils.utilFilepath("ml-latest-small\links.csv")
    tagsCsvPath = utils.utilFilepath("ml-latest-small\tags.csv")

    movies = pandas.read_csv(moviesCsvPath)
    ratings = pandas.read_csv(ratingsCsvPath)
    links = pandas.read_csv(linksCsvPath)
    tags = pandas.read_csv(tagsCsvPath)

    movies.to_sql('movies', conndb(), if_exists='append', index=False)
    ratings.to_sql('ratings', conndb(), if_exists='append', index=False)
    links.to_sql('links', conndb(), if_exists='append', index=False)
    tags.to_sql('tags', conndb(), if_exists='append', index=False)

if __name__ == '__main__':
    print()

