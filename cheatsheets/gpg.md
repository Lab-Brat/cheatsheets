### GPG keys

After keys are created, list them with:
```
gpg --list-secret-keys --keyid-format=long
```

And save signing key to git config:
```
git config --global user.signingkey <key>
```

#### Troubleshooting
```
error: gpg failed to sign the data:
[GNUPG:] KEY_CONSIDERED 0831EB14AD7581A5BC31AD4312D64D09FC383FD2 0
[GNUPG:] BEGIN_SIGNING H10
[GNUPG:] PINENTRY_LAUNCHED 526623 curses 1.2.1-unknown - xterm-256color :1 - 1000/1000 0
gpg: signing failed: Inappropriate ioctl for device
[GNUPG:] FAILURE sign 83918950
gpg: signing failed: Inappropriate ioctl for device
```

Solution:
```
export GPG_TTY=$(tty)
```

#### Links
* [[Link](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification#gpg-commit-signature-verification)] - GitHub article on GPG keys
* [[Link](https://wiki.gentoo.org/wiki/GnuPG)] - Gentoo article on GPG keys
