import requests

text = input("Masukan text untuk ditulis: ")
get = requests.get(f"https://salism3api.pythonanywhere.com/write?text={text}").json()

print(f"Hasil: {get['images'][0]}")
