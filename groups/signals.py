from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StudentRating
from course.models import Review


@receiver(post_save, sender=Review)
def update_student_rating(sender, instance, **kwargs):
    student = instance.student
    course = instance.course

    rating_obj, created = StudentRating.objects.get_or_create(
        student=student,
        group__course=course,  
        defaults={"score": instance.rating}
    )
    rating_obj.score = instance.rating
    rating_obj.save()

    group_ratings = StudentRating.objects.filter(group__course=course).order_by('-score')
    position = 1
    for r in group_ratings:
        r.position_in_group = position
        r.save(update_fields=['position_in_group'])
        position += 1

    center_ratings = StudentRating.objects.all().order_by('-score')
    position = 1
    for r in center_ratings:
        r.position_in_center = position
        r.save(update_fields=['position_in_center'])
        position += 1
