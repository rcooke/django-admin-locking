from django.core.management.base import BaseCommand, CommandError

from locking.models import Lock


class Command(BaseCommand):
  help = 'Remove expired lock records, just wasting space they are.'

  def handle(self, *args, **options):
    num_removed = Lock.objects.delete_expired()
    if num_removed > 0:
      self.stdout.write(self.style.SUCCESS('Removed %s expired lock(s).' % str(num_removed)))
    else:
      self.stdout.write(self.style.SUCCESS('No expired locks to remove.'))

