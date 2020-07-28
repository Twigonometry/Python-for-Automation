base_url = "http://api.openweathermap.org/data/2.5/forecast"
parameters = {'APPID':'','q':'Seattle,US'}
response = requests.get(base_url, params=parameters)#not bothering with an account
print(response.content)