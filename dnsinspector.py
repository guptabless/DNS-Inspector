import dns.resolver
import bcolors
import sys

print("-----------------------------------------------")
print("DNSRecord.py")
print("Code By : NG")
print("Usage: python dnsinspector.py <domain_name>")
print("Give URl without http:// or https://")
print("-----------------------------------------------")

url = sys.argv[1]
print(bcolors.BLUE + '********CNAME Record******')
try:
    cname_user = dns.resolver.query(url, 'CNAME')
    for data in cname_user:
        print(bcolors.PASS)
        print(data)
except :
    print(bcolors.ERRMSG + "CNAME Not found"+ '\n')

#MX record
print(bcolors.BLUE + '************MX Record***********')
try:
    mx_user = dns.resolver.query(url, 'MX')

    for mxdata in mx_user:
        print(bcolors.PASS)
        print(mxdata)
except :
    print(bcolors.ERRMSG + "MX Record Not found"+ '\n')

#A record
print('\n'+ bcolors.BLUE +  '************A Record***************')
try:
    a_user = dns.resolver.query(url, 'A')
    for adata in a_user:
        print(bcolors.PASS)
        print(adata)
except :
    print(bcolors.ERRMSG + "A Record Not found"+ '\n')

# NS record
print('\n'+ bcolors.BLUE + '**********Name Server Record*******')
try:
    ns_user = dns.resolver.query(url, 'NS')
    for nsdata in ns_user:
        print(bcolors.PASS)
        print(nsdata)
except:
    print(bcolors.ERRMSG + "NameServer Record Not found"+ '\n')

print('\n'+ bcolors.BLUE + '*******SPF Record**********')
try:
    spf_user = dns.resolver.query(url, 'SPF')
    for spfdata in spf_user:
        print(bcolors.PASS)
        print(spfdata)
except:
    print(bcolors.ERRMSG + "SPF Record Not found"+ '\n')



