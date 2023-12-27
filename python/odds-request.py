import requests

from typing import List
from typing import Any
from dataclasses import dataclass


@dataclass
class OddsValue:
    name: str
    value: float

    @staticmethod
    def from_dict(obj: Any) -> 'OddsValue':
        _name = str(obj.get("name"))
        _value = float(obj.get("value"))
        return OddsValue(_name, _value)


@dataclass
class Odd:
    marketId: int
    marketName: str
    odds: List[OddsValue]

    @staticmethod
    def from_dict(obj: Any) -> 'Odd':
        _marketId = int(obj.get("marketId"))
        _marketName = str(obj.get("marketName"))
        _values = [OddsValue.from_dict(y) for y in obj.get("odds")]
        return Odd(_marketId, _marketName, _values)


@dataclass
class Root:
    bookmakerId: int
    bookmakerName: str
    odds: List[Odd]

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _bookmakerId = int(obj.get("bookmakerId"))
        _bookmakerName = str(obj.get("bookmakerName"))
        _odds = [Odd.from_dict(y) for y in obj.get("odds")]
        return Root(_bookmakerId, _bookmakerName, _odds)


r = requests.get("http://api.sstats.net/odds/1136556?apikey=75kwgw7361l0l1ir")

# Example Usage
# jsonstring = json.loads()
jsonArr = r.json()
root = [Root.from_dict(el) for el in jsonArr]

print("bookies count", root.__len__())

bookieOdds = next((i for i in root if i.bookmakerName == "1xBet"), None)

if bookieOdds is not None:
    print("1xbet odds founded")
    m = next((i for i in bookieOdds.odds if i.marketName == "Match Winner"), None)

    if (m is not None):
        print("Match winner odds")
        print([i.name + ": " + i.value.__str__() for i in m.odds])



