# Generated by Django 5.1.2 on 2024-11-28 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_remove_message_is_read_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageAttachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='attachments/%Y/%m/%d/')),
                ('original_name', models.CharField(max_length=255)),
                ('file_type', models.CharField(max_length=50)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='attachments',
            field=models.ManyToManyField(blank=True, related_name='messages', to='chat.messageattachment'),
        ),
    ]
