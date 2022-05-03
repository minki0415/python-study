import requests, os
import pandas as pd
from datetime import date, datetime, timedelta
from multiprocessing import Pool
import time


def get_stock(code, startTime=None, endTime=None, type_='day'):
    payload = {"symbol": "005930",
          "requestType": "1",
          "startTime": "20170202",
          "endTime": "20180508",
          "timeframe": "day",}
    ajax_url = "https://api.finance.naver.com/siseJson.naver?"
    head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44"}
    
    payload['symbol']= code 
    payload['endTime'] = datetime.strftime(date.today(), "%Y%m%d")
    payload['startTime'] = str(date.today() - timedelta(days=30)).replace("-", "")
    
    r = requests.post(ajax_url, data=payload, headers= head)
    
    data = eval(" ".join(r.text.strip().split()))
    df = pd.DataFrame(data[1:], columns=data[0])
    
    if os.path.isdir("./stock_data") == False:
        os.mkdir("./stock_data")
    df.to_csv(f"./stock_data/{code}.csv", encoding='utf-8-sig', index=False)

if __name__ == "__main__":
    start = time.time()
    code_list = ["095570","006840","282330","027410","138930","001465","001460","001045","00104K","001040","011155","011150","000590","012030","016610","005830","000995",
                 "000990","139130","001530","000215","001880","000210","37550K","375500","155660","069730","017940","365550","383220","007700","078935","006360","078930","012630","294870",
                 "097230","003560","175330","234080","001065","001067","001060","096760","105560","009070","016385","016380","001390","033180","001940","025000","092230","000040","093050","003555",
                 "034220","003550","051905","051900","373220","032640","011070","066575","066570","051915","051910","079550","010120","000680","006260","001120","023150","035420","181710","338100",
                 "034310","008260","004255","004250","010060","010955","010950","005090","001380","001770","002360","009160","123700","025530","03473K","011790","018670","001745","001740","210980","395400",
                 "034730","402340","361610","096775","096770","001515","001510","28513K","285130","017670","064960","100840","003570","036530","005610","011810","077970","071970","084870","002710","024070","000500",
                 "000860","035250","011420","002100","009450","267290","012320","000050","214390","012610","009140"]
    pool = Pool(processes = 4)
    pool.map(get_stock, code_list)
    get_stock('005930')
    
    print(time.time() - start)