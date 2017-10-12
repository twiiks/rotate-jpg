if [ $# -lt 2 ]; then
  echo '$1 <Directory>, $2 <Angle>'
  exit
fi

echo 'hi'

for file in ./$1/*.jpg; do
  convert "$file" -quality 100 -distort SRT $2 "${file%.jpg}"_rot$2.jpg
done
