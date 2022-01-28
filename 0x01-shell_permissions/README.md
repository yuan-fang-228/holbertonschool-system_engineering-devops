 # 0x01. Shell, permissions
 0. switches the current user to the user betty - scripts: su betty
 1. prints the effective username of the current user - scripts: whoami
 2. prints all the groups the current user is part of. - scripts: groups
 3. changes the owner of the file hello to the user betty - scripts: sudo chown betty hello 
 4. creates an empty file called hello - scripts: touch hello
 5. adds execute permission to the owner of the file hello - scripts: chmod +x hello
 6. adds execute permission to the owner and the group owner, and read permission to other users, to the file hello. - scripts: chmod ug+x,o+r hello
 7. adds execution permission to the owner, the group owner and the other users, to the file hello - scripts: chmod a+x hello
 8. sets the permission to the file hello as follows: Owner: no permission at all Group: no permission at all Other users: all the permissions - scripts: chmod 007 hello
 9. sets the mode of the file hello - scripts:chmod 753 hello
 10. sets the mode of the file hello the same as olleh’s mode. - scripts: chmod --reference=olleh hello
 11. adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users - scripts: chmod a+X *
 12. creates a directory called my_dir with permissions 751 in the working directory. - scripts: mkdir -m 751 my_dir
 13. changes the group owner to school for the file hello - scripts: chgrp school hello
 14. changes the owner to vincent and the group owner to staff for all the files and directories in the working directory - scripts: chown -R vincent:staff ./
 15. changes the owner and the group owner of _hello to vincent and staff respectively. - scripts: chown -h vincent:staff _hello
 16. changes the owner of the file hello to vincent only if it is owned by the user guillaume - scripts: chown --from=guillaume vincent hello
 17. play the StarWars IV episode in the terminal - scripts: telnet towel.blinkenlights.nl