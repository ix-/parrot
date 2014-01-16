#!../bin/python3


class pw:
    '''parrot.pw - password administration

    gen: parrot's password generation tool
    enc: encrypts password with gpg-id
    save: saves encrypted password file
    prompt: prompt for gpg-password
    '''

    def gen(lenght=12, low=True, num=True, punct=True, upp=True):
        '''gen - generates a random string

        lenght:     lenght of the string
        low:        if true, string contains lower case alpha characters
        num:        if true, string contains numerical characters
        punct:      if true, string contains punctuation
        upp:        if true, string contains upper case alphabetical characters

        returns a string with a random combination of
        upper and/or lower case letters, numbers and/or punctuation.
        '''

        pool = []   # pool of characters available for pwd generation
        import random
        import string
        if low:                              # add lower case chars to pool
            pool.append(string.ascii_letters.lower())
        if num:                              # add numerical chars to pool
            pool.append(string.digits)
        if punct:                            # add punctuation chars to pool
            pool.append(string.punctuation)
        if upp:                              # add upper case chars to pool
            pool.append(string.ascii_letters.upper())
        if not len(pool):
            raise ValueError("Pool is empty. Abort!")
        if not lenght:
            import warnings
            warnings.warn("Password is empty!", UserWarning)
        password = [random.choice("".join(pool)) for item in range(lenght)]
        return "".join(password)    # create pwd with 'lenght' char

