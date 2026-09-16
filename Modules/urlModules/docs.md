## Python urllib Module — Complete Notes

urllib is Python’s built-in module/package for working with URLs.

Think of it like this:

URL = address of something on the internet
urllib = Python's tools for understanding, creating, encoding, and opening those addresses.

You don't need to install it.

## import urllib

But in practice, we usually use its submodules:

from urllib import request
from urllib import parse
from urllib import error
from urllib import robotparser

## 2. What is urllib?

urllib is a standard library package that provides tools for:

Opening URLs
Sending HTTP requests
Reading web pages
Encoding URL parameters
Parsing URLs
Handling URL-related errors
Working with robots.txt

Basic structure:

urllib
│
## ├── request
## ├── parse
├── error
└── robotparser


urllib.request
Method / Class	What it does	Example
urlopen()	Opens a URL and sends an HTTP request	urlopen("https://example.com")
Request()	Creates a customizable HTTP request	Request(url, headers={...})
urllib.parse
Method	What it does	Example
urlparse()	Breaks a URL into its components	urlparse(url)
urlunparse()	Builds a URL from its components	urlunparse(parts)
urljoin()	Combines a base URL with another URL/path	urljoin(base, path)
quote()	URL-encodes a string	quote("hello world")
unquote()	Decodes a URL-encoded string	unquote("hello%20world")
urlencode()	Converts dictionary data into a query string	urlencode({"name": "Abhi"})
parse_qs()	Converts query string into a dictionary	parse_qs("name=Abhi&age=21")
parse_qsl()	Converts query string into a list of key-value tuples	parse_qsl("name=Abhi&age=21")
urllib.error
Class	What it does	Example
HTTPError	Handles HTTP errors such as 404, 403, 500	except HTTPError as e:
URLError	Handles URL/network-related errors	except URLError as e:
urllib.robotparser
Class / Method	What it does	Example
RobotFileParser()	Creates a parser for robots.txt	rp = RobotFileParser()
set_url()	Sets the robots.txt URL	rp.set_url(url)
read()	Downloads and reads robots.txt	rp.read()
can_fetch()	Checks whether a URL can be fetched according to robots rules	rp.can_fetch("*", url)
parse()	Parses robots.txt lines	rp.parse(lines)
Quick revision
Module	Main purpose	Most important
urllib.request	Send/open HTTP requests	urlopen(), Request()
urllib.parse	Work with URL structure/data	urlparse(), urlencode(), quote(), urljoin()
urllib.error	Handle URL/HTTP errors	HTTPError, URLError
urllib.robotparser	Work with robots.txt	RobotFileParser(), can_fetch()