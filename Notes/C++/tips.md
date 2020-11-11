                                        
																				# ---- [C++ TIPS] ---- #

               [< Go Back](C++)

# -- [CLASS OBJECT AS POINTERS] -- #

				```cpp
						class Tilemap: public sf::Drawable, public sf::Transformable
						{
								class snippet
						}
				```		
					
				## [CREATE OBJECT] ##
					
						```cpp
								Tilemap *t = new Tilemap;
								t->loadfile("resources/map1.xml");
						```
					

# -- [SOME USEFUL TIPS] -- #
		
			<tbTO FIND AN INDEX IN MATRICE :> y * nElem + x
					
								int *data <- MyMap
							```cpp
							for( int y = 0; y < NB_TILE_HEIGHT; y++)
								for(int x =0; x < NB_TILE_WIDTH;x++)
								{
										x * nElem + y				// LOOP 0 32 64 96 128 ...
										data[y*NB_TILE_WIDTH+x]		// LOOP ALL VALUES IN DATA	
								}
								```
								
		## OTHER EXAMPLES ##
				
						```cpp
						int someArray[10] = { 3,6,9,12,15,18,21,24,27,30};
						
						int *pLocation0 =&SomeArray[0];
						for(int i=0; i < 10; i++)
						{
								//std::cout << someArray + i << "=" << *(someArray + i) << std::endl;
								std::cout << pLocation0 << " = " << *pLocation0 << std::endl;
								pLocation0++;
						}
						
						```
			## ALLOCATION ##
						
								struct sSomeObject
								{
										int x = 0xA3A2A1A0;
										int y = 0xB3B2B1B0;
										
										sSomeObject() // constructor
										{
												x = 0xC3C2C1C0;
												y = 0xD3D2D1D0;  
										}
								}
						
						
						Stack Allocation(COMPILATION TIME): sSomeObject pSomeObject[10];
						
						Heap(RUNTINE):			sSomeObject *pSomeObject = new sSomeObject[10]
								then delete		delete sSomeObject;
								
								
			* <tbPOINTERS OF ARRAY POINTERS:>
						
						Heap(RUNTIME) :			sSomeObject **pSomeObject = new sSomeObject*[10] { 0 };
						then delete		        delete[] pSomeObject;
						
		
		## TRANSFORMATION ##
				
				<tbTHIS CODE>
								```cpp
								if (bkey[0]) {

								if( DoesPieceFit(nCurrentPiece,nCurrentRotation,nCurrentX + 1, nCurrentY)) {
								nCurrentX = nCurrentX +1
								}
								```
				<tbBECOME>
					
					```CPP
				 	// if bkey[0] is pushed and DoesPieceFit return 1 or return 0 if it is false
					nCurrentX += (bKey[0] && (DoesPieceFit(nCurrentPiece,nCurrentRotation,nCurrentX + 1, nCurrentY)) ? 1 : 0
					```
								
				<tb AVOID IF LOOP>
					Example:    bGameOver = !(DoesPieceFit(nCurrentPiece,nCurrentRotation,nCurrentX + 1, nCurrentY))
                                                                
                
				## FILESTREAM #
				
					static_cast<new type(expression)
					
					// size_t is unsigned interger type 
					static_cast<size_t>length                       // Convert length to size_t
								
					Example:
								```cpp
								const size_t N=100
								int numbers[N]
				 				for(size_t ndx=0; ndx < N;++ndx)
								```
												
				## FLAGS ##
				
					 <tbstd::ios::app>                  Append content to an existing file. Otherwise the content will be deleted 
					 <tbstd::ios:ate>               Open file with position indicator to the end
									
                                
                              
                        
                
