#!/bin/bash
#
# Description: backup and export docker containers and volumes
# Author: Bill

set -euo pipefail

# === Prompt for backup destination ===
echo "📁 Please enter the full path to the backup destination (e.g., /mnt/ssd/backup):"
read -r BACKUP_ROOT

# === Constants ===
USER="bill"
HOME_DIR="/home/$USER"
DATE=$(date +%F)
BACKUP_DIR="$BACKUP_ROOT/ubuntu-container-backup-$DATE"
IMAGES_DIR="$BACKUP_DIR/docker-images"
VOLUMES_DIR="$BACKUP_DIR/docker-volumes"

# === Auto-detect Distrobox Ubuntu Home Directory ===
echo "🔍 Searching for Ubuntu Distrobox home directory..."
UBUNTU_HOME_DIR=$(find "$HOME_DIR" -type d -path "*/ubuntu" | head -n 1)

if [[ -z "$UBUNTU_HOME_DIR" ]]; then
    echo "❌ Could not auto-detect Ubuntu Distrobox directory."
    exit 1
fi

UBUNTU_BACKUP="$BACKUP_DIR/docker-ubuntu/$(basename "$UBUNTU_HOME_DIR")-distrobox-home.tar.gz"

# === Create directory structure ===
echo "📂 Creating backup directory structure at: $BACKUP_DIR"
mkdir -p "$IMAGES_DIR" "$VOLUMES_DIR" "$(dirname "$UBUNTU_BACKUP")"

# === Backup Ubuntu Distrobox Home ===
echo "🗃️  Backing up Distrobox Ubuntu home directory from: $UBUNTU_HOME_DIR"
tar czf "$UBUNTU_BACKUP" -C "$(dirname "$UBUNTU_HOME_DIR")" "$(basename "$UBUNTU_HOME_DIR")"

# === Backup Docker Images ===
echo "🐳 Exporting Docker images..."
IMAGES=$(docker images --format '{{.Repository}}:{{.Tag}}')
for IMAGE in $IMAGES; do
    SAFE_IMAGE_NAME=$(echo "$IMAGE" | tr '/:' '_')
    echo "📦 Saving image: $IMAGE"
    docker save "$IMAGE" -o "$IMAGES_DIR/${SAFE_IMAGE_NAME}.tar"
done

# === Backup Docker Volumes ===
echo "💾 Backing up Docker volumes..."
VOLUMES=$(docker volume ls -q)
for VOL in $VOLUMES; do
    echo "🧱 Backing up volume: $VOL"
    docker run --rm \
        -v "$VOL:/volume" \
        -v "$VOLUMES_DIR:/backup" \
        alpine \
        tar czf "/backup/${VOL}.tar.gz" -C /volume .
done

echo "✅ Backup completed successfully at: $BACKUP_DIR"

