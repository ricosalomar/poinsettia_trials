from django.db import models
from django.template.defaultfilters import slugify

class Region(models.Model):
    region = models.CharField(max_length=128)
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.region

    class Meta:
        ordering = ['region']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.region)

        super(Region, self).save(*args, **kwargs)

class Breeder(models.Model):
    breeder = models.CharField(max_length=128)
    slug = models.SlugField(editable=False)

    def __unicode__(self):
        return self.breeder

    class Meta:
        ordering = ['breeder']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.breeder)

        super(Breeder, self).save(*args, **kwargs)


class Variety(models.Model):
    VIGOR_CHOICES = (
        (1, 'low'),
        (2, 'medium'),
        (3, 'high'),
    )

    COLOR_CHOICES = (
        (1, 'red'),
        (2, 'novelty red'),
        (3, 'white'),
        (4, 'pink'),
        (5, 'marble'),
        (6, 'jingle'),
        (7, 'peppermint'),
        (8, 'other novelties'),
    )

    TIMING_CHOICES = (
        (1, 'early season'),
        (2, 'mid season'),
        (3, 'late season'),
    )


    region = models.ForeignKey(Region)
    variety = models.CharField(max_length=128)
    slug = models.SlugField(editable=False)
    color = models.IntegerField(choices=COLOR_CHOICES, default=0)
    vigor = models.IntegerField(choices=VIGOR_CHOICES, default=0)
    timing = models.IntegerField(choices=TIMING_CHOICES, default=0)
    breeder = models.ForeignKey(Breeder)
    summary = models.TextField()

    def __unicode__(self):
        return "%s-%s" % (self.region, self.variety)

    class Meta:
        verbose_name_plural = 'Varieties'
        ordering = ['variety']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.variety)

        super(Variety, self).save(*args, **kwargs)


class Trial(models.Model):
    import datetime
    YEAR_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append((r,r))
    variety = models.ForeignKey(Variety)
    year = models.IntegerField(max_length=4, choices=YEAR_CHOICES)
    bracht_color = models.DateField()
    antithesis = models.DateField()
    height = models.CharField(max_length=32)
    bracht_diameter = models.CharField(max_length=32)

    def __unicode__(self):
        return "%s-%s" % (self.variety, self.year)

    class Meta:
        ordering = ['variety','year']


class Image(models.Model):
    trial = models.ForeignKey(Trial)
    url = models.URLField()
    alt_text = models.CharField(max_length=128)


