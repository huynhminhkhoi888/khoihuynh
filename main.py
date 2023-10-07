import os
try:
    from flask import Flask, jsonify, request
    import requests
except:
    os.system('pip install flask')
    os.system('pip install requests')
app = Flask(__name__)

def o2pl(data):
    check_data = data.split(':')
    if len(check_data) == 1:
        email = check_data[0]
        password = None
    elif len(check_data) == 2:
        email = check_data[0]
        password = check_data[1]
    else:
        return {
        'api': 'KhoiHuynh1109', 
        'status': 'error',
        'message': 'Please Check Your Data Again'
        }
    headers = {
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-arch': '""',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'dpr': '1.875',
    'downlink': '2.35',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.135"',
    'sec-ch-ua-bitness': '""',
    'sec-ch-ua-model': '"SM-A037F"',
    'sec-ch-ua-platform': '"Android"',
    'device-memory': '4',
    'rtt': '150',
    'sec-ch-ua-mobile': '?1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'viewport-width': '384',
    'Content-Type': 'application/json;charset=utf-8',
    'Referer': 'https://1login.wp.pl/rejestracja?client_id=o2_poczta_o2_pl_nh&flow=registration&login_challenge=CkYKJDExYWM2NmU0ZTMzN2FlMWQyYTYwYjYzMGYzOTU3MTEwNzIyYxD0hfuoBhoYChJvMl9wb2N6dGFfbzJfcGxfbmgSAnYxEiCxno2lM7y2rb-yVaLWEzWNyBWdg8kBATRX5npIbd__Yw&registrationFlow=newForced&registrationBrand=o2',
    'ect': '4g',
    }

    params = {
    'login_challenge': 'CkYKJDExYWM2NmU0ZTMzN2FlMWQyYTYwYjYzMGYzOTU3MTEwNzIyYxD0hfuoBhoYChJvMl9wb2N6dGFfbzJfcGxfbmgSAnYxEiCxno2lM7y2rb-yVaLWEzWNyBWdg8kBATRX5npIbd__Yw',
    }

    json_data = {
    'birthDate': '',
    'email': email,
    'lastName': '',
    'name': '',
    }
    
    response = requests.post('https://1login.wp.pl/api/v1/public/ol-identity-provider/register/available',params=params,headers=headers,json=json_data,).text
    if '"available":true' in response:
        if password != None:
            return {
            'api': 'KhoiHuynh1109', 
            'status': 'success',
            'message': 'Die',
            'email': email,
            'email:password': email + ':' + password
            }
        else:
            return {
            'api': 'KhoiHuynh1109', 
            'status': 'success',
            'message': 'Die',
            'email': email,
            }
    elif '"available":false' in response:
        if password != None:
            return {
            'api': 'KhoiHuynh1109', 
            'status': 'success',
            'message': 'Live',
            'email': email,
            'email:password': email + ':' + password
            }
        else:
            return {
            'api': 'KhoiHuynh1109', 
            'status': 'success',
            'message': 'Live',
            'email': email,
            }
    else:
        if password != None:
            return {
            'api': 'KhoiHuynh1109', 
            'status': 'success',
            'message': 'Error',
            'email': email,
            'email:password': email + ':' + password
            }
        else:
            return {
            'api': 'KhoiHuynh1109', 
            'status': 'success',
            'message': 'Error',
            'email': email,
            }
@app.route('/o2pl', methods=['GET'])
def get_data():
    key = request.args.get('key')
    data = request.args.get('data')
    if key == None or key == '':
        response_data = {
        'api': 'KhoiHuynh1109', 
        'status': 'error',
        'message': 'Invalid Key!!!',
        }
    else:
        if key.lower() == 'khoideptrai':
            if data == None or data == '':
                response_data = {
                'api': 'KhoiHuynh1109', 
                'status': 'error',
                'message': 'Invalid Data!!!',
                }
            else:
                response_data = o2pl(data)
        else:
            response_data = {
            'api': 'KhoiHuynh1109', 
            'status': 'error',
            'message': 'Wrong Key!!!'
            }
    
    import json


    #compact_json = json.dumps(data, separators=(',', ':'))
    #print(compact_json)
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
