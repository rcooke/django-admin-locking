from django.core.management.base import BaseCommand, CommandError

from locking.models import Lock


class Command(BaseCommand):
  help = 'Remove expired lock records, just wasting space they are.'

  def handle(self, *args, **options):
    Lock.objects.delete_expired()
    self.stdout.write(self.style.SUCCESS('Successfully removed expired locks, if any. '))

