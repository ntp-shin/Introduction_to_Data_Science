import requests
import json
import subprocess
import time

url = 'https://tienphong.vn/api/diemthi/get/result?'

error = open('error.txt', 'w', encoding='utf-8')

#Cum thi = (1, 64) ---> Nên lấy từng cụm thi để tránh bị lỗi
allValue = []
for cum in range(21, 42):
    cumthi = cum
    if cumthi < 10:
        cumthi = '0' + str(cumthi)
    else:
        cumthi = str(cumthi)

    allCum = []
    index = 0
    while True:
        stt = str(index)
        while len(stt) < 4:
            stt = '0' + stt
        sbd = cumthi + stt
        param = {'type': 0, 'keyword': sbd, 'kythi': 'THPT', 'nam': 2022, 'cumthi': 0}
        try:
            # (1) Use requests
            # response = requests.get(url, params=param)
            # response = requests.get('https://tienphong.vn/api/diemthi/get/result?type=0&keyword='+sbd+'&kythi=THPT&nam=2022&cumthi=0')
            # value = json.loads(response.content)
            # (2) Use subprocess
            response = subprocess.check_output('curl "https://tienphong.vn/api/diemthi/get/result?type=0&keyword='+sbd+'&kythi=THPT&nam=2022&cumthi=0"')
            value = json.loads(response.decode('utf-8')) 

            # Choose one of the two methods above
            scores = value['data']['results']
            scores = scores.split('<tr>')

            lst = []
            for point in scores[1:]:
                score = point.replace('<td class="point">', '')
                score = score.replace('<th class="point">1</th>', '')
                score = score.replace('</td>', '')
                score = score.split('\n')

                lstScore = score[2:12]
                if len(lstScore) < 10:
                    continue
                else:
                    lstScore.insert(0, str(cum))
                    # for i in range(0, 10):
                    #     file.write(lstScore[i] + ',')
                    # file.write(lstScore[10] + '\n')
                    lst.insert(0, lstScore)
            if len(lst) > 0:
                allCum += lst
                index += 1
            else:
                break
        except:
            # Write error to file and sleep 5s to reset the connection
            # If it's not ok, should open website ---> F5 to reset the website with keyword = error
            error.write(sbd + '\n')
            print('------------>', sbd)
            time.sleep(5)
            continue
    allValue += allCum

error.close()
file = open('csv.csv', 'w', encoding='utf-8')
for lstScore in allValue:
    for i in range(0, 10):
        file.write(lstScore[i] + ',')
    file.write(lstScore[10] + '\n')