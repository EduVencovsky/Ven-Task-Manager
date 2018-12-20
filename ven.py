import sys
import re
import validator

def main():
    try:
        validator.call(sys.argv)
    except KeyError as e:
        print(str(e) + " is not a ven command. See 'ven --help'")
    except Exception as e:
        print(e + " error")

if __name__ == "__main__":
    main()