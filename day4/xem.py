from zaifapi import *

zaif = ZaifPublicApi()
xem_jpy = zaif.last_price(('xem_jpy'))
print(xem_jpy["last_price"]
      ,"円")
