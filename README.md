# AutoVMWARE
Automatically starts and restarts VMWare VMs 💫

## Install 🧙‍♂️
Launch `autoVMware.sh` with crontab on linux (or with task manager on windows).

Basically the script is programmed to launch all the VMs (.vmx) contained in the folder and subfolders of `/home`. The `PATH_TO_SEARCH` variable can be modified to match the path pattern of the VMs you want to monitor with the script. 

The script is designed to be run in a Linux environment, but it is easily transportable to a Windows environment with some modifications.