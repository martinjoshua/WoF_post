#!/usr/bin/env python3

class PostConfig(dict):

    def __init__(self, config):
        super().__init__(config)

    def __getattr__(self, k):
        v = self[k]
        if isinstance(v, dict):
            return PostConfig(v)
        return v

    def __setattr__(self, k, v):
        raise Exception("PostConfig attribut <%s> read only."%k)
        return

    @classmethod
    def fromfilename(cls, filename):
        import yaml
        with open(filename,'r') as f:
            config = yaml.safe_load(f)
        return cls(config)

#endclass

if __name__ == "__main__":

  conf_filename='realtime.yaml'   # should be extracted from the command line options

  #
  # Use Class PostConfig
  #
  # To refer to variable using dot notation
  #
  config = PostConfig.fromfilename(conf_filename)

  print(config.imagedir)
  print(config.realtime)

  for field,fdetail in config.fields.items():
      fd=PostConfig(fdetail)  # fdetail is now a dictionary, should be casted to PostConfig object again
      print(fd.var_name)

  #
  # Direct method
  #
  # To refer to variable using nested brackets
  #
  import yaml

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


