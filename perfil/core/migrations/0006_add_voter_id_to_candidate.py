# Generated by Django 2.1.1 on 2018-09-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("core", "0005_make_number_optional_in_candidate")]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="voter_id",
            field=models.CharField(blank=True, default="", max_length=12),
        ),
        migrations.AddIndex(
            model_name="candidate",
            index=models.Index(
                fields=["voter_id"], name="core_candid_voter_i_f35f83_idx"
            ),
        ),
    ]
