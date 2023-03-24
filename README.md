# pylyrics


## Description

Simple web-scraping tool that interacts with [Genius Lyrics](https://genius.com/) to fetch song lyrics by name or URL.

Written in Python.


## Compiling

Ensure that `python3` and `pip` are installed.

Then, simply install required packages:

```
pip3 install -r requirements.txt
```


## Usage

```
python3 src/main.py --help
python3 src/main.py <url> OR <name>
./main <url> OR <name>
```

- url **OPTIONAL**: The URL of the server where requests are sent
- name **OPTIONAL**: The name of the song, following Genius Lyrics format. The song name must be prefixed by the **full name** of the artist. See below for examples.

Lyrics to Ariana Grande's "thank u, next", can be fetched in two ways:

```
python3 src/main.py --url https://genius.com/Ariana-grande-thank-u-next-lyrics

# OR

python3 src/main.py --name "ariana grande thank u next"
```

Note that the `--url` and `--name` parameters are mutually exclusive, therefore both cannot be included when running the program.
