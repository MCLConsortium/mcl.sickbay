# 👩‍⚕️ MCL Sickbay

"MCL Sickbay" is the data model and object-relational mapping for the clinical data application of the [Consortium for Molecular and Cellular Characterization of Screen-Detected Lesions](https://mcl.nci.nih.gov/).


## 🏃‍♀️ Getting Started

The "Sickbay" software provides a [Python](https://python.org/) based API into a data model (a series of related classes) and takes advantage of [SQLAlchemy](https://www.sqlalchemy.org/) as the object-relational mapper. This section will help you get started.


### 📀 The Database

For this project, we're using [PostgreSQL](https://www.postgresql.org). You can create a PostgreSQL database to use with this software as follows:

```console
dropdb --if-exists clinical_data
dropuser --if-exists mcl

createuser \
    --createdb \
    --inherit \
    --login \
    --no-createrole \
    --no-superuser \
    mcl


createdb --encoding=UTF8 --owner=mcl clinical_data
```


### 🖥 The Software

To use this software, simply add `mcl.sickbay` as a dependency to your project or install it into your Python virtual environment.

You can develop, build, and test the package locally as follows:

```console
python3 -m venv venv
venv/bin/pip install --quiet --upgrade setuptools pip wheel build
venv/bin/pip install --editable .
```

You can run `venv/bin/create-clinical-db` to populate a PostgreSQL database with the schema of the Sickbay data model. Add `-add-test-data` to include some test data or `--add-sample-data` to add some sample data (or use both!).

To build and publish this software, try [build](https://pypi.org/project/build/) and [Twine](https://twine.readthedocs.io/).


### 🔢 Versioning

We use the [SemVer](https://semver.org/) philosophy for versioning this software. For versions available, see the [release history](https://pypi.org/project/mcl.sickbay/#history).


## 📦 Additional Resources

Some resources that provide further context for this software are as follows:

-   [Sample data, presentations, mockups, etc.](https://drive.google.com/drive/folders/1oXqRl-Aw2TSF70D9sPJaW99F9hyPiFHY?usp=sharing)
-   [Common Data Elements](https://mcl.nci.nih.gov/resources/standards/mcl-cdes)


## 👥 Contributing

Well it's wide open right now, but later you might look at [open issues](https://github.com/MCLConsortium/mcl.sickbay/issues), forking the project, and submitting a pull request.


## 📃 License

The project is licensed under the [Apache version 2](LICENSE.txt) license.


