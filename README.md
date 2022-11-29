# RSS-fetch
A python script to fetch rss details from site and storing data in sqlite
<br>

Table of Content
- [RSS-fetch](#rss-fetch)
    - [Installation](#installation)
    - [Run](#run)
    - [Usage](#usage)
    - [Warnings](#warnings)
    - [TODO](#todo)

### Installation
1. git clone https://github.com/vedantjain8/rss-fetch.git
2. cd rss-fetch
3. Edit rss_site.py to add site for rss fetching
<br>

### Run
`python3 -m main.py`
> This will fetch rss details from all sites listed in rss_site

   -- OR --

`python3 -m main.py -k <key from rss_site>`
> This will fetch rss details for the given site

<br>

### Usage
usage: main.py [-h] [-k KEY]

options:
| Key               | Message                         |
| ----------------- | ------------------------------- |
| -h, --help        | Show this help message and exit |
| -k KEY, --Key KEY | Key from rss_site               |
<br>

### Warnings
1. Some sites might not work
2. It might take a long time if there are many sites
<br>

### TODO
~~add unique searching for onyl one site~~
sqlite database to webapp i.e. frontend
add parralel searching