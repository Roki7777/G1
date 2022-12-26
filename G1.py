import random
import sys
import time
def mengetik(s):
   for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()

       time.sleep(random.random() * 0.1)

mengetik('Jangan Lupa Subscribe Chanel User Eror21\nselamat Menonton\nTerima kasih')
