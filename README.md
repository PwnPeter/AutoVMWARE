# AutoVMware 🤖
Automatically starts and restarts VMWare Virtual Machines 💫

## Get Started 🧙‍♂️
Launch `autoVMware.sh` with crontab on linux (or with task manager on windows), for example to check every minute if all VMs are running to restart them if necessary : 
```bash
sudo crontab -e
# In editor
* * * * * su peterpan -c "/PATH_TO_SCRIPT/AutoVMWARE/autoVMware.sh" # You can also run directly the autoVMware.py instead of using a .sh
```

If you use VMware Player or Fusion instead of VMware Workstation, you need to edit all command line in the script containing the `ws` argument. Possibles arguments are :
 * `ws` for **Workstation Pro**
 * `fusion` for **VMware Fusion** (MacOS)
 * `player` fir **VMware Player**
 
example for **VMware Player** :   

`subprocess.run(f'vmrun -T ws stop "{vm_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)` -> `subprocess.run(f'vmrun -T player stop "{vm_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)`

Basically the script is programmed to launch all the VMs (.vmx) contained in the folder and subfolders of `/home`. The `PATH_TO_SEARCH` variable can be modified to match the path pattern of the VMs you want to monitor with the script. 

The script is designed to be run in a Linux environment, but it is easily transportable to a Windows environment with some modifications.
