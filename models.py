import os, utm
from datetime import datetime
from ming import collection, Field, Document, schema, Session, create_datastore

MONGO_URL = os.environ.get('MONGO_URL', 'mim://dc_gun_crime')

db_bind = create_datastore(MONGO_URL)
db_session = Session(db_bind)

Crime = collection(
    'crime', db_session,
    Field('_id', schema.ObjectId),
    Field('CCN', str),
    Field('REPORTDATETIME', datetime, if_missing=datetime.utcnow),
    Field('SHIFT', str),
    Field('OFFENSE', str),
    Field('METHOD', str),
    Field('LASTMODIFIEDDATE', str),
    Field('BLOCKSITEADDRESS', str),
    Field('BLOCKXCOORD', str),
    Field('BLOCKYCOORD', str),
    Field('WARD', str),
    Field('ANC', str),
    Field('DISTRICT', str),
    Field('PSA', str),
    Field('NEIGHBORHOODCLUSTER', str),
    Field('BUSINESSIMPROVEMENTDISTRICT', str),
    Field('BLOCK_GROUP', str),
    Field('CENSUS_TRACT', str),
    Field('VOTING_PRECINCT', str),
    Field('START_DATE', datetime, if_missing=datetime.utcnow),
    Field('END_DATE', datetime, if_missing=datetime.utcnow),
    Field('lat', float),
    Field('lon', float),
    Field('utm_lat', float),
    Field('utm_lon', float)
)

ShotSpotterEvent = collection(
    'shot_spotter_event', db_session,
    Field('_id', schema.ObjectId),
    Field('Coverage_Area', str),
    Field('Incident_ID', str),
    Field('Date_Time', datetime),
    Field('Type', str),
    Field('lat', float),
    Field('lon', float),
    Field('utm_lat', float),
    Field('utm_lon', float)
)