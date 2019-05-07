# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Book(models.Model):
    primarykey = models.AutoField(primary_key=True)
    book_id = models.IntegerField()
    chapter_id = models.IntegerField()
    chapter_name = models.CharField(max_length=45, blank=True, null=True)
    chapter_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'book'
    def __unicode__ (self):
        return self.chapter_name


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=45, blank=True, null=True)
    book_author = models.CharField(max_length=45, blank=True, null=True)
    book_summary = models.TextField(blank=True, null=True)
    book_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'books'
    def __unicode__ (self):
        return self.book_name
