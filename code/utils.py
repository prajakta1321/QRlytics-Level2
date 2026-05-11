import re  # import re (regular expression) to validate url format

def is_valid_url(url):   # this function checks whether the given string looks like a valid url or no
    pattern = re.compile(   # define a regular pattern for basic url validation
        r'^(https?:\/\/)?'  # optional http:// or https://
        r'([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,6})'   # domain extension like .cpm, .org
        r'(\/\S*)?$'        # optional path after domain
    )
