# TROJAN HORSE

## Description:
A Trojan Horse is a type of malware disguised as legitimate software, such as a game. Unlike a virus, it doesn’t necessarily cause harm but can fetch data from the infected machine and send it to an attacker.

In this case, the Trojan simulates a simple "Guess the Number" game. Behind the scenes, it connects to a remote server and allows the server to issue commands to the client (the infected machine).

## Note:  
In the real world, a Trojan would likely be implemented in a lower-level language like C++ to avoid detection. For educational purposes, this project uses Python to help understand the mechanics of a Trojan.

## How to Reproduce:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/AdityaGahukar/Trojan-Horse.git
   cd Trojan-Horse
   ```

2. Adjust ip address both in server.py and spyware.py to your own by running ipconfig (Windows) or ifconfig (Linux/macOS).
3. From terminal #1 execute server.py:
   ```bash
   python server.py
   ```

4. from terminal #2 execute main.py
   ```bash
   python main.py
   ```
    * The "Guess a Number" game will be prompted. Behind the curtains a connection is established between server and spyware (it runs on a different thread respect to the game)
5. From server's terminal try these commands:
    * infect: The Trojan will print a message as a joke or distraction.
    * chat on: Activates chat mode where you can send messages to the victim
    * chat off - return to default mode
    * get_sysinfo: Retrieves system information like OS, version, and machine specs.
    * exec:<command>: Executes shell commands on the victim's machine.
    * create_file:<filename>:<content>: Creates a file with the given content.