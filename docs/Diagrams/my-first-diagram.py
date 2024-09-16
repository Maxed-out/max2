from diagrams import Diagram, Edge, Cluster
from diagrams.aws.storage import S3
from diagrams.onprem.compute import Server
from diagrams.aws.analytics import Redshift
from diagrams.aws.compute import LambdaFunction as Lambda

from diagrams.generic.network import Router
from diagrams.onprem.client import Client

from diagrams.onprem.vcs import Gitlab

from diagrams.onprem.container import Docker

from diagrams.custom import Custom

with Diagram("My Design Diagram") :
    DataService = Server("Data Service")

    Router = Router("Wireless Router")
    Repo = Gitlab("GitLab Repo")

    WorkStation = Client("Workstation")

    Docker=Docker("Docker")

    cc_heart = Custom("Creative Commons", "./images/harddrive.png")
    cc_notebook = Custom("Notebook", "./images/laptop.png")
    cc_robot = Custom("Your Robot", "./images/robot.png")
    cc_docker = Custom("Your Robot", "./images/docker_registry.png")


    with Cluster('S3 Buckets') :
        S3Storage = [S3(f"S3 Bucket_{n}") for n in range(1,4)]

    with Cluster('Lambda Process'):
        Lambdas = [Lambda(f"LambdaFunction_{n}") for n in range(1,4)]

        for n in range(0,2):
            Lambdas[n] - Lambdas[n+1]



    MasterDB = Redshift("Redshift DW")

    DataService >> Edge(label="Sending data to S3") >> S3Storage
    S3Storage >> Edge(label="Copying data to Redshift") >> MasterDB
    MasterDB >> Lambdas

