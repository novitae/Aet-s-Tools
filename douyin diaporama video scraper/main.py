from argparse import ArgumentParser
from re import match
import requests
from os import path
from tqdm import tqdm

class UrlNotMatchingError(Exception): pass
class APIFetchingError(Exception): pass

def _getApiResp(url) -> dict:
    resp = requests.get(url, headers={
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    }, allow_redirects=False)
    if resp.status_code == 302:
        loc = resp.headers.get("Location")
        vid = loc.split("/")[-2]
        api = requests.get(f"https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={vid}", headers={
            "Host": "www.iesdouyin.com",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
            "Referer": loc,
            "Accept-Language": "fr-FR,fr;q=0.9",
            "X-Requested-With": "XMLHttpRequest"
        })
        return api.json()
    raise APIFetchingError(f"{url} responded {resp.status_code}.")

def _checkUrlFormat(url) -> str:
    if match(r"https:\/\/v\.douyin\.com\/[A-Za-z0-9]{6,8}\/", url):
        return url
    raise UrlNotMatchingError(f"""{url} doesn't match r"https:\/\/v\.douyin\.com\/[A-Za-z0-9]{{6,8}}\/\"""")

def _parseResp(j) -> list:
    retour = []
    uid = j["item_list"][0]["author"]["unique_id"]
    for x, imgnfo in enumerate(j["item_list"][0]["images"]):
        retour.append({f"{uid}_{x}.webp":imgnfo["url_list"][0]})
    return retour

def _getPicBinary(url) -> bytes:
    host = url.split("//")[-1].split("/")[0]
    image = requests.get(url, headers = {
        "Accept": "image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Host": host,
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        "Accept-Language": "fr-FR,fr;q=0.9",
        "Referer": "https://www.iesdouyin.com/",
        "Connection": "keep-alive"
    })
    return image.content

def main() -> None:
    p = ArgumentParser()
    p.add_argument("url", help="The url of the video to download")
    p.add_argument("-p","--path", help="Path to export the images")
    a = p.parse_args()

    url = _checkUrlFormat(url=a.url)
    pth = a.path if a.path else path.dirname(__file__)

    j = _getApiResp(url=url)
    pics = _parseResp(j=j)
    for name, picurl in tqdm([tuple(p.items())[0] for p in pics]):
        open(path.join(pth, name),"wb").write(_getPicBinary(picurl))

if __name__ == "__main__":
    main()
