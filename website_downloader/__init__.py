import requests,os
from bs4 import BeautifulSoup
import urllib.parse

class WebsiteDownloaderError:
    class RequestError(Exception):
        pass
    class IoError(Exception):
        pass
    class UrlParseError(Exception):
        pass
    class SelectorParseError(Exception):
        pass

def save_website(url:str,directory:str):
    client = requests.Session()
    client.headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; rv:124.0) Gecko/20100101 Firefox/124.0"}
    try:
        res = client.get(url)
        body = res.text
    except Exception as e:
        raise WebsiteDownloaderError.RequestError(e)
    try:
        os.mkdir(directory)
        os.mkdir(os.path.join(directory, "videos"))
    except Exception as e:
        raise WebsiteDownloaderError.IoError(e)
    for sub_dir in ["css","js","img"]:
        try:
            os.mkdir(os.path.join(directory, sub_dir))
        except Exception as e:
            raise WebsiteDownloaderError.IoError(e)
    soup = BeautifulSoup(body, "html.parser")
    replacements = []
    for selector in ["link[rel='stylesheet']", "script[src]", "img[src]"]:
        try:
            elements = soup.select(selector)
        except Exception as e:
            raise WebsiteDownloaderError.SelectorParseError(e)
        for element in elements:
            attr = "href" if "link" in selector else "src"
            if element.get(attr) != None:
                href = element.get(attr)
                try:
                    resolved_url = urllib.parse.urljoin(url,href)
                except Exception as e:
                    raise WebsiteDownloaderError.UrlParseError(e)
                try:
                    content = client.get(resolved_url).content
                except Exception as e:
                    raise WebsiteDownloaderError.RequestError(e)
                file_name = resolved_url.split("/")[-1].split("?")[0] or "index.html"
                sub_directory = "css" if element.name=="link" else "js" if element.name=="script" else "img"
                try:
                    open(os.path.join(directory,sub_directory,file_name),"wb").write(content)
                except Exception as e:
                    raise WebsiteDownloaderError.IoError(e)
                relative_path = "{}/{}".format(sub_directory,file_name.split("?")[0])
                replacements.append((href,relative_path))
    video_selector = "video[src], source[src]"
    try:
        video_elements = soup.select(video_selector)
    except Exception as e:
        raise WebsiteDownloaderError.SelectorParseError(e)
    for element in video_elements:
        if element.get("src") != None:
            src = element.get("src")
            try:
                resolved_url = urllib.parse.urljoin(url, src)
            except Exception as e:
                raise WebsiteDownloaderError.UrlParseError(e)
            try:
                content = client.get(resolved_url).content
            except Exception as e:
                raise WebsiteDownloaderError.RequestError(e)
            file_name = resolved_url.split("/")[-1].split("?")[0] or "video.mp4"
            file_path = os.path.join(directory,"videos",file_name)
            open(os.path.join(directory,"videos",file_name),"wb").write(content)
            relative_path = "{}/{}".format(sub_directory,file_name)
            replacements.append((src,relative_path))
    for (original,replacement) in replacements:
        body = body.replace(original,replacement)
    try:
        open(os.path.join(directory,"index.html"),"w").write(body)
    except Exception as e:
        raise WebsiteDownloaderError.IoError(e)
