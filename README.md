# Tiny Bitcoin Wallet Collision Program

Based on ofek's bit library. 50 lines of code with multiprocessing. Tested againts 23,205,715 public keys. Apple M1 Macbook pro able to generate and compare around 150,000 key per seconds. 

- Python 3.8 and above
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

## Tips
Build your own bitcoin address database with full bitcoin node current chain state.
- https://github.com/graymauser/btcposbal2csv
```
python btcposbal2csv.py /path/to/your/chainstate /path/to/desired/addresses_with_balance.csv
```


## Credits
- https://github.com/ofek/bit
- https://github.com/vlnahp/Btcbf
- https://github.com/Isaacdelly/Plutus
