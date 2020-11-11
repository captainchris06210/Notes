                        
                                        # ---- [COMPRESSSION] ---- #
                        
                [< GO BACK](index)
                        
        # -- [ZIP] -- #
        
                zip <file.zip> *.c *.h
                
                Recursive zip with folder 
                zip -r <file.zip> Folder/*
                
        # -- [UNZIP] -- #
        
                <tbunzip [options] filename>
                
                         Options:
                                        -d /path/location               Unzip to a different directory
                                        -j                              Unzip without creating new folder 
                                        -l                              Lists the contents of an archive without extracting it
                                        -P password                     Supplies a password to unzip protected archive
                                        -t                              Test whether a file is valid
                                        -x filename                     Extract 
                        
                        
        # -- [TAR] -- #
                        
                <tbtar -[options] file.tar.gz>
                
                        Options:
                                        -c                              Create an archive
                                        -x                              Extract a tar ball
                                        -v                              Verbose
                                        -f                              Specify an archive or a tarball filename
                                        -j                              Decompress
                                        -z                              Decompress and extract the contetns of compressed archive create by gzip(gz)
                                        
                <tbExtract tgz file>                    ->              tar -xvf filename.tgz
                <tbExtract tar.gz file>                 ->              tar -zxvf filename.tar.gz
                <tbExtract tar.bz2 file>                ->              tar -jxvf filename.tar.bz2
                
                <tbExtract into a different directory :> 
                
                                        tar -zxvf filename.tgz -C /<directory>
                                        tar -zxvf filename.tar.gz /<directory>
                                        tar -jxvf filename.tar.bz2 /<directory>
                        
              <tbCompress an entire directory or single file:>                 tar -czvf archive.tar.gz /folder
                                        
              <tbCompress Multiple directories or File at once:>               
                        
                        tar -czvf archive.tar.gz /home/ubuntu/Downloads /usr/local/stuff /home/ubuntu/Documents/notes.txt
                
                                        
                        
                        
                        
