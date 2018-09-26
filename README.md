# cursedboard
Ncurse based textboard for ssh. 
> ssh bbs.shiptoasting.com

- Comfypost in style with markup 
- Browse with arrow keys and vim style commands 
- Sqlite3 backend scaling to the moon and beyond
- Country posting
- File Browser, Image and Text Viewer for the full multimedia experience
- Fuelled by npyscreen

### Setup
Needs python3, npyscreen and GeoIP. Use pip3 install -r requirements or packages provided by your distribution 

1. Install dependencies
2. Change motd.py to your likening 
3. Create a dedicated unix user
4. Copy config.py-sample to config.py and adjust settings
5. Touch .hushlogin in the user directory to avoid an IP leak
6. Disable TCP Forwarding for the user in sshd\_config 
7. Disable the sftp Subsystem or make sure its not set to internal-sftp in sshd\_config
8. ENJOY
