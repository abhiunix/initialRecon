import os
import subprocess
import time

def collect_subdomains_in_domain_txt(parentDomain):
    global file1
    file1 = open("./targets/{}/domains.txt".format(parentDomain), "a")
    collect_subdomains(file1, parentDomain)
    number_of_subdomains(parentDomain)

def number_of_subdomains(parentDomain):
    file_path = './targets/{}/domains.txt'.format(parentDomain)
    line_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line_count += 1
    print(f"Number of Subdomains found: {line_count}")

def collect_subdomains(file1, parentDomain):
    print("\033[31m\033[m")
    print("\033[31mStarting initial phase\033[m")
    print("\033[31m\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")
    # number_of_subdomains(parentDomain)
    time.sleep(2.5)
    print("\033[31mStarting subdomain enumeration with assetfinder:\033[m")
    domains=subprocess.check_output(["assetfinder", parentDomain]).decode()
    file1.writelines(domains)
    print("\033[31mDone with assetfinder. File saved to domains\033[m")
    print("\033[31m\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")
    time.sleep(2.5)
    number_of_subdomains(parentDomain)

    print("\033[31mStarting subdomain enumeration with subfinder:\033[m")
    domains=subprocess.check_output(["subfinder", "-silent", "-d", parentDomain]).decode()
    file1.writelines(domains)
    print("\033[31mDone with subfinder. File saved/appended to domains\033[m")
    print("\033[31m\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")

    number_of_subdomains(parentDomain)

    print("\033[31mStarting subdomain enumeration with findomain:\033[m")
    domains=subprocess.check_output(["findomain", "-q", "-t", parentDomain]).decode()
    file1.writelines(domains)
    print("\033[31mDone with findomain. File saved/appended to domains\033[m")
    print("\033[31m\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")

    number_of_subdomains(parentDomain)

    print("\033[31mStarting subdomain enumeration with crtsh:\033[m")
    domains=subprocess.check_output(["crtsh", "-d", parentDomain]).decode()
    file1.writelines(domains)
    print("\033[31mDone with crtsh. File saved/appended to domains\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")
    print("\033[31m\033[m")

    number_of_subdomains(parentDomain)

    print("\033[31mStarting subdomain enumeration with waybackurls:\033[m")
    domains=subprocess.check_output(["waybackurls", parentDomain, "|", "unfurl", "--unique", "domains"]).decode()
    file1.writelines(domains)
    # os.system(f"waybackurls {parentDomain} | unfurl --unique domains >> domains")
    print("\033[31mDone with waybackurls. File saved/appended to domains\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")
    print("\033[31m\033[m")

    print("\033[31mSorting..\033[m")
    os.system("cat domains | sort | uniq > uniq.domains")
    print("\033[31mFile saved to uniq.domains.\033[m")
    print("\033[31m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>\033[m")
    print("\033[31m \033[m")
