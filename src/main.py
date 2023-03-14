# Used for HTML parsing
from bs4 import BeautifulSoup


# HTTP requests, command-line argument parsing
import requests, argparse


# Initialise argparse and declare arguments
def parse_arguments():
	parser = argparse.ArgumentParser(description='Fetch song lyrics from genius.com')

	# Create mutually exclusive group, so either the name OR the URL can be provided; not both
	group = parser.add_mutually_exclusive_group()
	group.add_argument('--url', '-u', help='URL of the song', nargs=1, default='', required=False)
	group.add_argument('--name', '-n', help='Name of the song prefixed by the name of the artist', nargs=1, default='', required=False)
	args = parser.parse_args()
	return args


# Lyrics exist within seperate 'span' elements within one div
def parse_html(html):
	soup = BeautifulSoup(html, features='html.parser')

	# Find div with lyrics
	div = soup.find_all('div', {'class': 'Lyrics__Container-sc-1ynbvzw-6 YYrds'})

	# Used later to replace '<br>' tags with line breaks
	delimeter = '\n'

	# Used later to return scraped text
	text = []

	# Iterate through the divs scraped
	for i in range(len(div)):

		# Iterate through '<br>' tags in the div
		for line_break in div[i].find_all('br'):

			# Replace '<br>' tags with line breaks
			line_break.replace_with(delimeter)

		# Append the modified text from the div to the list initialised earlier
		text.append(div[i].get_text())

	return text


def make_request(args):

	# Declared for later use
	r = ''

	# If URL provided, make request and parse
	# If name provided, make request and parse
	if args.url != '':
		r = requests.get(args.url[0])
		if r.status_code != 200:
			print("Error:", r.status_code)
			exit()
		r = r.text
		lyrics = parse_html(r)
	elif args.name != '':
		name = args.name[0]
		name = name.replace(' ', '-')
		url = 'https://genius.com/' + name + '-lyrics'
		r = requests.get(url)
		if r.status_code != 200:
			print("Error:", r.status_code)
			exit()
		r = r.text
		lyrics = parse_html(r)
	return lyrics


def main():
	args = parse_arguments()
	lyrics = make_request(args)
	for line in lyrics:
		print(line)


main()
