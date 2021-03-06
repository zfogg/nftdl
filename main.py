"""grabs all the nft json and image files from a url"""
import os
import pprint
import sys
import requests

pp = pprint.PrettyPrinter(indent=2)

BASE_URL = "https://meebits.larvalabs.com/meebit"


def mkdir_fosho(some_dir):
    """definitely make this dir"""
    if not os.path.exists(some_dir):
        os.mkdir(some_dir)


def download_nft_json_and_img(root_dir, index, url):
    """download nft json and img"""
    json_req = requests.get(url)
    json_blob = json_req.json()
    img_req = requests.get(json_blob['image'])
    with open(f"{root_dir}/json/{index}.json", "wb") as file:
        file.write(json_req.content)
    with open(f"{root_dir}/img/{index}.png", "wb") as file:
        file.write(img_req.content)


def main():
    """download all the json and images for an nft given a url"""
    pwd = sys.path[0]
    mkdir_fosho(f"{pwd}/json")
    mkdir_fosho(f"{pwd}/img")
    # for index in range(1, 5001):
    for i in range(1, 10001):
        url = f"{BASE_URL}/{i}"
        pp.pprint((i, url))
        download_nft_json_and_img(pwd, i, url)


if __name__ == '__main__':
    main()
