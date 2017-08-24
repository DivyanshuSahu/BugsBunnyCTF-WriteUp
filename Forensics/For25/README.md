# Forensics: For25

**Link to the challenge is [here](http://www.bugsbunnyctf.me/challenges).**

After downloading the hex file I saw that it is a hex dump of a particular file. Since the hex dump starts and ends with a tag PK (the initials of Phil Katz, the inventor of the zip file), it clearly shows that the above is the hex dump of the zip file.

After removing the initial line numbers and trailing ASCII characters from the original file we left with the hex dump of the zip file.

We convert this hex dump back to zip file from very useful Unix command xxd.

**xxd -r -p hexdump compress.zip**

Now extract the zip file compress.zip and read the flag.

Flag : Bugs_Bunny{Y0u_D1D_1T_W3ll}
