
import random
import string


def random_string(prefix, maxlen):
    # '" "*10'-part is used to raise number of cases
    # when 'space'-char is returned
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def rnd_name_string(prefix, maxlen):
    symbols = string.ascii_letters + "._-"
    return prefix + " " + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
