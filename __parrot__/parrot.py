#!../bin/python3


class pw:
    '''parrot.pw - password administration

    create_needir: creates needed file structure
    gen: parrot's password generation tool
    TODO: enc: encrypts password with gpg-id
    save: saves encrypted password file
    prompt: prompt for gpg-password
    '''

    def create_needir(name=None):
        ''' create_needir - creates directories as needed

        name:   name of the file (full path)
        '''
        if not name:
            raise ValueError("No filename given. Abort!")
        import os
        dirname = os.path.dirname(name)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
            return "%s created" % (dirname)

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

    def enc(plainpw=None, gpgID=None):
        '''TODO: enc -  encrypts plaintext password with public gpg-key

        plaintextpw:    plaintext password to be encrypted
        gpgID:          public key ID with wich to encrypt the password

        returns a gpg encrypted string
        '''

        ''' TODO:
            pyGPG does not work for python3. Implementing GPG
            through pipes might make the program platform dependend.
            Alternatives?
            Right now, this is a dummy
        '''
        return "Spam, Ham, Eggs and Spam"

    def save(password=None, name=None):
        ''' save - saves the password in a file 'name'.

        password:   string to be saved (should already be encrypted)
        name:       name of the file to save

        Example:    save(password="Spam", name="ham/egg.bacon")
        Return:     file 'egg.bacon' in folder 'ham' containing 'Spam'
        '''
        if not password:
            import getpass
            password = getpass.getpass(prompt="Nothing to save.\n Enter text:")
            if not password:
                raise ValueError("Nothing to save. Abort!")
        if not name:
            name = input("No file name specified.\n Enter filename:")
            if not name:
                raise ValueError("No file name specified. Abort!")
        pw.create_needir(name)    # create the file structure
        storage = open(name, "w")
        storage.writelines(password)
        storage.close()
