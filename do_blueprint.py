import os

import digitalocean
from flask import Blueprint, render_template

do_token = os.environ.get("DO_TOKEN", "")
digital_ocean = digitalocean.Manager(token=do_token)
bp = Blueprint("digitalocean", __name__, url_prefix="/digitalocean")


@bp.route("/regions", methods=("GET",))
def regions():
    regions = digital_ocean.get_all_regions()

    return render_template("regions.html", regions=regions)


@bp.route("/droplets")
def droplets():
    droplets = digital_ocean.get_all_droplets()

    return render_template("droplets.html", droplets=droplets)
