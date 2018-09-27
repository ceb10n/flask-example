from flask import Flask, render_template
import digitalocean
import os


app = Flask(__name__)
do_token = os.environ.get('DO_TOKEN', '')
digital_ocean = digitalocean.Manager(token=do_token)


@app.route("/droplets")
def droplets():
    droplets = digital_ocean.get_all_droplets()
    
    return render_template('droplets.html', droplets=droplets)


@app.route("/regions")
def regions():
    regions = digital_ocean.get_all_regions()
    
    return render_template('regions.html', regions=regions)


if __name__ == "__main__":
    app.run()











