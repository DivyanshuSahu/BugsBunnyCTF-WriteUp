# Crypto: Scy way

**Link to the challenge is [here](http://www.bugsbunnyctf.me/challenges#Scy way).**

The name of the problem suggest that it is Scytale cipher.
Read about Scytale cipher [here](https://en.wikipedia.org/wiki/Scytale).

Now after observing different possibilities I observe that the cipher is divided into 11 coloumns.

So

<<<<<<< HEAD
```

cipher="IHUDERMRCPESOLLANOEIHR"; 
decrypt="";
for(i=0,j=11;i<11;i++,j++)
	decrypt+=cipher[i]+cipher[j];

```
=======
cipher="IHUDERMRCPESOLLANOEIHR"; 
decrypt=""
for(i=0,j=11;i<11;i++,j++)
	decrypt+=cipher[i]+cipher[j];
>>>>>>> fff204b9e39e83ed352e99bcc5dad1e2e636d633

The flag is Bugs_Bunny{decrypt}
