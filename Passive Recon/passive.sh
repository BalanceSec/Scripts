#Requires a list of ips titled passive_ips.txt
#It runs a whois, dig and outputs to the same file. The last part is a reminder to to do more passive recon

#!/bin/bash

hosts=$(cat passive_ips.txt)

for i in $hosts; do whois "$i" > $i.txt; echo -e "\nDig for $i\n" >> $i.txt; dig $i MX >> $i.txt; echo -e "\n" >> $i.txt; done

echo "don't forget to lookup hosts on dnsdumpster and shodan as well. Happy Hacking!"

#whois $host
