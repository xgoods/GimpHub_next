#!/usr/bin/env python

from gimpfu import *
import os


def echo(*args):
  """Print the arguments on standard output"""
  print("echo:", args)

def get_group_layers(layers):
  # iterate layer groups, only goes one level deep right now
  for group in [group for group in gimp.image_list()[0].layers if pdb.gimp_item_is_group(group)]:
    # you want a group.name check here to pick a specific group
    for layer in group.layers:
      layers.append(layer)
  return layers

def get_all_layers(img):
  layers = []
  pdb.gimp_image_undo_group_start(gimp.image_list()[0])
  # iterate non-group layers
  for layer in img.layers:
      print(layer)
      layers.append(layer)

  layers = get_group_layers(layers)
  pdb.gimp_image_undo_group_end(gimp.image_list()[0])
  return layers

def convert_to_png(filename):

  img = pdb.gimp_file_load(filename, filename)

  filePath = os.path.dirname(filename)
  fullFilePath = os.path.join(filePath, "full.png")

  #for i, layer in enumerate(get_all_layers(img)):
  for i, layer in enumerate(pdb.gimp_image_get_layers(img)[1]):
      fName = os.path.join(filePath, "%d.png" % i)
      pdb.gimp_file_save(img, gimp.Item.from_id(layer), fName, fName)

  layer = pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
  pdb.gimp_file_save(img, layer, fullFilePath, fullFilePath)

  pdb.gimp_image_delete(img)

register("xfc-to-png", "", "", "", "", "",
  "<Toolbox>/MyScripts/XFV_TO_PNG", "",
  [
  (PF_STRING, "arg0", "argument 0", "test string"),  
  ],
  [],
  convert_to_png
  )

main()
