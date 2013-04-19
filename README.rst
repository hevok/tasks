=====
Tasks
=====
This application utilizes semantictasks to add semantic to Denigma task management.

1. Include semantictasks in your project folder and execute the RUNME in it:

    bash RUNME.sh

2. Add tasks to the installed applications:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tasks',
        ...
    )

3. Add semantictasks static files in the settings to the static files directory:

.. code-block:: python

    STATICFILES_DIRS = ('static', 'semantictasks')

