import requests

url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
params ={'serviceKey' : '서비스키', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'stnId' : '108', 'tmFc' : '201310170600' }

response = requests.get(url, params=params)
print(response.content)