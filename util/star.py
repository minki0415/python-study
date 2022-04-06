import requests

def search_star(addr):
    url= 'https://www.starbucks.co.kr/store/getStore.do?r=804IUG79N7'
    payload = {
        'in_biz_cds' : '0',
        'in_scodes' : '0',
        'ins_lat' : '37.5627128',
        'ins_lng' : '126.93279869999999',
        'search_text' : '',
        'p_sido_cd' : '01',
        'p_gugun_cd' : '',
        'in_distance' : '0',
        'in_biz_cd' : '',
        'isError' : 'true',
        'searchType' : 'C',
        'set_date' : '',
        'all_store' : '0',
        'T03' : '0',
        'T01' : '0',
        'T12' : '0',
        'T09' : '0',
        'T30' : '0',
        'T05' : '0',
        'T22' : '0',
        'T21' : '0',
        'T10' : '0',
        'T36' : '0',
        'P10' : '0',
        'P50' : '0',
        'P20' : '0',
        'P60' : '0',
        'P30' : '0',
        'P70' : '0',
        'P40' : '0',
        'P80' : '0',
        'whcroad_yn' : '0',
        'P90' : '0',
        'new_bool' : '0',
        'iend' : '1000',
        'rndCod' : 'V8UNZFKU44',}

    r = requests.post(url, data=payload)
    return [x['addr'] for x in r.json()['list'] if x['addr'].find(addr) > -1]

def starbucks():
    url= 'https://www.starbucks.co.kr/store/getStore.do?r=804IUG79N7'
    payload = {
        'in_biz_cds' : '0',
        'in_scodes' : '0',
        'ins_lat' : '37.5627128',
        'ins_lng' : '126.93279869999999',
        'search_text' : '',
        'p_sido_cd' : '01',
        'p_gugun_cd' : '',
        'in_distance' : '0',
        'in_biz_cd' : '',
        'isError' : 'true',
        'searchType' : 'C',
        'set_date' : '',
        'all_store' : '0',
        'T03' : '0',
        'T01' : '0',
        'T12' : '0',
        'T09' : '0',
        'T30' : '0',
        'T05' : '0',
        'T22' : '0',
        'T21' : '0',
        'T10' : '0',
        'T36' : '0',
        'P10' : '0',
        'P50' : '0',
        'P20' : '0',
        'P60' : '0',
        'P30' : '0',
        'P70' : '0',
        'P40' : '0',
        'P80' : '0',
        'whcroad_yn' : '0',
        'P90' : '0',
        'new_bool' : '0',
        'iend' : '1000',
        'rndCod' : 'V8UNZFKU44',}

    r = requests.post(url, data=payload)
    rt_dict = r.json()
    
    return rt_dict
