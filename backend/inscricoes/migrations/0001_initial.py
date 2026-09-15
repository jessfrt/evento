from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_participante', models.CharField(max_length=150)),
                ('email_participante', models.EmailField(max_length=254)),
                ('data_inscricao', models.DateTimeField(auto_now_add=True)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
    ]
