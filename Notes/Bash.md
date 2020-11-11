																	# ---- [BASH SCRIPTING] ---- #
   
   
   
        # -- [ECHO & PRINTF] -- #
                
                ## PRINT VAR ## 
                        ```sh
                        var="10"
                        echo "$var"
                
                        printf "%s" "$var"
                        ```
                
        # -- [CASE CONDITION] -- #
                                ```sh
                                       case "$BLOCK_BUTTON" in
                                                5) decrease ;;
                                                4) increase ;;
                                                3) stop ;;
                                                1) start ;;
                                                2) pause ;;
                                        esac 
                                ```
                                
        # -- [IF CONDITIONS] -- #
                                ```sh
                                       var=1
                                       if [ "$var" == "1" ]; then 
                                       echo "blop"
                                        fi
                                ```
        # -- [READ FILE LINE BY LINE AND STORE INTO ARRAY] -- #
   
                                ```sh
                                file="voc.txt"
                                while read -r line;do
                                l+=( "$line" )
                                done < "$file"
                                ```
	# -- [CMUS SCRIPTING] -- #
                		```sh
				INFO_CMUS=$(cmus-remote -Q 2>/dev/null)
				if [[ $? -eq 0 ]]; then
					  INFO_TITLE=$(echo "${INFO_CMUS}" | sed -n -e 's/^.*title//p' | head -n 1)
					  INFO_ALBUM=$(echo "${INFO_CMUS}" | sed -n -e 's/^.*album//p' | head -n 1)
					  INFO_ARTIST=$(echo "${INFO_CMUS}" | sed -n -e 's/^.*artist//p' | head -n 1)
				else
				 exit
					fi

				if [[ "${INFO_ARTIST}" ]] && [[ "${INFO_TITLE}" ]]; then
				 OUT_TEXT="${INFO_ARTIST} - ${INFO_TITLE}"
				elif [[ "${INFO_TITLE}" ]]; then
				 OUT_TEXT="${INFO_TITLE}"
				fi

				echo "${OUT_TEXT}"
				echo "${OUT_TEXT}"
				exit
	                        ```
								

# --[ARRAY]-- #

			array=(Hello World)

			array[0]=Hello
			array[1]=world

			${array[*]} 									All of the items in the array
			${!array[*]}									All of the indexes in the array
			${#array[*]}									Number of the items in the array
			${#array[0]}									Length of item zero
			
	## ADD AN ELEMENT TO THE BEGINING OF ARRAY ##
	
		array=("new_element" "${array[@]}") 					
		array=("new_element1" "new_element2" "..." "new_elementN" "${array[@]}")

	## ADD AN ELEMENT TO THE END OF ARRAY ##

		array=( "${array[@]}" "new_element" )
		array+=( "new_element" )

		array=( "${array[@]}" "new_element1" "new_element2" "..." "new_elementN") #Or
		array+=( "new_element1" "new_element2" "..." "new_elementN" )

	##  ADD AN ELEMENT TO THE SPECIFIC INDEX ##
	
		array=( "${array[@]:0:2}" "new_element" "${array[@]:2}" )
	
	## REMOVE AN ELEMENT FROM ARRAY ##
	
		arr=( "${arr[@]:0:2}" "${arr[@]:3}" )

		Explanation: Remove the element #3. 
			     ${arr[@]:0:2} will get two elements arr[0] and arr[1] starts from the beginning of the array.
			     ${arr[@]:3} will get all elements from index3 arr[3] to the last.
					 
	## INCREMENT VAR IN BASH ##
		((var++))
		
	## LOOP OVER THE ARRAY 
		<TT>      I3:								
		<TT>      Client:
		<TT>      Launcher:
 		<TT>      Screen:
		<TT>      Layout:
		<TT>     Containers:

		for i in ${TITLE} output :			echo output example:
			<TT>					tmp=${title[idx]}			tmp=("$title[idx]}")
			I3:					 
			...				:OUTPUT:	<TT> I3:		<TT> I3:
		for i in "${TITLE} output:				
			<TT>	I3:				tmp=(${title[idx]})
			...				
							:OUTPUT:        <TT>
	
	## WORKS COMMANDS ##
	
		l[i]=$(echo "${l[i]}" | sed -e "s/<C>/${cmd}/g;s/<T>/${text}/g;")
		similar but in while loop	 line=${line/<P5>/} line=${line//<C>/$cmd} line=${line//<T>/$txt} p5+=( "$line" )

		In while read -r 
			
		Modify one occurence:
			title+=( "${line/<TT>/}" ) 

		Modify two occurences and store to the title
			/ for the first occurence // for all occurence in string
			line=${line//<[CT]>/} line=${line//<TT>/} title+=("$line")


	 	* few examples with sed 

	 	echo ${title[0]} | sed -e "s/<TT>//g     <- Remove <TT> from string

	## REPLACEMENT WITH SED ## 

	* SED argument 

		-n Quiet / -e script expression / -f script file / -s consider file as separate rather / -i edit file in place
		
	* Change all <C> TO $cmd  AND ALL <T> in  ${text} in string:

			sed -e "s/<C>/${cmd}/g;s/<T>/${text}/g;
	
	* Remove keywords in string:

			sed -i 's/bad//g' ${string}

