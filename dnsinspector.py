import dns.resolver
import bcolors
import sys, argparse

def banner():
    print(""" 
        
██████╗░███╗░░██╗░██████╗░░░░░░██╗███╗░░██╗░██████╗██████╗░███████╗░█████╗░████████╗░█████╗░██████╗░
██╔══██╗████╗░██║██╔════╝░░░░░░██║████╗░██║██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██║██╔██╗██║╚█████╗░█████╗██║██╔██╗██║╚█████╗░██████╔╝█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
██║░░██║██║╚████║░╚═══██╗╚════╝██║██║╚████║░╚═══██╗██╔═══╝░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
██████╔╝██║░╚███║██████╔╝░░░░░░██║██║░╚███║██████╔╝██║░░░░░███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚══╝╚═════╝░░░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░░░░╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                                                                 Coded BY NG              
          """)
if len(sys.argv)>1:
    banner()
    if(sys.argv[1] == '-d'):
     try:
        url = sys.argv[2]
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", required=True)
        args = parser.parse_args()

        print(bcolors.BLUE + '********CNAME Record******')
        try:
                cname_user = dns.resolver.query(url, 'CNAME')
                for data in cname_user:
                    print(bcolors.PASS)
        except:
                print(bcolors.ERRMSG + "CNAME Not found"+ '\n')

 # MX record
        print(bcolors.BLUE + '************MX Record***********')
        try:
            mx_user = dns.resolver.query(url, 'MX')
            for mxdata in mx_user:
                print(bcolors.PASS)
                print(mxdata)
        except:
            print(bcolors.ERRMSG + "MX Record Not found" + '\n')

# A record
        print('\n' + bcolors.BLUE + '************A Record***************')
        try:
            a_user = dns.resolver.query(url, 'A')
            for adata in a_user:
                print(bcolors.PASS)
                print(adata)
        except:
            print(bcolors.ERRMSG + "A Record Not found" + '\n')

# NS record
        print('\n' + bcolors.BLUE + '**********Name Server Record*******')
        try:
            ns_user = dns.resolver.query(url, 'NS')
            for nsdata in ns_user:
                print(bcolors.PASS)
                print(nsdata)
        except:
            print(bcolors.ERRMSG + "NameServer Record Not found" + '\n')

#SPF
        print('\n' + bcolors.BLUE + '*******SPF Record**********')
        try:
            spf_user = dns.resolver.query(url, 'SPF')
            for spfdata in spf_user:
                print(bcolors.PASS)
                print(spfdata)
        except:
            print(bcolors.ERRMSG + "SPF Record Not found" + '\n')

     except:
         print('Please enter python dnsrecord.py -d <valid damin name>')
    elif ((sys.argv[1] == '-h')|(sys.argv[1] == '--help')):
          print(bcolors.BOLD + 'usage: DNSRecord.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
              'show this help message and exit' '\n''-d Domain,   --domain Domain')
else:
     banner()
     print(bcolors.ERR+ 'Please select atleast 1 option from -d or -h, with a valid domain name')

