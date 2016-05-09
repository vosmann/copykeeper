#!/bin/bash

# Run install.sh beforehand.

# 1. Run periodically, e.g. hourly, and scan configured directories.
#    Schedule it with cron.
#    Run every minute.
#    If last run was more than e.g. 30 or 60 minutes ago, run. Else skip.

# source copykeep.conf

# 2. Produce status files by scanning local and remotes.
#
# filepath        size        md5sum    modtime               type    mutable/immutable
# /file.txt       123400      00aabb    2016-02-21-23:59      fridge  mutable
# /favorites.md   123400      44aabb    2016-01-28-20:00      fridge  versioned # every file gets a +1 version e.g. favorites.md.1
# /video.avi      993401      00aacc    2016-02-20-21:53      freezer immutable

function generate_timestamp() {
    local TIMESTAMP=`date -d "today" +"%Y-%m-%d-%H-%M"`
    echo $TIMESTAMP
}

function generate_status() {
    local LOCATION_NAME=$1
    local LOCATION_PATH=$2
    local TIMESTAMP=`generate_timestamp`
    find $LOCATION_PATH -type f > status.$TIMESTAMP.$LOCATION_NAME
}

generate_status local $PWD

# 3. Warns if he duplicates are found in any of the manifests.

# function check_duplicates() {
    # Generate list of duplicates
    # Generate list of files that can be kept
    # Generate list of duplicates that can be deleted (leave the one copy out)
#     if filepaths equal || md5sums equal
#         duplicate
# }

# 4. Compare local's and remotes' status and write a manifest saying which files will be copied or even overwritten.
#     if immutable
#         if (filepath, mdsum) not present on remote
#             copy
#     else if mutable
#         if filepaths equal && mdsums different 
#             overwrite or version
#         else
#             copy
#     else if versioned
#         if (filepath, mdsum) not present on remote
#             copy
# 
# 5. Copykeeper is used to back up data automatically from the local disk to the remote disk.

# 6. Copykeeper only reads data from remote and writes to local (bootstrapping sequence) after a fresh OS reinstall.

# 7. Copykeeper bootstrapping copies the remote directory structure for both fridge and freezer directories onto local. Fridge gets files copied, freezer only empty dir structure.


# ANSWER=`zenity --entry --text "Copykeeper has detected new files. Their full list is available at $NEW_FILES. Do you want to back them up? Currently keeping $FRIDGE_COUNT fridge files and $FREEZER_COUNT freezer files."`
# ANSWER=`zenity --entry --text "Copykeeper has detected duplicate files (identical content). Their full list is available at $DUPLICATE_FILES. Please delete duplicates."`
# Or use some sort of OS/display manager pop up.

