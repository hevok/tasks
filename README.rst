=====
Tasks
=====
This application utilizes semantictasks to add semantic to Denigma task management.

1. Include semantictasks in your project folder and execute the RUNME in it:

    bash RUNME.sh

2. Install tasks

    pip install -e https://github.com/denigma/tasks

3. Add tasks to the installed applications:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'tasks',
        ...
    )

4. Add semantictasks static files in the settings to the static files directory:

.. code-block:: python

    STATICFILES_DIRS = ('static', 'semantictasks')

5. Include the tasks URL mappings in the global URLconf:

.. code-block:: python

    urlpatterns = patterns('',
        ...
        url(r'^tasks/', include('tasks.urls')),
        ...
    )

