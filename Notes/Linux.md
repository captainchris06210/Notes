                        
                        # ---- [LINUX TIPS & TRICKS] ---- #
                        
                [<Go Back](index)
                
# -- [ USEFUL COMMAND ] -- #

        ## MOUNT USBSTICK WITH PERMISSIONS ## 
               sudo mount /dev/sdb1 /home/captainchris/mount/ -o umask=000

        ## LIST ALL MAN PAGES ##
                man -k zathura
                
         ## XRANDR DEFAULT MODE ##
                xrandr --output DVI-I-0 --mode 1280x1024
                
        ## TURN OFF THE MONITOR ##
                xset dpms force off
                
# -- [ GREP / PDFGREP ] -- #

        ## ARGS ##
                -n              Show number lines
                -r              Recursive
                -i              Ignore sensitive case 
                
        ## SEARCH OCCURENCE IN PDF(RECURSIVE) ##
                pdfgrep -nri 'emplace_back'
                
        ## SEARCH IN FILES ##
                grep -nri "occurence" 
                
        ## SEARCH TWO DIFFERENT WORDS ##
                egrep -w 'word|word2' <folder>
                
# -- [ FIND ] -- #

        ## SEARCH CASE SENSITIVE REGARDLESS ##
                find /home/captainchris -iname file.txt
                
        ## SEARCH PATTERNS ##
                find /home/captainchris -name '*.mp3'
                
        ## SEND OUTPUT FROM COMMAND TO A FILE
                find /home/captainchirs -name *.mp3 > output.txt

# -- [ FFMPEG ] -- #

        ## ARGS ##
                -f x11grab                      Record from screen
                -s 1280x1024                    Record Size
                -r 30                           Frame per second
                -f pulse/alsa                   Record audio from pulse or alsa
                -i default                      Uses delfault input device for recording
                -c:v libx264                    Setting Video Codec
                -c:a flac                       Setting Audio Codec
                -y                              Overwrite output file
        ## TRANSFORM ALL MP4 IN MP3 ##
                ```sh
                for f in *.mp4;
                do ffmpeg -i "$f" -q:a 0 -map a "Output/${f%.mp4}.mp3"
                done
                ```
                
        ## RECORD A WEBCAM ##
                ffmpeg -y -i /dev/video0 output.mkv
                
        ## RECORD DESKTOP AND AUDIO AT THE SAME TIME 
                
                ```sh
                ffmpeg -y -f x11grab -s $(xdpyinfo | grep dimensions | awk '{print $2;} \
                -i :0.0 \
                -f alsa -i default \
                -c:v libx264 -r 30 -c:a flac $filename 
                ```

