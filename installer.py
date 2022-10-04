import sys
import subprocess

def install_if_missing(path, *modules):
    sys.path.append(path)
    installed = installed_modules(path)
    missing = list(set(modules) - set(installed))
    if missing:
        print("Installing modules: " +  ", ".join(missing))
        subprocess.check_call(['pip', 'install', '--target=' + path, *missing])
        print("Installed modules: " +  ", ".join(missing))

def installed_modules(path):
    output = subprocess.check_output(["pip", "freeze", "--path=" + path])
    lines = output.decode().rsplit()
    modules = [line.split("==")[0] for line in lines]
    return modules