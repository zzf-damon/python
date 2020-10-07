import requests



url = "http://222.197.219.6:8080/cclzc/search?tgt=1&src=0&zh=我要煮一碗酸汤。&xyz=Tôi sẽ nấu canh chua.&data_xh=10506201&ywzql=&zh_update=我要煮一碗酸汤。&updatexyz=Tôi sẽ nấu canh chua."

cookies = {
"JSESSIONID": "2DB62252AB4FA3D0CF2A259105FBFEA7"
}


response = requests.get(url,cookies=cookies).text

print(response)
