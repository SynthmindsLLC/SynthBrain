[![](https://img.realpython.net/6fe6464c8bf6ec2cbcf3f1f0e778156b)](https://srv.realpython.net/click/57356986228/?c=41067926597&p=29182759436&r=36103)

Cryptography[¶](#cryptography "Permalink to this headline")
===========================================================

![https://d33wubrfki0l68.cloudfront.net/f1a879211bca220b40f3855a91acd2a079ae22a9/9dec9/_images/33907152824_bf91078cc1_k_d.jpg](https://d33wubrfki0l68.cloudfront.net/f1a879211bca220b40f3855a91acd2a079ae22a9/9dec9/_images/33907152824_bf91078cc1_k_d.jpg)

cryptography[¶](#id1 "Permalink to this headline")
--------------------------------------------------

[cryptography](https://cryptography.io/en/latest/) is an actively developed library that provides cryptographic recipes and primitives. It supports Python 2.6-2.7, Python 3.3+, and PyPy.

cryptography is divided into two layers of recipes and hazardous materials (hazmat). The recipes layer provides a simple API for proper symmetric encryption and the hazmat layer provides low-level cryptographic primitives.

### Installation[¶](#installation "Permalink to this headline")

$ pip install cryptography

### Example[¶](#example "Permalink to this headline")

Example code using high level symmetric encryption recipe:

from cryptography.fernet import Fernet
key \= Fernet.generate\_key()
cipher\_suite \= Fernet(key)
cipher\_text \= cipher\_suite.encrypt(b"A really secret message. Not for prying eyes.")
plain\_text \= cipher\_suite.decrypt(cipher\_text)

GPGME bindings[¶](#gpgme-bindings "Permalink to this headline")
---------------------------------------------------------------

The [GPGME Python bindings](https://dev.gnupg.org/source/gpgme/browse/master/lang/python/) provide Pythonic access to [GPG Made Easy](https://dev.gnupg.org/source/gpgme/browse/master/), a C API for the entire GNU Privacy Guard suite of projects, including GPG, libgcrypt, and gpgsm (the S/MIME engine). It supports Python 2.6, 2.7, 3.4, and above. Depends on the SWIG C interface for Python as well as the GnuPG software and libraries.

A more comprehensive [GPGME Python Bindings HOWTO](https://dev.gnupg.org/source/gpgme/browse/master/lang/python/docs/GPGMEpythonHOWTOen.org) is available with the source, and an HTML version is available [at http://files.au.adversary.org](http://files.au.adversary.org/crypto/GPGMEpythonHOWTOen.html). Python 3 sample scripts from the examples in the HOWTO are also provided with the source and are accessible [at gnupg.org](https://dev.gnupg.org/source/gpgme/browse/master/lang/python/examples/howto/).

Available under the same terms as the rest of the GnuPG Project: GPLv2 and LGPLv2.1, both with the “or any later version” clause.

### Installation[¶](#id3 "Permalink to this headline")

Included by default when compiling GPGME if the configure script locates a supported python version (which it will if it’s in $PATH during configuration).

### Example[¶](#id4 "Permalink to this headline")

import gpg

\# Encryption to public key specified in rkey.
a\_key \= input("Enter the fingerprint or key ID to encrypt to: ")
filename \= input("Enter the filename to encrypt: ")
with open(filename, "rb") as afile:
    text \= afile.read()
c \= gpg.core.Context(armor\=True)
rkey \= list(c.keylist(pattern\=a\_key, secret\=False))
ciphertext, result, sign\_result \= c.encrypt(text, recipients\=rkey,
                                            always\_trust\=True,
                                            add\_encrypt\_to\=True)
with open("{0}.asc".format(filename), "wb") as bfile:
    bfile.write(ciphertext)
\# Decryption with corresponding secret key
\# invokes gpg-agent and pinentry.
with open("{0}.asc".format(filename), "rb") as cfile:
    plaintext, result, verify\_result \= gpg.Context().decrypt(cfile)
with open("new-{0}".format(filename), "wb") as dfile:
    dfile.write(plaintext)
\# Matching the data.
\# Also running a diff on filename and the new filename should match.
if text \== plaintext:
    print("Hang on ... did you say \*all\* of GnuPG?  Yep.")
else:
    pass