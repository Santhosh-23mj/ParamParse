# ParamParse

A python script that opens the output of ParamSpider and prints out the parameters.

```
Usage:
python3 paramparse.py -f /paramspideroutput.txt
```
Output:
```
###########################################################
               ParamSpider Output Parser
    Parse the ParamSpider output and make simple files
###########################################################

---------------------------------------
       PARAMETER COUNT STATS      
---------------------------------------
PARAMETER            COUNT               
----------           -------             
t                    344                 
utm_source           121                 
ver                  116                 
v                    49                  
utm_campaign         16                  
page                 16                  
hs_amp               14                  
id                   13                  
_v                   13                  
hsFormKey            11                               
__ws                 10                  
p                    6                   
C                    6                   
preview              5                   
dlp                  4                   
q                    4                   
action               4                   
kid                  4                   
page_id              3                   
utm_content          3                                 
url                  2                   
_                    2                   
ref                  2                                      
mkt_tok              2                   
utm_medium           2                   
u                    2                   
author               1                   
target               1                   
file                 1                   
post_type            1                   
?utm_source          1                   
portalId             1                   
redirect_to          1                   
product              1                   
fbclid               1                   
paged                1                   
display_custom_css   1                   
tag                  1                   
feed                 1                   
site                 1                   
m                    1                   
cat                  1                   
search               1                   
width                1                   
route                1                   
mcsf_action          1                   
s                    1                   
family               1                   
---------------------------------------
[+] Total unique parameters       :  48
```

You could create seperate files in the name of parameters, using the -s switch.
Each file contains the list of URLs that had the parameter.
This might be useful when the no.of URLs in the output file are more.
