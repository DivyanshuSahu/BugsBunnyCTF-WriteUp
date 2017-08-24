# Forensics: UNKOWN FILE

**Link to the challenge is [here](http://www.bugsbunnyctf.me/challenges).**

After downloading the file named UNKOWN. First I check it's type.

```
    $ file file
    file: data

```

Now after realising that the file type is *unknown*, I pass the file with strings argument but it didn't help.

```
    $ strings file | more

```

Now I pass the file with xxd command.

```
    $ xxd UNKWON

```

At last line, we saw the word GNP which is the reverse of PNG.

Flag : Bugs_Bunny{E4Sy_T4Sk_F0R_H4X0r_L1KeS_Y0u}

Therefore, we need to reverse the file. This can be done through python easily.

```
    f1 = open('UNKOWN','r')
    con1 = f1.read()
    f1.close()
    con2 = con1[::-1]
    f2 = open('un1','w')
    f2.write(con2)
    f2.close()

```

Now you got the PNG image and the flag will be obvious then.

