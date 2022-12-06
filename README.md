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
3. Edit Userdata.yaml to add site for rss fetching
<br>

### Run
`python3 -m main.py`
> This will fetch rss details from all sites listed in Userdata.yaml

   -- OR --

`python3 -m main.py -k <key from Userdata.yaml>`
> This will fetch rss details for the given site

<br>

### Usage
usage: main.py [-h] [-k KEY]

options:
| Key               | Message                         |
| ----------------- | ------------------------------- |
| -h, --help        | Show this help message and exit |
| -k KEY, --Key KEY | Key from Userdata.yaml          |
<br>

### Warnings
1. Some sites might not work
2. It might take a long time if there are many sites
<br>

### TODO
[x] add unique searching for onyl one site

[x] sqlite database to webapp i.e. frontend

[] run webserver while running main.py

[] lazy loading

[] add parralel searching

[] add exception for everything

[] notification