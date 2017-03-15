# webdirfuzz
基于爬虫的web目录fuzz工具
![](https://ws1.sinaimg.cn/large/9b7c67c1ly1fdnn9g10cij20vu0gkgmp)
## Feature
- Generate the fuzzing vectors based on crawler results
- Support brute scan mode and could custom stuffix

## Requirement
- python 2.7
- pip

## Install
1. `git clone https://github.com/Fenguopeng/webdirfuzz.git`
2. `cd webdirfuzz`
3. `pip install -r requirement.txt`


## Usage

```
usage: webdirfuzz.py [-h] (-t TARGET | -update) [-thread THREAD]
                     [-d DEPTH | -b] [-e EXT] [-o OUTPUT] [--delay DELAY]
                     [--cookie COOKIE] [--timeout TIMEOUT] [-V]

optional arguments:
  -h, --help                        show this help message and exit
  -t TARGET, --target TARGET        The target site to be scanned
  -update, --update                 Update from github automaticly
  -thread THREAD, --thread THREAD   Max number of concurrent HTTP requests (default 1)
  -d DEPTH, --depth DEPTH           Depth for spider(default 3)
  -b                                Just brute scan, others ignored
  -e EXT, --ext EXT                 Brute scan path extention(default php)
  -o OUTPUT, --output OUTPUT        File to output result(only TXT)
  --delay DELAY                     Delay in seconds between each HTTP request(default 0)
  --cookie COOKIE                   Add Cookie with HTTP request
  --timeout TIMEOUT                 HTTP request timeout(default 5)
  -V, --version                     show program's version number and exit

```    
## Links

