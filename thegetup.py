import os
import subprocess

def run_command(command):
    """Run a shell command."""
    subprocess.run(command, shell=True, check=True)

def main():
    # Remove unnecessary packages and update system
    run_command("sudo apt autoremove -y")
    run_command("sudo apt update && sudo apt upgrade -y")

    # Install packages
    packages = [
        "tmux", "gpg", "gcc", "make", "gettext", "unzip", "cmake", "build-essential",
        "python3-neovim", "jq", "wget", "curl", "apt-file", "python3-dev", "python3-pip",
        "tzdata", "dconf-cli", "uuid-runtime", "inetutils-ping", "rclone", "pkg-config",
        "libtool", "locate", "git", "tmux", "gh", "libu2f-udev", "xsel", "docker.io",
        "locate", "python3.10-venv", "calendar", "ccal", "htop", "gcalcli", "fuse",
        "libnss3", "libatk-bridge*", "libgtk-3-common", "libasound2", "lxappearance",
        "net-tools", "nvidia-utils-535", "nvidia-cuda-toolkit", "whois", "ripgrep",
        "nmap", "dnsutils", "xmlstarlet", "gawk", "fzf", "gettext"
    ]
    run_command(f"sudo apt install {' '.join(packages)} -y")

    # Create directories
    os.makedirs(os.path.expanduser("~/.local/bin"), exist_ok=True)
    os.makedirs(os.path.expanduser("~/projects"), exist_ok=True)

    # Download and install starship
    run_command("wget https://starship.rs/install.sh")
    run_command("chmod 755 install.sh")
    run_command("./install.sh -b $HOME/.local/bin")

    # Git configuration
    run_command('git config --global user.name "regular bill"')
    run_command('git config --global user.email "regularbill@bill.com"')
    run_command("gh auth login")

    # Install nvm and node
    run_command("wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash")
    nvm_dir = os.path.expanduser("~/.nvm")
    run_command(f"[ -s '{nvm_dir}/nvm.sh' ] && . '{nvm_dir}/nvm.sh'")
    run_command("nvm install --lts")
    run_command("nvm use --lts")

    # Install Bitwarden CLI
    run_command("npm install -g @bitwarden/cli")
    run_command("bw login")

    # Install chezmoi
    run_command("sh -c \"$(curl -fsLS get.chezmoi.io)\"")
    run_command("sudo cp $HOME/projects/bin/chezmoi /usr/bin/")
    run_command("alias dot=/usr/bin/chezmoi")
    run_command("export PATH=$PATH:$HOME/.local/bin")
    run_command("/usr/bin/chezmoi init https://github.com/winslowb/dotfiles.git")
    run_command("/usr/bin/chezmoi update -v")
    run_command("source $HOME/.bashrc")

    # Clone and build Neovim
    run_command("git clone https://github.com/neovim/neovim.git ~/projects/neovim")
    run_command("cd ~/projects/neovim && git checkout origin/release-0.8")
    run_command("cd ~/projects/neovim && make CMAKE_BUILD_TYPE=Release")
    run_command("sudo make install")
    run_command("cp ~/projects/neovim/build/bin/nvim ~/.local/bin")

    # Download and extract Jira CLI
    run_command("wget https://github.com/ankitpokhrel/jira-cli/releases/download/v1.3.0/jira_1.3.0_linux_arm64.tar.gz")
    run_command("tar -xzvf jira_1.3.0_linux_arm64.tar.gz")

    # Set terminal and run additional script
    os.environ['TERMINAL'] = 'tilix'
    run_command("bash -c \"$(wget -qO- https://git.io/vQgMr)\"")

if __name__ == "__main__":
    main()
