#!/usr/bin/env python3

# Bring "libs" onto the path
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'scripts','libs')))

from postConf import PostConfig

if __name__ == "__main__":

  conf_filename='../conf/realtime.yaml'   # should be extracted from the command line options

  #
  # Use Class PostConfig
  #
  # To refer to variable using dot notation
  #
  config = PostConfig.fromfilename(conf_filename)

  #
  # Refer to variable directly
  #
  print(config.realtime)
  print(config.imagedir)
  print(config.scriptdir)

  #
  # Plotting fields is an array and each element is field_name -> field_detail
  # and the field_detail is a dict again with keys:
  #    var_name
  #    var_thresh
  #    var_label
  #    var_units
  #
  # After casting the dict variable to PostConfig object, we can refer to
  # each key,value using dot notation
  #
  for field in config.fields:
      for k,v in field.items():
        fd=PostConfig(v)  # fdetail is now a dictionary, should be casted to PostConfig object again
        print(fd.var_name)



