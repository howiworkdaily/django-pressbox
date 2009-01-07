from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from pressbox.managers import PressItemManager

class ModelBase(models.Model):
    """
    Abstract base class for all model instances in django-pressbox.
    
    """
    created_on = models.DateTimeField(_('created on'), default=datetime.now, 
        editable=False, )
    updated_on = models.DateTimeField(_('updated on'), editable=False)

    class Meta:
        abstract = True

    def save(self):
        self.updated_on = datetime.now()    
        super(ModelBase, self).save()

class PressCategory(models.Model):
    """
    Represents a category for organizing press items.
    
    """
    
    title = models.CharField(_('title'), max_length=100, unique=True)
    slug = models.SlugField(_('slug field'), unique=True)
    sort_order = models.PositiveIntegerField(_('sort order'), default=0)
    
    class Meta:
        verbose_name = _('press category')
        verbose_name_plural = _('press categories')
        ordering = ['sort_order', '-title']

    def __unicode__(self):
        return self.title

class PressItem(ModelBase):
    """
    Represents a press release or any unique press item.
    
    """
    
    title = models.CharField(_('title'), max_length=100)
    slug = models.SlugField(_('slug'), unique_for_date="published_on")
    category = models.ForeignKey(PressCategory, related_name="press_items")
    short_description = models.CharField(_('short descrption'), 
        max_length=500, blank=True, null=True, help_text=_("Max 500 characters."))
    body =  models.TextField(_('body'), blank=True, null=True)
    published_on = models.DateField(_('published on'), blank=False, null=True)
    download_file = models.FileField(_('downloadable file'), blank=True, 
        null=True, upload_to='uploads/pressbox')
    download_title = models.CharField(_('downloadabe file title'), max_length=255, blank=True, null=True)
    sort_order = models.PositiveIntegerField(_('sort order'), default=0)
    is_active = models.BooleanField(_('is active'), default=True)
    
    objects = PressItemManager()

    class Meta:
        verbose_name = _("press item")
        verbose_name_plural = _("press items")
        ordering = ['sort_order', '-published_on',]

    def __unicode__(self):
        return self.title
    
    @property
    def main_image(self):
        """ Returns either the first sorted image for the associated press images. """
        try:
            return images.all()[0]
        except:
            return None
        
    @permalink
    def get_absolute_url(self):
        return ('press_detail', None, {
            'slug': self.slug,
        })
        

class PressImage(models.Model):
    """
    Represents an image related to a press item.
    
    """

    press_item = models.ForeignKey(PressItem, related_name='images')
    image = models.ImageField(_('image'), upload_to='uploads/pressbox' )
    alt_text = models.CharField(_('alt text'), max_length=50, blank=True, 
        null=True)
    sort_order = models.PositiveIntegerField(_('sort order'))

    class Meta:
        verbose_name = _("press image")
        verbose_name_plural = _("press images")
        ordering = ['-sort_order', '-created_on', ]
        
    def save(self):
        self.updated_on = datetime.now()
        super(PressImage,self).save()

    def __unicode__(self):
        return self.alt_text
        
    class Meta:
        ordering = ['sort_order',]
    
    
