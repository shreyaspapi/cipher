<h1> Cipher </h1>
<p>
This cipher can be used to encrypt text through the use of letter-by-letter substitutions, eg.
</p>
<b>
Key: CRYPTO <br>
Plaintext: I LOVE SECURITY <br>
</b>
<br>
<p>
The encryption is performed by writing the key as mnay times as necessary (Can be partially) so that there is a correspondence between each character in the plain text and a character in the key. eg.
</p>
<b>
I  LOVE SECURITY <br>
C RYPT OCRYPTOC <br>
</b>
<br>
<p>
The ciphertext is constructed on by associating each letter of alphabet to a number from 0 to 25.
</p>
<b>
00 &nbsp; 01 &nbsp; 02 &nbsp; 03 &nbsp; 04 &nbsp; 05 &nbsp; 06 &nbsp; 07 &nbsp; ... <br>
A &nbsp;&nbsp;&nbsp;&nbsp;  B &nbsp;&nbsp;&nbsp;  C &nbsp;&nbsp;&nbsp;  D &nbsp;&nbsp;&nbsp;  E &nbsp;&nbsp;&nbsp;&nbsp; F &nbsp;&nbsp;&nbsp;&nbsp; G &nbsp;&nbsp;&nbsp;&nbsp; H &nbsp;&nbsp; ... <br>
</b>
<br>
<p>
and then adding the value of each letter of the plaintext with the value of the corrosponding letter of the key (modulo 26), and interpreting the result again as a letter. Thus, the first letter of ciphertext is obtained by:
</p>
<b>
I + C = K  <br>
08 + 02 = 10  mod 26 <br>
</b>
