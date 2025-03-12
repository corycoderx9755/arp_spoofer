import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--access", dest="access_point", help="Specify the access point ip to start spoofing")
    parser.add_argument("-t", "--target", dest="target", help="Specify the target ip to start spoofing")
    options = parser.parse_args()
    if options.access_point and options.target:
        return options
    else:
        parser.error("[-] Please specify the routers ip or target ip you left blank")
        return None
