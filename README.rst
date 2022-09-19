pgbackup
=======

CLI for backup remote PostgreSQL database either locally or to s3

Preparing the Development
=========================

1. Ensure ``pip`` and ``pipven`` are installed
2. Clone repository: ``git clone git@github:example/pgbackup``
3. ``cd`` into the repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
=====

Pass in a full database URL, ther storage driver, and the destination

S3 Example w/ bucket name:

::

  $pgbackup postgresql://bob@example.com:5432/db_one --driver s3 backup

Local Example w/ local path

::

  $pgbackup postgresql://bob@example.com:5432/db_one --driver local /var/loval/backups

Running Test
============

Run test local using ``make`` if virtualenv is active:

::

  $make

If virtualenv isn't activate then use:

::

  $ pipenv run make
