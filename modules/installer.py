import os
import modules.subdomain_finder as subdomain_finder

def install():
    os.system('go get -u github.com/tomnomnom/assetfinder')
    os.system('go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest')
    os.system('git clone https://github.com/YashGoti/crtsh.py.git')
    os.chdir('crtsh.py')
    os.system('mv crtsh.py crtsh')
    os.system('chmod +x crtsh')
    os.system('cp crtsh /usr/local/bin/')
    os.system('go install github.com/tomnomnom/httprobe@latest')
    os.system('go install github.com/tomnomnom/meg@latest')
    os.system('go install github.com/lc/gau/v2/cmd/gau@latest')
    os.system('go install github.com/tomnomnom/unfurl@latest')