# Generated by Django 4.2.4 on 2023-08-10 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Afterschool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=20, verbose_name='동 명')),
                ('title', models.CharField(max_length=20, verbose_name='프로그램명')),
                ('receipt_start', models.DateTimeField(verbose_name='접수 시작 날짜')),
                ('receipt_end', models.DateTimeField(verbose_name='접수 마감 날짜')),
                ('training_start', models.DateTimeField(verbose_name='교육 시작 날짜')),
                ('training_end', models.DateTimeField(verbose_name='교육 마감 날짜')),
                ('day', models.CharField(choices=[('월요일', '월요일'), ('화요일', '화요일'), ('수요일', '수요일'), ('목요일', '목요일'), ('금요일', '금요일'), ('토요일', '토요일'), ('일요일', '일요일')], max_length=20, verbose_name='요일')),
                ('tuition', models.IntegerField(verbose_name='수강료')),
                ('number_of_member', models.IntegerField(verbose_name='정원')),
                ('status', models.CharField(choices=[('접수 전', '접수 전'), ('접수중', '접수중'), ('접수마감', '접수마감')], default='접수중', max_length=20, verbose_name='상태')),
            ],
        ),
        migrations.CreateModel(
            name='RegionAndMulticultural',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='제목')),
                ('content', models.CharField(max_length=100, verbose_name='내용')),
                ('phone', models.CharField(max_length=20, verbose_name='전화번호')),
                ('support_cycle', models.CharField(choices=[('일', '일'), ('월', '월'), ('년', '년')], default='일', max_length=20)),
                ('type', models.CharField(max_length=20, verbose_name='제공 유형')),
                ('department', models.CharField(max_length=20, verbose_name='담당 부서')),
                ('tag', models.CharField(choices=[('태그1', '태그1'), ('태그2', '태그2')], default=None, max_length=20, verbose_name='태그')),
                ('category', models.CharField(choices=[('지역', '지역'), ('다문화', '다문화')], default='일', max_length=20, verbose_name='지역/다문화 정보')),
            ],
        ),
    ]
