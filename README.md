# Requirement

* webdriver_manager
* selenium
* google-chrome

```
pip install webdriver-manager
pip install selenium
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt -y install ./google-chrome-stable_current_amd64.de
```


# Issue

* 한글 꺠짐

1. locale 설정
    ```
    sudo apt-get install language-pack-ko
    sudo locale-gen ko_KR.UTF-8
    sudo dpkg-reconfigure locales
    sudo update-locale LANG=ko_KR.UTF-8 LC_MESSAGES=POSIX
    ```
1. font 설치
    ```
    cd /usr/share/fonts
    sudo apt-get install fonts-unfonts-core fonts-unfonts-extra
    sudo apt-get install fonts-baekmuk
    sudo apt-get install fonts-unfonts-core fonts-unfonts-extra
    ```
1. reboot
    ```
    sudo reboot
    ```
