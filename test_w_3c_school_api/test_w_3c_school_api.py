import requests
import json

def test_w_three_c_school_top_advert():

    url = "https://www.w3cschool.cn/index/topAdvert"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.post(url, headers=headers)
    assert response.status_code == 200
    assert json.loads(response.text)['statusCode'] == 201
    assert json.loads(response.text)['message'] == 'success'

def test_w_three_c_school_check_header():
    url = "https://www.w3cschool.cn/index/checkHeader"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.post(url, headers=headers)
    assert response.status_code == 200
    assert json.loads(response.text)['statusCode'] == '300'
    assert json.loads(response.text)['message'] == '未登陆'
    assert json.loads(response.text)['dotype']['reload'] == 'currentTab'

def test_w_three_c_school_right_float_advert():
    url = "https://www.w3cschool.cn/index/rightFloatAdvert"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.post(url, headers=headers)
    assert response.status_code == 200
    assert json.loads(response.text)['statusCode'] == 400
    assert json.loads(response.text)['message'] == '暂无浮标广告'
    assert json.loads(response.text)['dotype']['reload'] == 'currentTab'

def test_w_three_c_school_index_popup():
    url = "https://www.w3cschool.cn/index/indexPopup"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
    }

    response = requests.post(url, headers=headers)
    assert response.status_code == 200
    assert json.loads(response.text)['statusCode'] == 305
    assert json.loads(response.text)['message'] == 'noconent'
    assert json.loads(response.text)['dotype']['reload'] == 'currentTab'

if __name__ == '__main__':
    test_w_three_c_school_top_advert()
    test_w_three_c_school_check_header()
    test_w_three_c_school_right_float_advert()
    test_w_three_c_school_index_popup()