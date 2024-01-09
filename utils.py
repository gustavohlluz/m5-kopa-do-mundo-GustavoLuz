from datetime import datetime
from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(data: dict):
    if data["titles"] < 0:
        raise NegativeTitlesError()
    
    first_cup_year = int(data["first_cup"].split("-")[0])
    
    if first_cup_year < 1930 or (first_cup_year - 1930) % 4 != 0:
        raise InvalidYearCupError()
    
    current_date = datetime.now()
    current_year = current_date.year
    possible_titles = current_year - first_cup_year

    if (possible_titles // 4) < data["titles"]:
        raise ImpossibleTitlesError()