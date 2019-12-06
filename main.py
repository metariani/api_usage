author = 'meta riani ananda'
email = 'metarianiananda05@gmail.com'
app_title= 'Menggunakan Python Requests Untuk Memanggil Django API'
print(f'{app_title} oleh {author}')

# Memanggil API di server Django
url = 'http://127.0.0.1:8000/'
import requests

response = requests.get(url)
if response.status_code == 200:
    print ('koneksi berhasil!')
    #panggil API untuk Stats; suhu,humidity dan temperature
    url_api = f' {url}api/v1/Stats/'
    response = requests.get(url_api)
    if response.status_code == 200:

        # ubah json ke python dict
        import json
        data = json.loads(response.text)

    #data terakhir adalah status sensor terakhir.
    data_terakhir = data [len(data) -1]
    suhu = data_terakhir['suhu']
    humidity = data_terakhir['humidity']
    print(f'Hasil pembacaan sensor: suhu={suhu}, humidity={humidity}')