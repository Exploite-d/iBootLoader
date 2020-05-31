# iBootLoader
easy script for loading iBootStage2 and custom BootLogo
# needed stuff

- argparse

- python3

# use

Before using put your device to pwnDFU mode with removed signature checks

- load iOS 10+ iBoot : ./iBootLoader.py --ibss path to dec ibss --ibec path to dec ibec -p PATCH -s shsh.shsh

- load iOS 9- iBoot: ./iBootLoader.py --ibss path to dec ibss --ibec path to dec ibec -n NOPATCH -s shsh.shsh

- custom logo: -l path to logo (patch argument needed so iOS9- iboots cant do it)


