These are the shell permissions that we shall use for the Linux programming bash.

# Basic commands
1. ***chmod***  - modify the file access rights
2. ***su***     - temporarily become the super user
3. ***sudo***   - temporarily become a super user
4. ***chown***  - change file ownership
5. ***chgrp***  - change a file's group ownership
6. ***whoami*** - Who is the current super user

***To see teh permissions of a specific file***
we use `ls -l`

## File permission values
- **777** - No restrictions
- **755** - File's owner may read, write and execute for all users
- **700** - Only the file owner has the rights.
- **666** - All users may read and write the file.
- **644** - Owner may read and write a file while the other users may only read the file
- **600** - Owner may read and write . Other users have no rights

## Directory permission values
- **700** - Only the owner can have the full rights
- **755** - Owner has full access. Other users can list  but cannot delete or create.
- **777** - No restrictions.

## 0x01. Shell, permissions

[0-iam_betty](./0-iam_betty)  - Create a script that changes your user ID to betty. You should use exactly 8 characters for your command (+1 character for the new line). You can assume that the user betty will exist when we will run your script

[1-who_am_i](./1-who_am_i) - Write a script that prints the effective userid of the current user.

[4-empty](./4-empty) - Write a script that creates an empty file called hello.

[2-groups](./2-groups) - Write a script that prints all the groups the current user is part of.

[3-new_owner](./3-new_owner) - Write a script that changes the owner of the file hello to the user betty.

[5-execute](./5-execute) - Write a script that adds execute permission to the owner of the file hello. The file hello will be in the working directory

[6-multiple_permissions](./6-multiple_permissions) - Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file hello. The file hello will be in the working directory.

[7-everybody](./7-everybody) - Write a script that adds execution permission to the owner, the group owner and the other users, to the file hello. The file hello will be in the working directory,  You are not allowed to use commas for this script

[8-James_Bond](./8-James_Bond) - Write a script that sets the permission to the file hello as follows:
Owner: no permission at all
Group: no permission at all
Other users: all the permissions
The file hello will be in the working directory You are not allowed to use commas for this script

[9-John_Doe](./9-John_Doe) - Write a script that sets the mode of the file hello to this:
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
The file hello will be in the working directory
You are not allowed to use commas for this script

[10-mirror_permissions](./10-mirror_permissions) - Write a script that sets the mode of the file hello the same as olleh’s mode.
The file hello will be in the working directory
The file olleh will be in the working directory

[11-directories_permissions](./11-directories_permissions) - Create a script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed.

[12-directory_permissions](./12-directory_permissions) - Create a script that creates a directory called dir_holberton with permissions 751 in the working directory.

[13-change_group](./13-change_group) - Write a script that changes the group owner to holberton for the file hello
The file hello will be in the working directory

[14-change_owner_and_group](./14-change_owner_and_group) - Write a script that changes the owner to betty and the group owner to holberton for all the files and directories in the working directory.

[15-symbolic_link_permissions](./15-symbolic_link_permissions) - Write a script that changes the owner and the group owner of the file _hello to betty and holberton respectively.
The file _hello is in the working directory
The file _hello is a symbolic link

[16-if_only](./16-if_only) - Write a script that changes the owner of the file hello to betty only if it is owned by the user guillaume.
The file hello will be in the working directory

[100-Star_Wars](./100-Star_Wars) - Write a script that will play the StarWars IV episode in the terminal.
