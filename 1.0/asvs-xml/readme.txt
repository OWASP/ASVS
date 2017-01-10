From: Pekka Sillanpää [mailto:pekka.sillanpaa@nixu.com] 
Sent: Tuesday, December 01, 2009 11:05 AM
To: Boberski, Michael [USA]
Subject: Re: Owasp ASVS two versions


Hello,


Whoops, this took quite a while :) Yes, you may add Nixu to the list of ASVS users.


Finally had some time to play with xslt:s to make the conversion. I might still improve the namespace a bit, but this basically does what we need. Do you have any additional ideas? Now it's just quick and dirty solution to fit into our needs.


I attached few files. If you open the asvs.xml in a browser, you should see how it works. (at least FF does the xslt-conversion). Within the asvs.xsl file you can choose which levels should be included in the "checklist", so only the checks relevant to the specified level(s) are listed. (level_to and level_from params)


To create asvs.xml from the ASVS document:


1. Convert ASVSxxx.doc to ASVSxxx.odt in OpenOffice
2. Unzip content.xml from ASVSxxx.odt
3. xsltproc odt2asvs.xsl content.xml > asvs.xml


Regards,
Pekka
