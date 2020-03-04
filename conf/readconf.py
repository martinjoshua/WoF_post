#!/usr/bin/env python3

import yaml

conf_filename='realtime.yaml'   # should be extracted from the command line options

with open(conf_filename,'r') as conf_stream:
  #data = yaml.load(f, Loader=yaml.FullLoader)  # it requires PyYAML 5.1 and later
  conf_data = yaml.load(conf_stream)
  #print(conf_data)

for k,v in conf_data.items():
  if type(v) is list:  # list one element by one element
    print("%s: \tlen = %d "%(k,len(v)))
    for item in v:
      if type(item) is dict:    # dictionary
        for key, value in item.items():
          print("    %s = %s"%(key,value))
      else:
        print("    %s,"%item)
      #print("    %s,"%item)
  else:                # scalars
    print("%s = %s, \ttype - %s "%(k,v,type(v)))

