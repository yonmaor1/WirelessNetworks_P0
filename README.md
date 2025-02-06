# Notes 
## 2/5/2025
- got monitor mode working
- setup:
    - laptop A has wireshark running in monitor mode
    - laptop B connected to CMU SECURE, pinging laptop A
    - laptop A filtering packets with `wlan.sa == 0:1f:26:41:f0:0` where `0:1f:26:41:f0:0` came from running `arp -a` 
    - laptop A sees packets, but they sometimes come in randomly, and don't allways align with when laptop B pings
