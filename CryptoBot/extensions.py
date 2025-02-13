import requests
import json
from CryptoBot.config import keys

class APIException(Exception):
    pass



class CryptoConvertor:

     @staticmethod
     def get_price(quote: str, base:str, amount:str):
         if quote == base:
             raise ConversionException(f'Невозможно пересети одинаковые валюты {base}')

         try:
             quote_ticker = keys[quote.upper()]
         except KeyError:
             raise ConversionException(f'Не удалось обработать валюту {quote}')

         try:
             base_ticker = keys[base.upper()]
         except KeyError:
             raise ConversionException(f'Не удалось обработать валюту {base}')

         try:
             amount = float(amount)
         except ValueError:
             raise ConversionException(f'Не удалось обработать количество {amount}')


         r = requests.get(f'http://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')

         total_base = json.loads(r.content)[keys[base]]
         return total_base
