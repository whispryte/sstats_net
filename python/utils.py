# glicko 2
def get_win_probability(rating1: int, rd1: int, rating2: int, rd2: int) -> float:
    """
    Возвращает вероятность победы команды с rating1 и rd1
    :param rating1: Рейтинг 1ой команды (например 1600)
    :param rd1: Отклонение рейтинга 1ой команды (например 350)
    :param rating2: Рейтинг 2ой команды (например 1600)
    :param rd2: Отклонение рейтинга 2ой команды (например 350)
    :return: вероятность победы 1ой команды
    """
    gp = 0.00001007239860196398
    gf = lambda rd: 1 / math.sqrt(1 + gp * math.pow(rd, 2))
    return 1 / (1 + math.pow(10, (-(rating1 - rating2) * gf(math.sqrt(math.pow(rd1, 2) + math.pow(rd2, 2))) / 400)))


def standard_winning_expectancy(rating1: int, rating2: int):
    return 1 / (1 + math.pow(10, -(rating1 - rating2 + 10) / 400))