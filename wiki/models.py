from django.db import models
import markdown


class Page(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    body = models.TextField()

    def __unicode__(self):
        return self.title

    @classmethod
    def exist(cls, title):
        """ check if title exist and return page or None

        >>> Page.exist('not') is None
        True
        >>> page = Page(title='yes', body='')
        >>> page.save()
        >>> Page.exist('yes') == page
        True
        """
        try:
            page = cls.objects.get(title=title)
        except cls.DoesNotExist:
            page = None
        return page

    @classmethod
    def upsert(cls, title, body):
        """ given a title, update or create the page with body

        >>> Page.exist('upsert') is None
        True
        >>> page = Page.upsert('upsert', '')
        >>> Page.exist('upsert') == page
        True
        """
        page = Page.exist(title)
        if page is None:
            page = Page(title=title, body=body)
        else:
            page.body = body
        page.save()
        return page

    @property
    def html(self):
        return markdown.markdown(self.body)

class Edit(models.Model):
    page = models.ForeignKey(Page)
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
