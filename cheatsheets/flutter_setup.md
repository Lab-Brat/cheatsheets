### Flutter Environment Set-up on Arch

* `yay -S flutter` -> Install Flutter (choose `jdk11-openjdk` during install)
* Set permissions for the flutter directory:
```bash
sudo groupadd flutterusers
sudo gpasswd -a $USER flutterusers\n
sudo chown -R :flutterusers /opt/flutter\n
sudo chmod -R g+w /opt/flutter/\n
```
* `yay -S android-sdk android-sdk-platform-tools android-sdk-build-tools` -> Install Android SDK
* `yay -S android-platform` -> Install android platform
* `sudo pacman -S ninja` -> Install ninja
* `sudo pacman -S chromium` -> Install Chromium Browser
* Set permissions for Android SDK directory:
```bash
sudo groupadd android-sdk
sudo gpasswd -a labbrat android-sdk
sudo setfacl -R -m g:android-sdk:rwx /opt/android-sdk
sudo setfacl -d -m g:android-sdk:rwX /opt/android-sdk
```
* Set env variables:
```bash
export PATH=$PATH:/usr/lib/jvm:$ANDROID_HOME/cmdline-tools/latest/bin
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk"
unset JAVA_OPTS
#export JAVA_OPTS="-XX:+IgnoreUnrecognizedVMOptions --add-modules java.se.ee"
export CHROME_EXECUTABLE="chromium"
```
* `sdkmanager --list`
* `sdkmanager --install "cmdline-tools;latest"`
* `flutter doctor --android-licenses`
* `flutter doctor` -> Run flutter doctor to diagnose issues with dependencies
* `yay -S visual-studio-code-bin` -> Install Visual Studio Code
* Install `Flutter` extension

* Connect Android hardware device to VS Code 
  * Go to `Settings` -> `About` and click on `MIUI Version` multiple times until developer mode it on
  * Go to `Settings` -> `Additional Settings` -> `Developer options`
  * Turn On `USB Debugging`
  * Turn On `Install via USB`

