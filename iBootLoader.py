#!/usr/bin/env python3

import argparse
import sys
from os import system

Pink = '\33[95m'
CEND = '\033[0m'

argv = sys.argv

print(Pink + "iBootLoader allows you to automatically patch iBSS and iBEC and load it." + CEND)
parser = argparse.ArgumentParser()
parser.add_argument("--ibss", help="Specify path to decrypted iBSS image.")
parser.add_argument("--ibec", help="Specify path to decrypted iBEC image.")
parser.add_argument("--shsh", "-s", help="Specify path to your SHSH Blobs.")
parser.add_argument("--nopatch", "-n", help="Use if you are trying to load iOS 9 iBoot(but specify ibss path to iOS 10+ image).")
parser.add_argument("--logo", "-l", help="Use if you are trying to load iOS 9 iBoot(but specify ibss path to iOS 10+ image).")
parser.add_argument("--patch", "-p", help="Use if you are trying to load iOS 10+ iBoot.")
args = parser.parse_args()
if len(argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

system("rm -rf ibss.dec")
system("rm -rf ibss.pwn")
system("rm -rf ibss.im4p")
system("rm -rf ibss.img4")

system("rm -rf ibec.dec")
system("rm -rf ibec.pwn")
system("rm -rf ibec.im4p")
system("rm -rf ibec .img4")

print(Pink + "Pathing iBSS and iBEC" + CEND)

if args.ibss and args.shsh:
    shsh_path = str(args.shsh)
    ibss_path = str(args.ibss)
    system("bin/kairos " + ibss_path + " ibss.pwn")
    system("bin/img4tool -c ibss.im4p --type ibss --desc ibss ibss.pwn")
    system("bin/img4tool -p ibss.im4p -c ibss.img4 -s " + shsh_path)
else:
    print("iBSS path or SHSH path not specified. Exiting...")
    sys.exit(1)
if args.ibec and args.shsh and args.nopatch:
    ibec_path = str(args.ibec)
    system("bin/img4tool -c ibec.im4p --type ibec --desc ibec " + ibec_path)
    system("bin/img4tool -p ibec.im4p -c ibec.img4 -s " + shsh_path)
if args.ibec and args.shsh and args.patch:
    ibec_path = str(args.ibec)
    system("bin/kairos " + ibec_path + " ibec.pwn")
    system("bin/img4tool -c ibec.im4p --type ibec --desc ibec ibec.pwn")
    system("bin/img4tool -p ibec.im4p -c ibec.img4 -s " + shsh_path)   

print(Pink + "About to load iBSS and iBEC" + CEND)
system("bin/irecovery -f ibss.img4")
system("bin/irecovery -f ibec.img4")
print(Pink + "Done! iBoot has been succesfully loaded. You can now load unsigned images or other cool stuff :)" + CEND)

if args.logo:
    print(Pink + "User selected to select custom bootlogo :) Doing stuff now :D" + CEND)
    logo_path = str(args.logo)
    system("bin/ibootim " + logo_path + " logo_ok_bommer_lmfao")
    system("bin/img4tool -c logo.im4p --type logo --desc logo logo_ok_bommer_lmfao")
    system("bin/img4tool -p logo.im4p -c logo.img4 -s " + shsh_path)
    print(Pink + "Sending custom logo :)" + CEND)
    system("bin/irecovery -f logo.img4")
    system('bin/irecovery -c "bgcolor 0 0 0" ')
    system('bin/irecovery -c "setpicture 1" ')
    print(Pink + "Enjoy:)" + CEND)


