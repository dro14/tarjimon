from urlextract import URLExtract
import re

invalid_url_regex = re.compile(r"\b[ABCDEFGHIJKLMNOPQRSUVWYZabcdefghijklmnopqrsuvwyz][aehou]?\.[A-Za-z]+\b")
invalid_tlds = (".LTD", ".Ltd", ".ltd", ".ga", ".ni", ".li", ".Ma", ".fan", ".To", ".Biz", "kVt.ch", "ni.ma")
extractor = URLExtract()


def extract_urls(s: str) -> tuple[str, list[str]]:
    result = []
    urls = extractor.find_urls(s, check_dns=True)
    urls = sorted(urls, key=lambda x: len(x), reverse=True)
    for url in urls:
        url = url.rstrip(".),-#»”\\?")
        if re.search(invalid_url_regex, url):
            continue
        if url.endswith(invalid_tlds):
            continue
        s = s.replace(url, "URL", 1)
        result.append(url)
    return s, result
