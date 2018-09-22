# -*- coding: utf-8 -*-

class Droplet:
    """Digital ocean's droplet management.

    Attributes:
        id (:obj:`int`): A unique identifier for each Droplet instance.
        name (:obj:`str`): The human-readable name set for the Droplet instance.
        memory (:obj:`int`): Memory of the Droplet in megabytes.
        vcpus (:obj:int`): The number of virtual CPUs.
        disk (:obj:`int`): The size of the Droplet's disk in gigabytes.
        locked (:obj:`bool`): A boolean value indicating whether the Droplet has been locked, preventing actions by users.
        created_at(:obj:`str`) A time value given in ISO8601 combined date and time format that represents when the Droplet was created.
        status (:obj:`str`): A status string indicating the state of the Droplet instance. This may be "new", "active", "off", or "archive".
        backup_ids (:obj:`dict`):   An array of backup IDs of any backups that have been taken of the Droplet instance.
        snapshot_ids (:obj:`dict`): An array of snapshot IDs of any snapshots created from the Droplet instance.
        features (:obj:`dict`) An array of features enabled on this Droplet.
        region (:obj:`region`): The region that the Droplet instance is deployed in.
        image (:obj:`image`): The base image used to create the Droplet instance.
        size (:obj:`size`): The current size object describing the Droplet.
        size_slug (:obj:`str`): The unique slug identifier for the size of this Droplet.
        networks (:obj:`network`): The details of the network that are configured for the Droplet instance
        kernel (:obj:`kernel`): The current kernel.
        next_backup_window (:obj:`backup`): The details of the Droplet's backups feature, if backups are configured for the Droplet.
        tags (:obj: `dict`): An array of Tags the Droplet has been tagged with.
        volume_ids (:obj:`dict`): A flat array including the unique identifier for each Block Storage volume attached to the Droplet.
        
    """


    def __init__(self):
        # default values
        self.id	= None
        self.name = None
        self.memory = None
        self.vcpus = None
        self.disk = None
        self.locked = None
        self.created_at = None
        self.status = None
        self.backup_ids = []
        self.snapshot_ids = []
        self.features = []
        self.region = None
        self.image = None
        self.size = None
        self.size_slug = None	
        self.networks = None
        self.kernel	= None
        self.next_backup_window	= None
        self.tags = []
        self.volume_ids = None
