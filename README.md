# RSS-fetch
A python script to fetch rss details from site and storing data in sqlite
<br>

Table of Content
- [RSS-fetch](#rss-fetch)
    - [Installation](#installation)
    - [Run](#run)
      - [Only to fetch rss data](#only-to-fetch-rss-data)
      - [Run web server](#run-web-server)
    - [Usage](#usage)
    - [Warnings](#warnings)
    - [TODO](#todo)

### Installation
1. git clone https://github.com/vedantjain8/rss-fetch.git
2. cd rss-fetch
3. Edit Userdata.yaml to add site for rss fetching
<br>

### Run
#### Only to fetch rss data
`python3 -m main.py`
> This will fetch rss details from all sites listed in Userdata.yaml

   -- OR --

`python3 -m main.py -k <key from Userdata.yaml>`
> This will fetch rss details for the given site

#### Run web server
`python3 -m flask_main.py`
> This will start flask webserver on port 5000
> Visit http://ip:5000/fetch_data this will fetch rss data in background
> *Currently there is none progress bar to check the status
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
- [x] Add unique searching for onyl one site
- [x] Sqlite database to webapp i.e. frontend
- [x] Sort post on latest and oldest
- [x] Lazy loading
- [x] Run webserver while running main.py
- [ ] sort by oldest post is giving me trouble
- [ ] pagination button setup
- [ ] Add parralel searching
- [ ] Add exception for everything
- [ ] Notification
- [ ] Site Name, Maybe you could suggest me somename 