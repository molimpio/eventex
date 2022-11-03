# Generated by Django 4.1.2 on 2022-11-03 16:41

from django.db import migrations


def copy_src_to_dst(Source, Destination):
    """
    Para cada ABC, instanciar um dst com todos os atributos
    Salvar o MTI
    Associar os speakers do src no dst
    Deletar o src
    """
    for src in Source.objects.all():
        dst = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots
        )
        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()


def forward_course_abc_to_mti(apss, schema_editor):
    copy_src_to_dst(
        apss.get_model('core', 'CourseOld'),
        apss.get_model('core', 'Course')
    )


def backward_course_abc_to_mti(apss, schema_editor):
    copy_src_to_dst(
        apss.get_model('core', 'Course'),
        apss.get_model('core', 'CourseOld')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti,
                             backward_course_abc_to_mti)
    ]
