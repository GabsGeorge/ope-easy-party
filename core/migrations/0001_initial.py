# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-23 20:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sysdiagrams',
            fields=[
                ('name', models.CharField(max_length=128)),
                ('principal_id', models.IntegerField()),
                ('diagram_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('definition', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sysdiagrams',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('codigo_cat', models.AutoField(db_column='Codigo_cat', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now_add=True, verbose_name='modificado em')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'Categoria',
                'ordering': ['nome'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Colaboradores',
            fields=[
                ('nome_c', models.CharField(db_column='Nome_C', max_length=100)),
                ('codigo_c', models.AutoField(db_column='Codigo_C', primary_key=True, serialize=False)),
                ('telefone_c', models.IntegerField(db_column='Telefone_C')),
            ],
            options={
                'db_table': 'Colaboradores',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contratos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(db_column='Descricao')),
                ('dia', models.DateField(db_column='Dia')),
                ('hora', models.TimeField(db_column='Hora')),
                ('endereco_ct', models.CharField(db_column='Endereco_CT', max_length=100)),
            ],
            options={
                'db_table': 'Contratos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('nome_f', models.CharField(db_column='Nome_F', max_length=100, primary_key=True, serialize=False)),
                ('email_f', models.CharField(blank=True, db_column='Email_F', max_length=100, null=True)),
                ('endereco_f', models.CharField(db_column='Endereco_F', max_length=255)),
                ('telefoneprincipal', models.IntegerField(db_column='TelefonePrincipal')),
                ('telefonesecundario', models.IntegerField(blank=True, db_column='TelefoneSecundario', null=True)),
                ('categoria_f', models.CharField(db_column='Categoria_F', max_length=100)),
            ],
            options={
                'db_table': 'Fornecedor',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('codigo_p', models.AutoField(db_column='Codigo_P', primary_key=True, serialize=False)),
                ('nome_p', models.CharField(db_column='Nome_P', max_length=100)),
                ('quantidade', models.SmallIntegerField(db_column='Quantidade')),
                ('imagem', models.ImageField(db_column='Imagem', upload_to='media')),
                ('descricao', models.TextField(db_column='Descricao_P')),
                ('custo_p', models.DecimalField(db_column='Custo_P', decimal_places=2, max_digits=10, verbose_name='Custo')),
                ('preco_p', models.DecimalField(db_column='Preço_P', decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('slug', models.SlugField(max_length=100, verbose_name='Identificador')),
                ('vender', models.BooleanField(db_column='Vender', default=True)),
                ('ativo', models.BooleanField(db_column='Ativo', default=True)),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now_add=True, verbose_name='modificado em')),
                ('categoria_p', models.ForeignKey(db_column='categoria_p', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Categoria')),
                ('nome_f', models.ForeignKey(db_column='Nome_F', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Fornecedor')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
                'db_table': 'Produto',
                'ordering': ['codigo_p'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo_u', models.AutoField(db_column='Codigo_U', primary_key=True, serialize=False)),
                ('nome_u', models.CharField(db_column='Nome_U', max_length=255)),
                ('usuario', models.CharField(db_column='Usuario', max_length=100, unique=True)),
                ('senha', models.CharField(db_column='Senha', max_length=100)),
                ('email_u', models.CharField(blank=True, db_column='Email_U', max_length=100, null=True)),
                ('cpf', models.IntegerField(db_column='CPF', unique=True)),
                ('telefone_u', models.IntegerField(db_column='Telefone_U')),
                ('endereco_u', models.CharField(db_column='Endereco_U', max_length=255)),
                ('news', models.NullBooleanField(db_column='News')),
            ],
            options={
                'db_table': 'Usuario',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='contratos',
            name='codigo_u',
            field=models.ForeignKey(db_column='Codigo_U', on_delete=django.db.models.deletion.DO_NOTHING, to='core.Usuario'),
        ),
    ]