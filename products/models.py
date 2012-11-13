from django.db import models

class Product(models.Model):
	title = models.CharField(max_length=30)
	subtitle = models.CharField(max_length=30, blank=True)
	content = models.TextField()
	price = models.IntegerField(help_text='This field <strong>shold be</strong> entered for buyers to have info of the <strong>cost</strong> ot the product!')
	image = models.ImageField(upload_to='uploads/', blank=True)

	IN_STOCK = 'IS'
	COMING_SOON = 'CS'
	DEPLETED = 'D'
	DO_WE_HAVE_IT_NOW = (
		(IN_STOCK, 'In stock'),
		(COMING_SOON, 'Coming soon'),
		(DEPLETED, 'Depleted'),
	)
	do_we_have_it = models.CharField(max_length=30, choices=DO_WE_HAVE_IT_NOW, default=IN_STOCK)

	category = models.ForeignKey('category.Category', null=True, default='asdasd')

	def __unicode__(self):
		return self.title + ' ' +  self.do_we_have_it