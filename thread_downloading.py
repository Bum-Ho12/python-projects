import requests
import time, concurrent.futures as fc

images = [

]
start_time = time.perf_counter()

def download_image(image_url):
    img_bytes = requests.get(image_url).content
    image_name = image_url.split('/')[3]
    image_name = f'{image_name}.png'
    with open(image_name,'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{image_name} was downloaded')

    with fc.ThreadPoolExecutor() as threader:
        threader.map(download_image,images)

finish_time = time.perf_counter()

print(f'Finished in {round(finish_time-start_time,2)} second(s)')
