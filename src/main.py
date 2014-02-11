#!../bin/python3

version = 0.1

# Arguments
from class_pw import pw
import argparse
parser = argparse.ArgumentParser()
gen = parser.add_argument_group("gen")
gen.add_argument("gen", nargs="?",
                    help="if set, a new password is generated")
gen.add_argument("name",
                 help="provide the name of the password")
gen.add_argument("-l", "--lenght", dest="lenght",
                    default=12,
                    help="provide the lenght of the password")
gen.add_argument("-L", "--lower", dest="low",
                    nargs="?", default=True,
                    help="if set, lower case characters are omitted")
gen.add_argument("-N", "--numeric", dest="num",
                    nargs="?", default=True,
                    help="if set, numeric characters are omitted")
gen.add_argument("-P", "--punctuation", dest="punct",
                    nargs="?", default=True,
                    help="if set, lower case characters are omitted")
gen.add_argument("-U", "--upper", dest="upp",
                    nargs="?", default=True,
                    help="if set, upper case characters are omitted")

args = parser.parse_args()
if args.gen:
    password = pw.gen(lenght=int(args.lenght),
                      low=bool(args.low), num=bool(args.num),
                      punct=bool(args.punct), upp=bool(args.upp))
    name=str(args.name)
    pw.save(password, name)
    print(" -> ".join((password, name)))
else:
    print("no option given")
