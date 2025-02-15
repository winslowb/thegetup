import os
import subprocess

def run_command(command):
    """Run a shell command."""
    subprocess.run(command, shell=True, check=True)

def get_package_list(distro):
    """Return the package list based on the distribution."""
    if distro == "debian":
        return [
            "tmux", "gpg", "gcc", "make", "gettext", "unzip", "cmake", "build-essential",
            "python3-neovim", "jq", "wget", "curl", "apt-file", "python3-dev", "python3-pip",
            "tzdata", "dconf-cli", "uuid-runtime", "inetutils-ping", "rclone", "pkg-config",
            "libtool", "locate", "git", "tmux", "gh", "libu2f-udev", "xsel", "docker.io",
            "locate", "python3.10-venv", "calendar", "ccal", "htop", "gcalcli", "fuse",
            "libnss3", "libatk-bridge*", "libgtk-3-common", "libasound2", "lxappearance",
            "net-tools", "nvidia-utils-535", "nvidia-cuda-toolkit", "whois", "ripgrep",
            "nmap", "dnsutils", "xmlstarlet", "gawk", "fzf", "gettext"
        ]
    elif distro == "ubuntu":
        return [
            "tmux", "gpg", "gcc", "make", "gettext", "unzip", "cmake", "build-essential",
            "python3-neovim", "jq", "wget", "curl", "apt-file", "python3-dev", "python3-pip",
            "tzdata", "dconf-cli", "uuid-runtime", "inetutils-ping", "rclone", "pkg-config",
            "libtool", "locate", "git", "tmux", "gh", "libu2f-udev", "xsel", "docker.io",
            "locate", "python3.10-venv", "calendar", "ccal", "htop", "gcalcli", "fuse",
            "libnss3", "libatk-bridge2.0-0", "libgtk-3-0", "libasound2", "lxappearance",
            "net-tools", "nvidia-utils-535", "nvidia-cuda-toolkit", "whois", "ripgrep",
            "nmap", "dnsutils", "xmlstarlet", "gawk", "fzf", "gettext"
        ]
    else:
        raise ValueError("Unsupported distribution")

def main():
    distro = input("Enter your Linux distribution (debian/ubuntu): ").strip().lower()
    if distro not in ["debian", "ubuntu"]:
        print("Invalid distribution. Please choose 'debian' or 'ubuntu'.")
        return
    while True:
        print("\nSelect an option:")
        print("1. Update and upgrade system")
        print("2. Install packages")
        print("3. Setup directories")
        print("4. Install Starship")
        print("5. Configure Git")
        print("6. Install NVM and Node.js")
        print("7. Install Bitwarden CLI")
        print("8. Install Chezmoi")
        print("9. Clone and build Neovim")
        print("10. Download and extract Jira CLI")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            run_command("sudo apt autoremove -y")
            run_command("sudo apt update && sudo apt upgrade -y")
        elif choice == '2':
            packages = get_package_list(distro)
            run_command(f"sudo apt install {' '.join(packages)} -y")
        elif choice == '3':
            os.makedirs(os.path.expanduser("~/.local/bin"), exist_ok=True)
            os.makedirs(os.path.expanduser("~/projects"), exist_ok=True)
        elif choice == '4':
            run_command("wget https://starship.rs/install.sh")
            run_command("chmod 755 install.sh")
            run_command("./install.sh -b $HOME/.local/bin")
        elif choice == '5':
            run_command('git config --global user.name "regular bill"')
            run_command('git config --global user.email "regularbill@bill.com"')
            run_command("gh auth login")
        elif choice == '6':
            run_command("wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash")
            nvm_dir = os.path.expanduser("~/.nvm")
            run_command(f"bash -c '[ -s \"{nvm_dir}/nvm.sh\" ] && . \"{nvm_dir}/nvm.sh\" && nvm install --lts && nvm use --lts'")
        elif choice == '7':
            run_command("npm install -g @bitwarden/cli")
            run_command("bw login")
        elif choice == '8':
            run_command("sh -c \"$(curl -fsLS get.chezmoi.io)\"")
            run_command("sudo cp $HOME/projects/bin/chezmoi /usr/bin/")
            run_command("alias dot=/usr/bin/chezmoi")
            run_command("export PATH=$PATH:$HOME/.local/bin")
            run_command("/usr/bin/chezmoi init https://github.com/winslowb/dotfiles.git")
            run_command("/usr/bin/chezmoi update -v")
            run_command("source $HOME/.bashrc")
        elif choice == '9':
            run_command("git clone https://github.com/neovim/neovim.git ~/projects/neovim")
            run_command("cd ~/projects/neovim && git checkout origin/release-0.8")
            run_command("cd ~/projects/neovim && make CMAKE_BUILD_TYPE=Release")
            run_command("sudo make install")
            run_command("cp ~/projects/neovim/build/bin/nvim ~/.local/bin")
        elif choice == '10':
            run_command("wget https://github.com/ankitpokhrel/jira-cli/releases/download/v1.3.0/jira_1.3.0_linux_arm64.tar.gz")
            run_command("tar -xzvf jira_1.3.0_linux_arm64.tar.gz")
        elif choice == '11':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
