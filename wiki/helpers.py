import re

def normalize_title(title):
    """ title normalization

    >>> normalize_title('human_body')
    'human body'
    >>> normalize_title('humanBody')
    'human body'
    >>> normalize_title('Parts_of_the_HumanBody')
    'parts of the human body'
    >>> normalize_title('HumanBody/Parts')
    'human body / parts'
    >>> normalize_title('HumanBody /Parts')
    'human body / parts'
    """
    title = re.sub(r'[_-]', ' ', title)
    camel = re.compile('([A-Z][A-Z][a-z])|([a-z][A-Z])')
    title = camel.sub(lambda m: m.group()[:1] + " " + m.group()[1:], title)
    title = ' / '.join(map(lambda s: s.strip(), title.split('/')))
    return title.lower()
