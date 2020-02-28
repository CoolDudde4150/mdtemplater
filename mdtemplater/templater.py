import argparse
import os
import errno


def make_dirs_to(filename):
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

def _write_header(file, size, header):
    for _ in range(size):
        file.write("#")
    file.write(" " + header)
    file.write("\n")

def write_link(file, link, link_text):
    file.write("[" + link_text + "]")
    file.write("(" + link + ")")
    file.write("\n")

def write_title(file, title):
    _write_header(file, 1, title)

def write_table_of_contents(file):
    file.write("[TOC]\n")

def write_terms_header(file):
    _write_header(file, 2, "Terms")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", metavar="", dest="filename", required=True, type=str, help="Name and path of the file. Generally add the .md suffix. Required")
    parser.add_argument("-t", "--title", metavar="", dest="title", required=True, type=str, help="Title used for the file. Required")
    parser.add_argument("-l", "--link", metavar="", dest="link", type=str, help="The link to the corresponding material")

    args = parser.parse_args()
    
    make_dirs_to(args.filename)
    with open(args.filename, "a+") as f:
        write_title(f, args.title)
        write_table_of_contents(f)
        if args.link:
            write_link(f, args.link, "Corresponding material")
        
if __name__ == "__main__":
    main()