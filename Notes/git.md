      						  										# ---- [GIT] ---- #

      [< GO BACK](index) 
                

	Remove GIT to the current folder			<tbrm -rf .git>
	Identify to github										<tbgit config user.email "you@github.com" / user.name "name">
	Create new local repository:					<tbgit init>
	Download from an existing repository:	<tbgit clone url>

	List files not commited:							<tbgit status>
	Show full change history:							<tbgit log>

# -- [BRANCHES] -- #
	
	List all branches:										<tbgit branch -a>
	List Remote branches:							    <tbgit branch -r>
	Local branch only											<tbgit branch -l / git branch>
	Delete branch													<tbgit branch -d [local branch] >
	Swith to branch branch names:					<tbgit switch -c "branch-name">
	Merge branch-name to current branch:	<tbgit merge branch-name>
	Add file to stagging environment,ready for commit			
					<tbgit add [file-name] / [folder] >
	Commit all stagged files to versionned history	
					<tbgit commit -m "Your message about the commit">
	Add remote repository URL															
					<tbgit remote add origin url>
	Fetch latest changes from origin and merge			
					<tbgit pull origin branch-name>
	Push local changes to the origin			
					<tbgit push origin branch-name>


# -- [STAGGING] -- #
	
	Remove single file from the stagging area					
					<tbgit reset HEAD -- [file] / [directory] >
	Remove commit from local repository            
					<tbgit reset --soft HEAD^>
	Rewrite reset index
					<tbgit rm --cached -r .>
	Remove every file from git's index 
					<tbgit reset --hard>

	 [DESC]
	Put your desc into README.md and add it to stagging
	Image ![Alt text](Sokoban.png?raw=true "Sokoban")
 	 
# -- [PROCESS] -- #

	## [INIT] ##
	1. git init 
	2. git status (Index files)
	3. git add <filename>
	4. git commit -m "Your message about the commit"

	## [BRANCHES(PENDING)] ##
	4. Create new branch git checkout -b new-branch
	5. To merge branch: git merge new-branch

	## [UPLOAD TO REPOSITORY] ##
	6. git remote add origin https://github.com/captainchris06210/config.git
	7. git push -u origin master


# -- [VOCABULARY] -- # 

  Staging(index)
  Commit: is a record of what files you have changed since the last time


