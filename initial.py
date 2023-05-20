import os
import sys
import datetime
import modules.installer as installer
import modules.subdomain_finder as subdomain_finder

#installer.install()

class common():
    filename = sys.argv[0]
    parentDomain = sys.argv[1]

print("""
      =||=  :;\    |: |; ==========  |;     /\      ||               ____
       ||   :; \\   |: |;     ||      |;    /  \\     ||             / ___|  ||   ||
       ||   :;  \\  |: |;     ||      |;   /====\\    ||             \___ \  ||___||
       ||   :;   \\ |: |;     ||      |;  /      \\   ||              ___) | ||   ||
      =||=  :;    \\|: |;     ||      |; /        \\  [[=====]]  (*) |____/  ||   ||
                                    Author: @abhiunix
""")

def time_date():
    time = datetime.datetime.now().strftime("%x %X")
    print("\033[31mScript Started at\033[m", time)
    print("")
time_date()

def creating_target_dir():
    path = "./targets/{}".format(common.parentDomain)
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)
        print("The new directory {} is created!".format(common.parentDomain))
    else:
        print("")
        print("{} Directory already exists, please check".format(common.parentDomain))
        # print("Removing older {} file ".format(common.parentDomain))
        # os.system("rm -r ./targets/{}".format(common.parentDomain))
        # os.makedirs(path)
        # print("The new directory {} is created!".format(common.parentDomain))
creating_target_dir()

def creating_domains_txt():
    directory = "./targets/{}/".format(common.parentDomain)
    filename = "domains.txt"
    file_path = os.path.join(directory, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            pass  # Create an empty file
        print(f"{filename} created in {directory}")
    else:
        print(f"{filename} already exists in {directory}")
creating_domains_txt()

#finding subdomains
subdomain_finder.collect_subdomains_in_domain_txt(common.parentDomain)


