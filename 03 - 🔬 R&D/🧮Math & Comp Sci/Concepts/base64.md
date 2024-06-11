---
title: "Base64 Encoding and Decoding"
description: "A binary-to-text encoding scheme that represents binary data in an ASCII string format by translating it into a radix-64 representation, used for various applications such as embedding images within scripts or transmitting binary data over text-only channels."
type: "concept"
tags:
- "Base64"
- "Encoding"
- "Decoding"
- "ComputerProgramming"
relationships:
- "#used_for [[Embedding Binary Data]]"
- "#related_to [[ASCII]], [[Binary Data]], [[Data Transmission]]"
birthdate: "deathdate: founded: tags:"
- "Base64 Encoding"
- "Text Representation of Binary Data"
- "Web Development"
- "Email Attachments"
start_date: "end_date: "
---

Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format by translating it into a radix-64 representation. It is used to encode binary files such as images within scripts, embed PDF files in HTML pages, and store or transmit binary data in environments that are restricted to ASCII data, such as email and URLs[1][2][3].

## Encoding
The encoding process involves taking binary data and converting it into a sequence of printable characters. Base64 uses a set of 64 characters, which includes A-Z, a-z, 0-9, '+', and '/', with '=' used as a padding character. The binary data is divided into groups of 6 bits, with each group then being mapped to one of the 64 characters in the Base64 alphabet[1][3].

An example of encoding is the ASCII string "Man", which is represented in binary as 01001101 01100001 01101110. These three bytes are joined together in a 24-bit buffer, which is then split into four groups of 6 bits. Each group is then converted into a Base64 character, resulting in the Base64-encoded string "TWFu"[4].

## Decoding
Decoding is the reverse process, where a Base64-encoded string is converted back into the original binary data. Each character in the Base64 string represents 6 bits of data, and by mapping these characters back to their binary equivalents and combining them, the original binary data is reconstructed[1][3].

For example, the Base64-encoded string "TWFu" is split into the characters 'T', 'W', 'F', and 'u', which correspond to the binary values 010011, 010110, 000101, and 101110. These are then combined into the original 24-bit binary sequence, which is split back into three 8-bit bytes, resulting in the original ASCII string "Man"[4].

## Applications and Considerations
Base64 is widely used on the World Wide Web, in email attachments, and for data URIs in web development. It is also used for encoding data in QR codes and for representing cryptographic keys and checksums in a readable format[1][2].

One of the limitations of Base64 is that it increases the size of the data by approximately 33%, due to the encoding process. This overhead is a trade-off for the ability to safely transmit binary data over channels that only support text[1][2].

In JavaScript, the functions `btoa()` and `atob()` are used for Base64 encoding and decoding, respectively. However, these functions have limitations when dealing with Unicode text, and additional steps are required to handle such data correctly[3].

## [[wikilinks]]
- [[Binary Data]]
- [[ASCII]]
- [[Text Encoding]]
- [[Data Transmission]]
- [[Web Development]]
- [[Cryptography]]

Citations:
[1] https://en.wikipedia.org/wiki/Base64
[2] https://www.freecodecamp.org/news/what-is-base64-encoding/
[3] https://developer.mozilla.org/en-US/docs/Glossary/Base64
[4] https://www.base64decode.org
[5] https://builtin.com/software-engineering-perspectives/base64-encoding
[6] https://emn178.github.io/online-tools/base64_decode.html
[7] https://www.base64encode.org
[8] https://www.base64decode.net
[9] https://docs.python.org/3/library/base64.html
[10] https://base64.guru/converter/decode
[11] https://www.youtube.com/watch?v=mxwvvMZaIvU
[12] https://www.rapidtables.com/web/tools/base64-decode.html