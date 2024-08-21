from django.db import migrations, models
import django.db.models.deletion

def populate_role(apps, schema_editor):
    entries = {
        "member": "A member of the site",
        "editor": "Someone who can edit others' posts",
        "moderator": "Someone who can edit posts and moderate editors"
    }

    Role = apps.get_model("accounts", "Role")
    for key, value in entries.items():
        role_obj = Role(name=key, description=value)
        role_obj.save()

def populate_team(apps, schema_editor):
    entries = {
        "alpha": "The A team", 
        "bravo": "The B team",
        "charlie": "The C team"
    }
    Team = apps.get_model("accounts", "Team")
    for key, value in entries.items():
        team_obj = Team(name=key, description=value)
        team_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # Ensure this points to your initial migration
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Role', blank=True, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Team', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(populate_role),
        migrations.RunPython(populate_team),
    ]
