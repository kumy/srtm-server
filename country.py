#!/usr/bin/env python

try:
  import config
except:
  import sys
  print("Failed to load config, declare your conf in config.py. see config.py.ex")
  sys.exit(1)

import sqlalchemy

class Country:

  connection = None

  def __init__(self):
    engine = sqlalchemy.create_engine(config.dsn, pool_recycle=300)
    self.connection = engine.connect()
  
  def get_country(self, lat, lon):
    result = self.connection.execute("""SELECT iso_2 FROM boundaries
LEFT JOIN codes ON boundaries.iso1 = codes.ISO_3
WHERE ST_Contains(boundaries.shape, GeomFromText('POINT(%f %f)'))""" % (lon, lat)
)

    for row in result:
      return row['iso_2']
