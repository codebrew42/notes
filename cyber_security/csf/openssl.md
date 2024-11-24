# OpenSSL Command Usage Guide

OpenSSL is a powerful toolkit for implementing the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols. It also provides a variety of cryptographic functions. This guide covers common commands and their usage.

## Table of Contents

1. [Generating a Private Key](#generating-a-private-key)
2. [Creating a Certificate Signing Request (CSR)](#creating-a-certificate-signing-request-csr)
3. [Self-Signed Certificate](#self-signed-certificate)
4. [Converting Certificate Formats](#converting-certificate-formats)
5. [Checking Certificate Information](#checking-certificate-information)
6. [Encrypting and Decrypting Files](#encrypting-and-decrypting-files)
7. [Creating a Hash](#creating-a-hash)
8. [Verifying a Certificate](#verifying-a-certificate)
9. [Conclusion](#conclusion)

## Generating a Private Key

To generate a new RSA private key, use the following command:

```bash
openssl genpkey -algorithm RSA -out private_key.pem
```

## Creating a Certificate Signing Request (CSR)

To create a CSR using an existing private key, run:

```bash
openssl req -new -key private_key.pem -out request.csr
```

## Self-Signed Certificate

To create a self-signed certificate, execute:

```bash
openssl req -x509 -new -nodes -key private_key.pem -sha256 -days 365 -out certificate.pem
```

## Converting Certificate Formats

To convert a PEM certificate to DER format, use:

```bash
openssl x509 -in certificate.pem -outform DER -out certificate.der
```

## Checking Certificate Information

To display the details of a certificate, run:

```bash
openssl x509 -in certificate.pem -text -noout
```

## Encrypting and Decrypting Files

To encrypt a file using AES-256-CBC, use:

```bash
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.txt
```

To decrypt the file, run:

```bash
openssl enc -d -aes-256-cbc -in encrypted.txt -out decrypted.txt
```

## Creating a Hash

To create a SHA256 hash of a file, use:

```bash
openssl dgst -sha256 file.txt
```

## Verifying a Certificate

To verify a certificate against a CA certificate, run:

```bash
openssl verify -CAfile ca_certificate.pem certificate.pem
```

## Conclusion

OpenSSL is a versatile tool that can handle a wide range of cryptographic tasks. The commands listed above are just a few examples of its capabilities. For more detailed usage, refer to the OpenSSL documentation or use the `man` command to access the manual pages.
