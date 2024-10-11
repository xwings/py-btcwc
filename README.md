# Tiny Bitcoin Wallet Collision Program

Based on ofek's bit library. < 100 lines of code with multiprocessing. Tested againts 31,506,665 wallet address, 1GB csv file. Apple M1 Macbook Pro run 150,000 addresses per second. 

- Python 3.8 and above
- address.csv is a file to store all the public keys
- letsgetrich.txt is a file to store public and private keys 

## How To
```bash
python3 ./btcwc.py
```

50% CPU Utilization
```bash
python3 ./btcwc.py --half
```

Benchmarking 
```bash
python3 ./btcwc.py --debug | pv -i2 -ltr > /dev/null
```

## Database
Build your own bitcoin address database with full bitcoin node. Forked from graymauser's repo, updated to python3.
- https://github.com/xwings/btcposbal2csv
```
python3 btcposbal2csv.py /path/to/your/chainstate /path/to/desired/addresses_with_balance.csv
```

## Credits
- https://github.com/ofek/bit
- https://github.com/vlnahp/Btcbf
- https://github.com/Isaacdelly/Plutus
