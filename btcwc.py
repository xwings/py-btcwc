import requests, sys
from bit import Key
from multiprocessing import cpu_count, Process

class Btcwc():
    def __init__(self):
        self.debug      = True if len(sys.argv) > 1 and sys.argv[1] == "debug" else False
        self.cpuhalf    = True if len(sys.argv) > 1 and sys.argv[1] == "half" else False
        self.tg_token   = None
        self.tg_chat_id = None
        
    def public_keys(self):
        load_data = open("address.csv", "r").readlines()
        load_data = [x.rstrip() for x in load_data]
        # Remove invalid wallet addresses
        load_data = [x for x in load_data if x.find('wallet') == -1 and len(x) > 0]
        load_data  = dict(zip(load_data, load_data))
        return load_data

    def send_tg_msg(self, text):
        url_req = "https://api.telegram.org/bot" + self.tg_token + "/sendMessage" + "?chat_id=" + self.tg_chat_id + "&text=" + text 
        results = requests.get(url_req)

    def random_brute(self):
        key = Key()
        def report():
            return (f"Found Public Adress: {key.address} Private Key: {key.to_wif()}\n")

        if key.address in self.total_address.keys():
            with open("letsgetrich.txt", "a") as f:
                f.write(report())
            if (self.tg_token and self.tg_chat_id):
                self.send_tg_msg(report())
        elif self.debug is True:
            print(report()) 
            
    def letsroll(self):
        while True:
            self.random_brute()

if __name__ =="__main__":
        bwc = Btcwc()
        cpu_count = cpu_count() // 2 if bwc.cpuhalf is True else cpu_count()
        bwc.total_address = bwc.public_keys()

        print(f"\nTargeting {len(bwc.total_address.keys())} BTC addresses with {cpu_count} processes")
        print(f"Benmarking: python3 {sys.argv[0]} debug | pv -i2 -ltr > /dev/null")
        
        for cpu in range(cpu_count):
            Process(target = bwc.letsroll).start()
