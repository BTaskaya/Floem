from floem import Ksilem

ksilem = Ksilem()


def main(args):
    fname = args.pop()
    with open(fname) as f:
        content = f.read()

    result = ksilem.parse(content)
    print(result)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
