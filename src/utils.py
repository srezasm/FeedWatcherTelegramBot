from time import gmtime, strftime
import regex

# returns current time with feed format
def get_current_time():
    # https://datatracker.ietf.org/doc/html/rfc2822
    return strftime('%a, %d %b %Y %X GMT', gmtime())


# prevents possible errors if the called entry doesn't exist
def get_entry(item, entry_name: str, is_list=False):
    return item[entry_name] if hasattr(item, entry_name) else ([] if is_list else '')


def format_str(self: str, **kwargs: object):
    for key, val in kwargs.items():
        match = regex.search('{.*?' + key + '.*?}', self).group()
        self = self.replace(match, val)
        # print(key + ': ' + val)
    return self
