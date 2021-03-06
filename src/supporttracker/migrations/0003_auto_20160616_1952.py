# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 19:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('supporttracker', '0002_auto_20160616_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_name', models.CharField(max_length=20)),
                ('information', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered', models.BooleanField(default=True)),
                ('left_message', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ContactRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referred_by', models.IntegerField(blank=True, null=True)),
                ('referral_note', models.CharField(blank=True, max_length=500)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('stage', models.CharField(choices=[('GET_INFO', 'Gather contact information'), ('MESSAGE', 'Need to send letter/message'), ('CALL', 'Need to call'), ('MEET', 'Meeting scheduled'), ('THANK', 'Send thank you'), ('FOLLOW_UP', 'Need to follow up'), ('STOP', 'Do not pursue further'), ('WAIT', 'Wait for a period of time'), ('MAINTAIN', 'Maintain')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254)),
                ('nickname', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('method', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_mailed', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('note', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_to_send', models.DateField(blank=True, null=True)),
                ('date_entered', models.DateField(default=datetime.date.today)),
                ('method', models.TextField(blank=True)),
                ('note', models.TextField(blank=True)),
                ('sent', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('spouse_name', models.CharField(blank=True, max_length=120)),
                ('street_address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, choices=[('', ''), ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachussets'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2, null=True)),
                ('zip', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', localflavor.us.models.PhoneNumberField()),
                ('nickname', models.CharField(blank=True, max_length=15)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_referred', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('referred_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referred', to='supporttracker.Person')),
                ('referring_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='referrer', to='supporttracker.Person')),
                ('staff_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remind_date', models.DateField(blank=True, null=True)),
                ('date_added', models.DateField()),
                ('note', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person')),
                ('staff_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='SupportRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('frequency', models.CharField(choices=[('Monthly', 'Monthly'), ('Quarterly', 'Quarterly'), ('Annually', 'Annually'), ('Semi-annually', 'Semi-annually'), ('One-time', 'One-time')], max_length=255)),
                ('start_date', models.DateField()),
                ('note', models.TextField(blank=True)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True, null=True)),
                ('staff_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile')),
                ('supporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ThankYou',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('sent', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person')),
                ('staff_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='VoiceMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_left', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person')),
                ('staff_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='note',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='message',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='letter',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='letter',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='followup',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='followup',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='contactrelationship',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='contactrelationship',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='call',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
        migrations.AddField(
            model_name='call',
            name='staff_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.UserProfile'),
        ),
        migrations.AddField(
            model_name='call',
            name='voice_mail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supporttracker.VoiceMail'),
        ),
        migrations.AddField(
            model_name='additionalinformation',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supporttracker.Person'),
        ),
    ]
