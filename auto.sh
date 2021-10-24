read -p " Your List Path Here :: " list
clear
for cred in $(cat $list); do echo -n $cred | python3 scrapper.py --url $cred; done
