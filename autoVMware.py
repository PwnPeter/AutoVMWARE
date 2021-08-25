import glob
import time
import subprocess

def get_vm_on_system():
    return glob.glob('/home/**/*.vmx', recursive=True)
    

def get_vm_in_execution(VMS_FOUND):
    VMS_NOT_FOUND = []
    VMS_LAUNCHED = subprocess.getoutput('vmrun list').split("\n")[1:]
    for vm in VMS_FOUND:
        if vm not in VMS_LAUNCHED:
            VMS_NOT_FOUND.append(vm)
    return VMS_NOT_FOUND
    

def start_vm(vm_path):
    result_stop = subprocess.run(f'vmrun -T ws stop "{vm_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'vmrun -T ws stop "{vm_path}"')
    result_remove_lock = subprocess.run(f'rm -Rf "{"/".join(vm_path.split("/")[::-1][1:][::-1])}/**.lck"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'rm -Rf "{"/".join(vm_path.split("/")[::-1][1:][::-1])}/*.lck"')
    result_start = subprocess.run(f'vmrun -T ws start "{vm_path}" nogui',shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'vmrun -T ws start "{vm_path}" nogui')
    if result_start.returncode == 0:
        print(f"VM {vm_path} lancé ")
    else:
        print(f"Erreur lors du lancement de {vm_path} : {result_start.stderr}")

def main():
    # while 1:
    VMS_FOUND = get_vm_on_system()
    # print(VMS_FOUND)
    VMS_NOT_FOUND = get_vm_in_execution(VMS_FOUND)
    # print(VMS_NOT_FOUND)
    if VMS_NOT_FOUND:
        for vm_path in VMS_NOT_FOUND:
            print(f'############# VM {vm_path.split("/")[::-1][0]} #############')
            start_vm(vm_path)
            print("'##########################\n")
    else:
        print("Aucune VM à lancer/relancer.")
        # print("sleep 300s")
        # time.sleep(300)
if __name__ == "__main__":
    main()