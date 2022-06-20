# Generated by Django 4.0.4 on 2022-06-20 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post'),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_member', to='app.neighbourhood', verbose_name='NeighbourHood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Memberships',
            },
        ),
        migrations.AddField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.neighbourhood', verbose_name='NeighbourHood'),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Business Owner'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
