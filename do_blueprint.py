import os

import digitalocean
from flask import Blueprint, jsonify

do_token = os.environ.get("DO_TOKEN", "")
digital_ocean = digitalocean.Manager(token=do_token)
bp = Blueprint("digitalocean", __name__, url_prefix="/digitalocean")


@bp.route("/regions", methods=("GET",))
def regions():
    regions = digital_ocean.get_all_regions()

    return jsonify(regions), 200


@bp.route("/droplets", methods=("GET",))
def droplets():
    droplets = digital_ocean.get_all_droplets()

    return jsonify(droplets), 200
