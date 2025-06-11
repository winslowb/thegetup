#!/bin/bash
#
# Description:  used to restore distrobox and ubuntu data from backup.sh
# Tags: Bill
# Date: 2025-06-11

# === Config ===
USER="bill"
HOME_DIR="/home/$USER"
BACKUP_ROOT="/mnt/ssd/ubuntu-container-backup-2025-05-31"
IMAGES_DIR="$BACKUP_ROOT/docker-images"
VOLUMES_DIR="$BACKUP_ROOT/docker-volumes"
UBUNTU_TARBALL="$BACKUP_ROOT/docker-ubuntu/ubuntu-distrobox-home.tar.gz"
TARGET_UBUNTU_HOME="$HOME_DIR/.docker/ubuntu"
DISTROBOX_NAME="ubuntu"

echo "🔁 Starting restore for user: $USER"
echo "📦 Backup root: $BACKUP_ROOT"
echo

# === 1. Restore ~/docker/ubuntu ===
if [[ -f "$UBUNTU_TARBALL" ]]; then
    echo "📁 Restoring Distrobox home directory to: $TARGET_UBUNTU_HOME"
    mkdir -p "$(dirname "$TARGET_UBUNTU_HOME")"
    tar xzf "$UBUNTU_TARBALL" -C "$(dirname "$TARGET_UBUNTU_HOME")"

    echo "🔧 Setting ownership of ~/docker to $USER:$USER"
    chown -R "$USER:$USER" "$HOME_DIR/.docker"
else
    echo "⚠️  Distrobox backup tarball not found: $UBUNTU_TARBALL"
fi
echo

# === 2. Restore Docker Images ===
if [[ -d "$IMAGES_DIR" ]] && compgen -G "$IMAGES_DIR/*.tar" > /dev/null; then
    echo "🐳 Restoring Docker images..."
    for img in "$IMAGES_DIR"/*.tar; do
        echo "  - Loading image: $(basename "$img")"
        docker load -i "$img"
    done
else
    echo "⚠️  No Docker images found in: $IMAGES_DIR"
fi
echo

# === 3. Restore Docker Volumes ===
if [[ -d "$VOLUMES_DIR" ]] && compgen -G "$VOLUMES_DIR/*.tar.gz" > /dev/null; then
    echo "💾 Restoring Docker volumes..."
    for vol in "$VOLUMES_DIR"/*.tar.gz; do
        name=$(basename "$vol" .tar.gz)
        echo "  - Restoring volume: $name"

        docker volume create "$name" >/dev/null

        docker run --rm \
            -v "$name:/volume" \
            -v "$VOLUMES_DIR:/backup" \
            alpine tar xzf "/backup/${name}.tar.gz" -C /volume
    done
else
    echo "⚠️  No Docker volumes found in: $VOLUMES_DIR"
fi
echo

# === 4. Recreate and enter Distrobox ===
echo "📦 Creating Distrobox container: $DISTROBOX_NAME"
export DISTROBOX_USE_DOCKER=true

distrobox create \
    --name "$DISTROBOX_NAME" \
    --image ubuntu:24.04 \
    --home "$TARGET_UBUNTU_HOME" || {
        echo "⚠️  Failed to create distrobox container"; exit 1;
    }

echo "🚀 Entering Distrobox container: $DISTROBOX_NAME"
distrobox enter "$DISTROBOX_NAME"


