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

