from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
	self.page_url = page_url
	self.links = set()
	
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
    def page_links(self): 
        return self.links 
                
    def error(self, message): 
        pass

#this is how you test start tag in example @ the end of episode 5  finder = LinkFinder()
#finder.feed('<html><head><title>Test</title></head>''<body><h1>Parse me!<h1></body></html>')


#2:36 caps are basics now were getting into custom fuctionality and i just want to show you how this works, there is a method in HTML parser thats called handle start tag. this method will
#be called when ever it comes across a start tag. <p> this would be the start tag </p> this would be the end tag. you can use it by default.

