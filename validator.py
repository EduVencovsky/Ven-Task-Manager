func = {
    "init": [
        "--y"
    ]
}

def init(params):
    print(params)

def call(argv):
    method = ""
    options = []
    arguments = []
    if func[argv[1]]:
        print("method found is " + argv[1])
        method = argv[1]
    else:
        raise KeyError(argv[1])
    
    for arg in argv[2:]:
        if arg[:2] == "--":
            print(arg)
            options.append(arg)
        else:
            arguments = arg

    print(method)
    print(options)
    print(arguments)