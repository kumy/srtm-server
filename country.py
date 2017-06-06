#!/usr/bin/env python

try:
  import config
except:
  import sys
  print("Failed to load config, declare your conf in config.py. see config.py.ex")
  sys.exit(1)

from sqlalchemy import create_engine

engine = create_engine(config.dsn, pool_recycle=300)
connection = engine.connect()

class Country:

  def get_country(self, lat, lon):
    connection = engine.connect()
    try:
      connection.execute("SELECT 1")
    except:
      pass

    result = connection.execute("""
      SELECT iso_2 FROM boundaries
      LEFT JOIN codes ON boundaries.iso1 = codes.ISO_3
      WHERE ST_Contains(boundaries.shape, GeomFromText('POINT(%f %f)'))""" % (lon, lat)
      )

    for row in result:
      country = row['iso_2']
      connection.close()
      break
    return country
