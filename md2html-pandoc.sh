#!/bin/sh
function md2html(){
  for fullname in `ls $1`
  do
    name=${fullname%.*}
    ext=${fullname##*.}
    if [ "$ext"x = "md"x ]
    then
      echo $name'☑️'
      pandoc $name.md -s -c lrda.css --self-contained -o $name
    fi
  done
}

IFS=$'\n'
INIT_PATH=".";
md2html $INIT_PATH
echo '///// HTML fires Generated 🚀!!! /////'