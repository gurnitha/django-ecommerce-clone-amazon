### MEMBUAT ECOMMERCE 'CLONE AMAZON' DENGAN MENGGUNAKAN DJANGO VERSI 3.2


### --------------------------------------------------------------------
### 1. PRA-SYARAT
### --------------------------------------------------------------------


#### 1.1 Menginstal Python versi 3.9.5

#### 1.2 Menginstal Sublime Text Editor

#### 1.3 Menginstall Git


### --------------------------------------------------------------------
### 2. BASIC SETUP
### --------------------------------------------------------------------


#### 2.1 Membuat local virtualenv 'venv3932'

#### 2.2 Mengaktifkan venv3932

#### 2.3 Menginstall Django v3.2

#### 2.4 Membuat README.md file

#### 2.5 Membuat .gitignore file

#### 2.6 Meng-inisiasi git

#### 2.7 Menyimpan file ke dalam lokal repositori

        new file:   .gitignore
        new file:   README.md


### --------------------------------------------------------------------
### 3. REMOTE REPOSITORI
### --------------------------------------------------------------------


#### 3.1 Membuat remote repositori pada Github dan meng-upload files pada remote repositori

        modified:   README.md


### --------------------------------------------------------------------
### 4. MEMBUAT DJANGO PROJECT
### --------------------------------------------------------------------


#### 4.1 Membuat django proyek di dalam root direktori 'src' dengan nama 'config'

        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py


#### 4.2 Menjalankan server untuk melihat tampilan proyek

        modified:   .gitignore
        modified:   README.md
        new file:   config/__pycache__/__init__.cpython-39.pyc
        new file:   config/__pycache__/settings.cpython-39.pyc
        new file:   config/__pycache__/urls.cpython-39.pyc
        new file:   config/__pycache__/wsgi.cpython-39.pyc
        new file:   db.sqlite3


#### 4.3 House keeping - Membuat copy project dalam bentun src.rar file

        modified:   README.md


### --------------------------------------------------------------------
### 5. DATABASE - USING MYSQL DATABASE
### --------------------------------------------------------------------


#### 5.1 Create mysql database

        > mysql> CREATE DATABASE django_ecommerce_clone_amazon;
        modified:   README.md


#### 5.2 Install django-environ

        (venv3932) λ python -m pip install django-environ
        modified:   README.md


#### 5.3 Create .env file

        modified:   README.md

        NOTE: The .env files is not seen due to it ignore by the git


#### 5.4 Adding varables to .env file

        modified:   README.md

        NOTE: The .env files is not seen due to it ignore by the git


#### 5.5 Import environ to settings.py

        modified:   README.md
        modified:   config/settings.py


#### 5.6 Replace the SECRET_KEY with the SECRET_KEY variabble in .env file

        modified:   README.md
        modified:   config/settings.py


#### 5.7 Setup database kredensial pada settings.py menggunakan variabel pada .env file

        modified:   README.md
        modified:   config/settings.py


### --------------------------------------------------------------------
### 6. DJANGO ADMIN
### --------------------------------------------------------------------


#### 6.1 Menjalankan migrasi untuk membuat tabel-tabel default dari django

        modified:   README.md
        modified:   config/__pycache__/settings.cpython-39.pyc


#### 6.2 Membuat superuser

        modified:   README.md


### --------------------------------------------------------------------
### 7. DJANGO APP - main
### --------------------------------------------------------------------


#### 7.1 Membuat django app dengan nama 'main' di dalam folder apps

        modified:   README.md
        new file:   apps/main/__init__.py
        new file:   apps/main/admin.py
        new file:   apps/main/apps.py
        new file:   apps/main/migrations/__init__.py
        new file:   apps/main/models.py
        new file:   apps/main/tests.py
        new file:   apps/main/views.py


#### 7.2 Register 'main' app pada config/settings.py

        modified:   README.md
        modified:   apps/main/apps.py
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/settings.py


### --------------------------------------------------------------------
### 8. HALLO WORLD!
### --------------------------------------------------------------------


#### 8.1 Menampilkan 'Hallo World!' menggunakan HttpResponse

        modified:   README.md
        modified:   apps/main/apps.py
        new file:   apps/main/urls.py
        modified:   apps/main/views.py
        modified:   config/__pycache__/settings.cpython-39.pyc
        modified:   config/__pycache__/urls.cpython-39.pyc
        modified:   config/settings.py
        modified:   config/urls.py


### --------------------------------------------------------------------
### 9. MEMBUAT HOME PAGE
### --------------------------------------------------------------------


### 9.1 Membuat home page mengggunakan django Templates, Views dan Urls

        modified:   README.md
        new file:   apps/main/templates/main/index.html
        modified:   apps/main/urls.py
        modified:   apps/main/views.py


### --------------------------------------------------------------------
### 10. MEMBUAT PRODUCT APP
### --------------------------------------------------------------------


#### 10.1 Membuat folder app dengan nama 'product' di dalam folder 'apps'

        modified:   README.md


#### 10.2 Membuat 'product' app di dalam folder 'apps' 

        modified:   README.md
        new file:   apps/product/__init__.py
        new file:   apps/product/admin.py
        new file:   apps/product/apps.py
        new file:   apps/product/migrations/__init__.py
        new file:   apps/product/models.py
        new file:   apps/product/tests.py
        new file:   apps/product/views.py