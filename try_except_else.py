# try-except-else-finally.py

def process_file(filename):
    try:
        fi = open(filename, "r")
    except IOError:
        print("oops!, couldn't open {} for reading".format(filename))
        return
    else:
        lines = fi.readlines()
        print("{} has {} lines".format(filename, len(lines)))
    finally:
        print("    Done with file {}".format(filename))

    print(" the first line of {} is:\n{}".format(filename, lines[0]))
    return


process_file("hello.txt")
