parrot
======

password rotation tool
__Disclaimer: this is a noob-project, don't use it.__
Parrot should generate, store, stdout, change and rotate passwords. Passwords in config files (ie to access a database) should be exchanged (and the database updated).

Goals
-----

  *  Generate random password with upper/lower, numerical, punctuation - each to turn off by switch
  *  Encrypt those passwords by GPG
  *  Store the encrypted passwords in a structured way (see [pass](http://zx2c4.com/projects/password-store/))
  *  use git to monitor changes

Further: If the use of a password is given, perform rotation:

  *  use is a file -> substitute $old_pw with $new_pw and update the store (with date)
  *  use is a db -> login with $old_pw, substitute $old_pw with $new_pw, update store (with date)
  *  log changes and mail to admin (via git)

Languages
---------
The project will be python-only

Roadmap
-------
* generate random passwords    DONE (is this random?)
* encrypt password with gpg    TODO
* store passwords in a file    DONE (TODO add .gpg if encrypted)
* look up (encrypted) password TODO
* add use (config, db)         TODO
* rotate passwords             TODO
* store changes in git history TODO
