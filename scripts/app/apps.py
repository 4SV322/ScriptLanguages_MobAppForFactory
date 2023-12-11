from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        # Создаём миграцию для добавления новых полей в модель `Account`
        from django.db.migrations import Migration
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute('ALTER TABLE "accounts_account" ADD COLUMN "reading" FLOAT;')
            cursor.execute('ALTER TABLE "accounts_account" ADD COLUMN "stamp" VARCHAR(100);')
            cursor.execute('ALTER TABLE "accounts_account" ADD COLUMN "comment" VARCHAR(100);')

        Migration(self.name, '0002_add_fields').apply()
