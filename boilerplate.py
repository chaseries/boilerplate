#! /usr/local/bin/python3
import argparse
import os
import itertools

CSS_LINK = "<link rel=\"stylesheet\" type=\"text/css\" href=\"css/main.css\">"
JS_LINK = "<script src=\"js/main.js\"></script>"
JS_PLACEHOLDER = "<!-- js -->"
CSS_PLACEHOLDER = "<!-- css -->"

js_map = { 
  JS_PLACEHOLDER: JS_LINK,
}

css_map = {
  CSS_PLACEHOLDER: CSS_LINK
}

parser = argparse.ArgumentParser()

parser.add_argument(
    "-css",
    help="Include a default CSS file.",
    action="store_true")

parser.add_argument(
    "-js",
    help="Include a default JavaScript file.",
    action="store_true")

args = parser.parse_args()

def handle_js():
  try:
    os.mkdir(os.path.join(os.getcwd(), "js"))
  except OSError:
    print("Creation of JavaScript directory failed.")

def handle_css():
  try:
    os.mkdir(os.path.join(os.getcwd(), "css"))
  except:
    print("Creation of CSS directory failed.")

def modify_index(js=False, css=False):
  dirname = os.path.dirname(os.path.realpath(__file__))
  input_template = os.path.join(dirname, "templates/basic.html")
  output_template = os.path.join(os.getcwd(), "index.html")
  with open(input_template, "r") as input_file, open(output_template, "w") as output_file:
    for line in input_file:
      whitespace = "".join(itertools.takewhile(str.isspace, line))
      stripped_line = line.strip()

      if stripped_line in js_map:
        if args.js:
          output_file.write(whitespace + js_map[stripped_line] + "\n")
        else:
          continue

      if stripped_line in css_map:
        if args.css:
          output_file.write(whitespace + css_map[stripped_line] + "\n")
        else:
          continue

      if stripped_line not in css_map and stripped_line not in js_map:
        output_file.write(line)


if __name__ == '__main__':
  if args.js:
    handle_js()
  if args.css:
    handle_css()
  modify_index(args.js, args.css)

