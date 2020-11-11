                                        # ----[WRITE WM TILLING MANAGER]---- #
                                        
                [<GO Back](index)
                
        TODO:
                - [X] Step 1 Setup and Teardown
                - [ ] Step 2 Initialization  
        
        Original Post: https://jichu4n.com/posts/how-x-window-managers-work-and-how-to-write-one-part-i/ 
        Window manager is a client of X server.
        
        
# --[SCHEMATICS]-- #
                 D = Down Arrow U = Up arrow
        
                                APP                  APP
                                  D U                D U
        WINDOW MANAGER          GUI FRAMEWORK   GUI FRAMEWORK
          D   U                    D U                D U
                                XSERVER        
            D U                   U         U
        VIDEO CARD              MOUSE   KEYBOARD 
        
        In modern GUI we use term widget or control, 
        In term application we use container instead widget.
         
        In windows is any rectangular area that is unit of user interaction
        
        The mechanism that allows a window manager to intercept such requests is called
        substructure redirection 
        
        Redirection means that an event is sent to the client selecting redirection (WM)
        
        <urSchema 2:>
        
               APP              WM
                D               D U                                    
                D               D U                                    
                D               D U                                    
                D               D U                                     
                     XSERVER                                          

                      1. App sends request to Xserver                                                           
                      2. Xserver routes request to window manager (XSERVER UP TO WM)                                                   
                      3. Window Manager grants,modifies,or denies request(DOWN TO XSERVER)

        Buttons minimizing maximizing and closing window are not create by the application but by the window manager
        via a process known as reparenting of framing 
        
# -- [WM CREATION] -- #
        
                1. Create a Root window
                2. When a top level window W is mapped (first shown),
                   The window manager is notfied by substructure redirection on the root
                   and the toplevel window is a direct child of the root windows
                3. The root window creates a frame F and reparent W to F.
                
       
       XCB is asynchron. The advantage is we have 5 windows at once. In XCB we can fire of all 5 requests to X server
       and then wait for all of them to return.
       
       XLIB is synchron. we have send one request at a time
      
# --[MAPPING(SHOW) A WINDOW]-- #
        
                 1. Recall that Create a frame window f
                 2. Register for substructure redirect on f with XSelectInput().
                    Recall that substructure redirect only applies to direct 
                    child windows, so after reparenting, the substructure 
                    redirect previously registered on the root window would no 
                    longer apply to w, hence this step.
                3. Make w a child of f with XReparentWindow().
                4. Render f and w with XMapWindow().
                5. Register for mouse or keyboard shortcuts on w and/or f.
                   Make w a child of f with XReparentWindow().
                   

                
        
        
       
       
