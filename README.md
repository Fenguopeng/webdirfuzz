# webdirfuzz
基于爬虫的web目录fuzz工具
![](https://ws1.sinaimg.cn/large/9b7c67c1ly1fdfoqhqtz7j20o90gfq3w)
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
    usage: webdirfuzz.py [-h] [-t THREAD] [-d DEPTH] [-b] [-e EXT] [-o OUTPUT]
     [--delay DELAY] [--timeout TIMEOUT] [-V] target
    
    positional arguments:
      target	The target site to be scanned
    
    optional arguments:
      -h, --help	show this help message and exit
      -t THREAD, --thread THREAD Max number of concurrent HTTP requests (default 1)
      -d DEPTH, --depth DEPTH depth for spider(default 3)
      -b just brute scan, others ignored
      -e EXT, --ext EXT brute scan path extention(default php)
      -o OUTPUT, --output OUTPUT File to output result(only TXT)
      --delay DELAY Delay in seconds between each HTTP request(default 0)
      --timeout TIMEOUT HTTP request timeout(default 5)
      -V, --version show program's version number and exit
```    
## Links

