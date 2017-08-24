# Forensics: Lost Data

**Link to the challenge is [here](http://www.bugsbunnyctf.me/challenges).**

After downloading the file named file. First I check it's type.

```
	$ file file
	file: data

```

Now after realising that the file type is *unknown*, I pass the file with strings argument.

```
	$ strings file | more

```

In the very first line it shows file.arj which indicates that the file is ARJ Compressed archive file. Refer [this](http://www.garykessler.net/library/file_sigs.html) for file signatures.

Now open the file with hexeditor and replace the initials signature with the actual signature of arj file (60 EA) and save the file with .arj extension.

```
	$ hexeditor file

```

Extract the compressed file and flag will be obvious then.

Flag : Bugs_Bunny{r3m3mb3r_4ll_w4ys_t0_ch3ck_h34d3r_f1l3}

