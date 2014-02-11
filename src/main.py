#!../bin/python3

from class_pw import pw
#load config file
config = {}
exec(open("config.py").read(), config)

# Arguments
import argparse
parser = argparse.ArgumentParser()
gen = parser.add_argument_group("gen")               # arguments related to pw-generation
gen.add_argument("gen", nargs="?",
                    help="if set, a new password is generated")
gen.add_argument("name",                            # name of the pw
                 help="provide the name of the password")
gen.add_argument("-l", "--lenght", dest="lenght",
                    default=12,                     # lenght of the pw
                    help="provide the lenght of the password")
gen.add_argument("-L", "--lower", dest="low",       # omitting lower case characters
                    nargs="?", default=True,
                    help="if set, lower case characters are omitted")
gen.add_argument("-N", "--numeric", dest="num",     # omitting numeric characters
                    nargs="?", default=True,
                    help="if set, numeric characters are omitted")
gen.add_argument("-P", "--punctuation", dest="punct", # omitting punctuation
                    nargs="?", default=True,
                    help="if set, punctuation is omitted")
gen.add_argument("-U", "--upper", dest="upp",       # omitting upper case characters
                    nargs="?", default=True,
                    help="if set, upper case characters are omitted")

args = parser.parse_args()  #store the arguments
if args.gen:                #if arg gen is given, generate pw with the options:
    password = pw.gen(lenght=int(args.lenght),  # - lenght of the pw
                      low=bool(args.low),       # - omit lower case characters
                      num=bool(args.num),       # - omit numeric characters,
                      punct=bool(args.punct),   # - omit punctuation
                      upp=bool(args.upp))       # - omit upper case characters
<<<<<<< HEAD
    name=str("".join((config.get('home'), args.name))) # name and file structure ...
=======
    name=str("/".join((config.get('home'), args.name))) # name and file structure ...
>>>>>>> 071976601717a1e81a95c65adc31a49ed38ad9b0
    pw.save(password, name)                     # ...to save pw to
    print(" -> ".join((password, name)))        # and print to stdout
else:
    print("no option given")
