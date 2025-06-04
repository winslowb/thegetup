#!/bin/bash
#
# Description: backup script
# Tags: Bill
# Date: 2025-05-31

set -euo pipefail

BACKUP_DIR="/media/bill/PortableSSD/ubuntu-container-backup-$(date +%F)"
mkdir -p "$BACKUP_DIR"/{docker-images,docker-volumes,docker-ubuntu}

echo "🔁 Backing up Docker images..."
docker images --format '{{.Repository}}:{{.Tag}}' | while read -r img; do
    safe_name=$(echo "$img" | tr '/:' '__')
    docker save "$img" -o "$BACKUP_DIR/docker-images/${safe_name}.tar"
done

echo "📦 Backing up Docker volumes..."
docker volume ls -q | while read -r vol; do
    docker run --rm -v "$vol:/volume" -v "$BACKUP_DIR/docker-volumes:/backup" alpine \
        tar czf "/backup/${vol}.tar.gz" -C /volume .
done

echo "📁 Archiving Distrobox working directory at \$HOME/docker/ubuntu..."
tar czf "$BACKUP_DIR/docker-ubuntu/ubuntu-distrobox-home.tar.gz" -C "$HOME/docker" ubuntu

echo "✅ All backups written to: $BACKUP_DIR"
 
