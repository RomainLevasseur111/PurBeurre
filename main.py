import mysql.connector
from classes.dbconnect import Dbconnect
import requests
import json
import constants as constants

connect_to_db = Dbconnect(constants.HOST, constants.USER, constants.PASSWORD, 'pur_beurre')
connect_to_db.connect()
