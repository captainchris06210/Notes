                                        # ---- [ ARCHLINUX ] ---- #
                                        
                                        
                [<GO Back](index)
                
# -- [ PACMAN ] -- #
        
        ## INSTALL OFFLINE DOC ##
                pacman -S arch-wiki-docs
                
        ## LIST FILES OF INSTALLED PACKAGES ##
                pacman -Ql <pkg>
                
        ## LIST ALL INSTALLED PACKAGES ##
                pacman -Qqe 
        
        ## SHOW PACKAGE INFORMATIONS ##
                pacman -Si <pkg>
                
        ## REMOVE PACKAGE WITH HIS DEPENCENCIES ##
                pacman -Rns <pkg>
        
        ## INSTALL PACKAGE FROM FILES ##
                pacman -U pkg.tar.xz
                
        ## LIST MANUALLY INSTALLED ##
                pacman -Qm
                
        ## DOWNLOAD PACKAGE WITHOUT INSTALL ##
                pacman -Sw <pkg>
        
        ## CLEAR CACHE ##
                pacman -Scc
                
        ## INSTALL DKMS MODULE ##
                
                dkms install nvidia/340.106 -k 4.4.46-lts
                
                * Change version number of nvidia and kernel 
                        
# -- [ PKGBUILD ] -- #
                epoch:		Used to force the package seend as newer than any previous version with a lower epoch.

                * Example:		1:5.13-2
                pkgver=5.13
                pkgrel=2
                epoch=1

