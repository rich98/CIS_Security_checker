import os
import subprocess

def check_password_policy():
    result = subprocess.run(['cat', '/etc/pam.d/common-password'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if 'pam_unix.so obscure sha512' in output:
        return True
    else:
        return False

def check_firewall():
    result = subprocess.run(['ufw', 'status'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if 'Status: active' in output:
        return True
    else:
        return False

def check_automatic_updates():
    result = subprocess.run(['cat', '/etc/apt/apt.conf.d/20auto-upgrades'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if 'APT::Periodic::Update-Package-Lists "1";' in output and 'APT::Periodic::Unattended-Upgrade "1";' in output:
        return True
    else:
        return False

def main():
    checks = {
        'Password Policy': check_password_policy,
        'Firewall': check_firewall,
        'Automatic Updates': check_automatic_updates
    }

    for check, func in checks.items():
        result = func()
        print(f'{check}: {"PASS" if result else "FAIL"}')

if __name__ == "__main__":
    main()
