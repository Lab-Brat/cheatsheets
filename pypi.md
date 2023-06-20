### PyPi

#### How to overwrite existing release
For example, a test_app version 0.1.5 was pushed to PyPi, 
but something was forgotten and it needs to be reuploaded. 
In this case:
* Push another tag with a build number, for example 0.1.5-1
* Delete release 0.1.5 from PyPi
* Publish 0.1.5-1 tag to PyPi

Reference: [StackOverflow](https://stackoverflow.com/questions/21064581/how-to-overwrite-pypi-package-when-doing-upload-from-command-line)
