import requests
import urllib.request
from PIL import Image
# import time
def img_file_down():

  nasa_url = "https://api.nasa.gov/planetary/apod?api_key=inze9NLfZ7PgHnPuMaFVIlb3H6uaV5RrYAswCD6n"

  data_from_nasa = requests.get(nasa_url).json()
  # 다운받을 이미지 url
  url = data_from_nasa['url']

  # time check
  # start = time.time()

  # 이미지 요청 및 다운로드
  urllib.request.urlretrieve(url, "test.jpg")

  # 이미지 다운로드 시간 체크
  # print(time.time() - start)

  # 저장 된 이미지 확인
  img = Image.open("test.jpg")
  
  return img

img_file_down()
