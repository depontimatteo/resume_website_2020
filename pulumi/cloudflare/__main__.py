"""A Python Pulumi program"""

import pulumi
import pulumi_cloudflare as cloudflare

maculade_com = cloudflare.Zone("maculade.com",
    plan="free",
    zone="maculade.com",
    opts=pulumi.ResourceOptions(protect=True))
