import os
import json
import digitalocean
from flask import Blueprint, jsonify

do_token = os.environ.get("DO_TOKEN", "")
digital_ocean = digitalocean.Manager(token=do_token)
bp = Blueprint("digitalocean", __name__, url_prefix="/digitalocean")


@bp.route("/regions", methods=("GET",))
def regions():
    regions = digital_ocean.get_all_regions()

    return jsonify(json.dumps(regions)), 200


@bp.route("/droplets", methods=("GET",))
def droplets():
    droplets = digital_ocean.get_all_droplets()
    data = []
    for droplet in droplets:
        data.append({
            "id": droplet.id,
            "name": droplet.name,
            "image": droplet.image})
    return jsonify(data), 200


@bp.route("/droplets/<int:id>")
def droplet(id):
    droplet = digital_ocean.get_droplet(id)

    data = {
        'id': droplet.id,
        'name': droplet.name,
        'memory': droplet.memory,
        'vcpus': droplet.vcpus,
        'cpu': droplet.disk,
        'region': droplet.region,
        'status': droplet.status,
        'image': droplet.image,
        'size-slug': droplet.size_slug,
        'locked': droplet.locked,
        'created_at': droplet.created_at,
        'networks': droplet.networks,
        'kernel': droplet.kernel,
        'backup_ids': droplet.backup_ids,
        'snapshop_ids': droplet.snapshot_ids,
        'action_ids': droplet.action_ids,
        'features': droplet.features,
        'ip_address': droplet.ip_address,
        'private_ip_adress': droplet.private_ip_address,
        'ip_v6_address': droplet.ip_v6_address,
        'ssh_keys': droplet.ssh_keys,
        'backups': droplet.backups,
        'ipv6': droplet.ipv6,
        'private_networking': droplet.private_networking,
        'user_data': droplet.user_data,
        'volumes': droplet.volumes,
        'tags': droplet.tags,
        'monitoring': droplet.monitoring
    }

    return jsonify(data), 200
