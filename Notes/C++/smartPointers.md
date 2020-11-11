                                
                                # ---- [SMART POINTERS]---- #
             
             [< GO BACK](C++)
             
     
# -- [SMART POINTERS] -- # 

        
        ## EXAMPLE STD::UNIQUE_PTR<T> ##
                ```cpp
                // DECLARATION IN FILE.HPP (CLASS)
                std::unique_ptr<Blocks> pBlock; 
                
                // INSTANTIATION IN FILE.CPP
                pBlock = std::make_unique<Blocks>(nbBlock,
                         sf::Vector2f(blockPos[i].x,blockPos[i].y));
                ``` 
                       
        ## EXAMPLE STD::SHARED_PTR<T> ##
        
                ```cpp
                // DECLARATION IN FILE.HPP(CLASS)
                std::shared_ptr<Blocks> pBlock;
                std::vector<std::shared_ptr<Blocks>> blockContainer;

                // INSTANTIATION IN FILE.CPP
                pBlock = std::make_shared<Blocks>(nbBlock,
                         sf::Vector2f(blockPos[i].x,blockPos[i].y));
                blockContainer.push_back(pBlock);
                
                // DRAW CONTAINERS
                for( int n = 0; n <= nbBlock;n++) {
                        window.draw(*blockContainer[n]);
                }
       
