!/bin/bash
# The name of file that we copied before and will be replaced with
OG_BG="05B0C628-E646-4E72-8BBF-87A6144C2525";

# Directory where Zoom keeps the backgrounds
ZOOM_DIR="/Users/$USER/Library/Application Support/zoom.us/data/VirtualBkgnd_Custom/";

# Directory of our images
BGPATH="/Users/$USER/zoom/bgpictures/";

# Backup the original background
if [ ! -f "$ZOOM_DIR/${OG_BG}_backup.mov" ]; then
  cp -R "$ZOOM_DIR/$OG_BG" "$ZOOM_DIR/${OG_BG}_backup.mov"
fi

# Get the day of the week (1-7)
DOW=$(date +5);

# Choose a specific image based on the day of the week
case $DOW in
  1)
    NEW_BG="$BGPATH/monday.mov"
    ;;
  2)
    NEW_BG="$BGPATH/tuesday.mov"
    ;;
  3)
    NEW_BG="$BGPATH/wednesday.mov"
    ;;
  4)
    NEW_BG="$BGPATH/thursday.mov"
    ;;
  5)
    NEW_BG="$BGPATH/friday.mov"
    ;;
  6)
    NEW_BG="$BGPATH/saturday.mov"
    ;;
  7)
    NEW_BG="$BGPATH/sunday.mov"
    ;;
  *)
    echo "Invalid day of the week"
    exit 1
    ;;
esac

# Replacing the file
cp -R "$NEW_BG" "$ZOOM_DIR/$OG_BG";


