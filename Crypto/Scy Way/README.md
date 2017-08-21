# Crypto: Scy way

**Link to the challenge is [here](http://www.bugsbunnyctf.me/challenges).**

The name of the problem suggest that it is Scytale cipher.
Read about Scytale cipher [here](https://en.wikipedia.org/wiki/Scytale).

Now after observing different possibilities I observe that the cipher is divided into 11 coloumns.

So

```
cipher="IHUDERMRCPESOLLANOEIHR"; 
decrypt="";
for(i=0,j=11;i<11;i++,j++)
	decrypt+=cipher[i]+cipher[j];

```

The flag is Bugs_Bunny{decrypt}
