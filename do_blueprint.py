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
