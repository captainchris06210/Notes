                
                                # ---- [PYGAME HOWTO] ---- #
                         
                         
                [ < GO BACK ](index.md)
                
        # --[CREATE SPRITE GROUP] -- #
                
                ```python
                        self.ships = Group()    # Create empty group
                        for ship_number in range(self.stats.ships_left):
                            # Call the CTOR
                            ship = Ship(self.ai_settings, self.screen)

                            # Positionning the ship 
                            ship.rect.x = 10 + ship_number * ship.rect.width
                            ship.rect.y = 10

                            self.ships.add(ship) ### Add new ship to the group
                  ``` 
