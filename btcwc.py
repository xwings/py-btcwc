import requests, sys
from bit import Key
from multiprocessing import cpu_count, Process
import cupy as cp
import argparse

class Btcwc():
    def __init__(self, debug=False, cpuhalf=False, usegpu = False, addressfile=None, tg_token=None, tg_chat_id=None):
        self.debug      = debug
        self.cpuhalf    = cpuhalf
        self.usegpu    = usegpu
        self.tg_token   = tg_token
        self.tg_chat_id = tg_chat_id
        self.addressfile = addressfile
        
    def public_keys(self, addressfile):
        load_data = open(addressfile, "r").readlines()
        load_data = [x.split(',')[0].rstrip() for x in load_data]
        load_data = dict(zip(load_data, load_data))
        return load_data

    def send_tg_msg(self, text):
        url_req = "https://api.telegram.org/bot" + self.tg_token + "/sendMessage" + "?chat_id=" + self.tg_chat_id + "&text=" + text 
        requests.get(url_req)

    def random_brute(self):
        key = Key()
        def report():
            return (f"Found Public Address: {key.address} Private Key: {key.to_wif()}\n")

        if key.address in self.total_address.keys():
            with open("getaddress.txt", "a") as f:
                f.write(report())
            if (self.tg_token and self.tg_chat_id):
                self.send_tg_msg(report())
        elif self.debug is True:
            print(report()) 
            
    def random_brute_gpu(self):
        while True:
        # Generate random bytes on GPU
            keys_gpu = cp.random.randint(0, 256, size=(10000, 32), dtype=cp.uint8)
            keys = [Key.from_bytes(bytes(key)) for key in cp.asnumpy(keys_gpu)]
            addresses = [key.address for key in keys]
            def report():
                return (f"Found Public Address: {address} Private Key: {key.to_wif()}\n")
            
            for key, address in zip(keys, addresses):
                if address in self.total_address.keys():
                    with open("getaddress.txt", "a") as f:
                        f.write(report())
                    if self.tg_token and self.tg_chat_id:
                        self.send_tg_msg(report())
                elif self.debug:
                    print(report())
            
    def letsroll(self):
        if self.usegpu:
            self.random_brute_gpu()
        else:
            self.random_brute()

if __name__ =="__main__":
        parser = argparse.ArgumentParser(description='BTC Wallet Collision')
        parser.add_argument('--debug', action='store_true', help='Enable debug mode')
        parser.add_argument('--half', action='store_true', help='Use half of the CPU cores')
        parser.add_argument('--usegpu', action='store_true', help='Use GPU cores')
        parser.add_argument('--addressfile', type=str, help='Address file', default='example_address_balance.csv')
        parser.add_argument('--tg_token', type=str, help='Telegram bot token')
        parser.add_argument('--tg_chat_id', type=str, help='Telegram chat ID')

        args = parser.parse_args()

        bwc = Btcwc(debug=args.debug, cpuhalf=args.half, usegpu=args.usegpu, tg_token=args.tg_token, tg_chat_id=args.tg_chat_id)
        cpu_count = cpu_count() // 2 if bwc.cpuhalf else cpu_count()
        bwc.total_address = bwc.public_keys(addressfile=args.addressfile)

        print(f"\nTargeting {len(bwc.total_address.keys())} BTC addresses with {cpu_count} processes")
        print(f"Benmarking: python3 {sys.argv[0]} --debug | pv -i2 -ltr > /dev/null")
        
        for cpu in range(cpu_count):
            Process(target = bwc.letsroll).start()