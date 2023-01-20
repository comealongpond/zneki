#!/usr/bin/bash

# Renames all sprite (png) files in directory
# "Walk (1).png" -> Walk_1.png

for FILE in ../sprites/the_knight/*; 
     do 
        new_name=$(echo $FILE | perl -pe 's/ \(([0-9]+)\)\.png/_$1.png/')
        mv -v "$FILE" "$new_name"; 
done

