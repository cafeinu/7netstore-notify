from html.parser import HTMLParser
import requests

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag:", tag)

    def handle_data(self, data):
        print("Encountered some data:", data)

if __name__ == '__main__':
    r = requests.get('http://www.google.co.jp')
    print(r.status_code)
    print(r.encoding)
    print(r.headers)
    #print(r.text)
parser = MyHTMLParser()
parser.feed(r.text)