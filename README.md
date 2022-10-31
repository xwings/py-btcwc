# Tiny Bitcoin Wallet Collision Program

Based on ofek's bit library. 50 lines of code, with multiprocessing. Tested againts 23,205,715 public keys. Apple M1 Macbook pro able to generate and compare around 150,000 key per seconds.

- address.txt is a file to store all the public keys
- letsgetrich.txt is a file to store public and private keys 

## How To
Utilize all CPUs
```bash
python3 ./btcwc.py
```

Utilized half CPUs
```bash
python3 ./btcwc.py half
```

Benchmarking 
```bash
python3 ./btcwc.py debug | pv -i2 -ltr > /dev/null
```

Credit:
- https://github.com/ofek/bit
- https://github.com/vlnahp/Btcbf
- https://github.com/Isaacdelly/Plutus
