import subprocess
import optparse
import re


def input_value():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--interface", dest="interface")
    parse_object.add_option("-m", "--mac", dest="mac")
    return parse_object.parse_args()


def change_mac(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


def successful(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    suc_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if suc_mac:
        return suc_mac.group(0)
    else:
        return None


(keys, values) = input_value()
change_mac(keys.interface, keys.mac)
if successful(keys.interface) == keys.mac:
    print('Success!!')
