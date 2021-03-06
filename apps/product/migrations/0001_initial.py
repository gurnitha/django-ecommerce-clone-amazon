# Generated by Django 3.2.5 on 2021-10-11 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(help_text='Field ini tidak boleh dikosongkan.', max_length=255)),
                ('url_slug', models.CharField(help_text='Field ini pre-populated diambil dari title.', max_length=255)),
                ('thumbnail', models.FileField(blank=True, help_text='Field untuk foto produk kategori.', upload_to='')),
                ('description', models.TextField(blank=True, help_text='Field untuk deskripsi produk, boleh dikosongkan.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Field waktu ini akan terisi secara otomatis.')),
                ('is_active', models.IntegerField(default=1, help_text='Field ini bila nilainya lain selain 1, berarti tidak aktif.')),
            ],
        ),
    ]
