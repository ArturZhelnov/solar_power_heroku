from django.contrib import admin
#from .models import Contact, Social_link, Service, Service_img
from .models import *

import csv
import datetime
from django.http import HttpResponse
from datetime import *

#import reportlab
#from reportlab.platypus import SimpleDocTemplate
#from reportlab.platypus import Paragraph, Table, TableStyle, SimpleDocTemplate
#from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
#from reportlab.lib.units import inch, cm, mm
from reportlab.platypus import *
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

# for contacts
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many\
    and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


# try
def export_audits_as_pdf(self, request, queryset):

    file_name = "audit_entries{0}.pdf"#.format(time.strftime("%d-%m-%Y-%H-%M-%S"))
    #file_name = "audit_entries{0}.pdf".format(time.strftime("%d-%m-%Y-%H-%M-%S"))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)

    data = [['Name', 'Phone', 'Time']]
    # data = [['id', 'Name', 'Phone', 'Time']]
    #data = [['Action Time', 'Priority', 'username', 'Source Address', 'Subject', 'Details']]
    for d in queryset.all():
        datetime_str = str(d.created).split('.')[0]
        item = [d.name, d.phone, datetime_str]
        # item = [datetime_str, d.name, d.phone, d.id, d.created]
        data.append(item)

    doc = SimpleDocTemplate(response, pagesize=A4)
    #doc = SimpleDocTemplate(response, pagesize=(21*inch, 29*inch))
    elements = []

    table_data = Table(data)
    table_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                    ('BOX', (0, 0), (-1, -1), 1.25, colors.black),
                                    ("FONTSIZE",  (0, 0), (-1, -1), 13),
                                    ('BACKGROUND', (0, 0), (-1, 0), colors.Color(0, 0.7, 0.7)),
                                    ('TEXTCOLOR', (0, 1), (0, -1), colors.blue),
                                    ('TEXTCOLOR', (1, 1), (-2, -1), colors.red),
                                    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                                    ('BACKGROUND', (0, 1), (0, -1), colors.pink),
                                    ('BACKGROUND', (1, 1), (-2, -1), colors.lavender),
                                    ('BACKGROUND', (3, 1), (-2, -1), colors.orange),
                                    #('TEXTCOLOR', (0,-1), (-1,-1), colors.green),
                                    ]))
    
    # can do: table_data.add('BACKGROUND', (0,0), (-1,0), colors.Color(0,0.7,0.7))
    
    elements.append(table_data)
    doc.build(elements)

    return response
export_audits_as_pdf.short_description = 'Export to PDF'

# try
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    #list_display = ['name', 'phone', 'is_contacted']
    list_filter = ['name', 'phone']
    search_fields = ['name', 'phone']
    list_filter = ['created', ]
    list_per_page = 10
    ordering = ('-created',)
    actions = [export_to_csv, export_audits_as_pdf]
    #list_editable = ['is_contacted',]


admin.site.register(Contact, ContactAdmin)



admin.site.register(Social_link)

admin.site.register(Service)
admin.site.register(Service_img)

admin.site.register(Step)
admin.site.register(Steps_img)

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active']
    list_editable = ['is_active',]
    
    
admin.site.register(Partner, PartnerAdmin)

admin.site.register(Footer_contact)
admin.site.register(Blockquote)

class Client_itemInline(admin.TabularInline):
    model = Client_item
    # can_delete = False
    extra = 1
    

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('heading', 'created',)
    inlines = [Client_itemInline,]
    

admin.site.register(Info_tab)
#admin.site.register(Tab_context)
admin.site.register(Info_tab_context)
# for contacts

#class Social_linkInline(admin.TabularInline):
    #model = Social_link
    #extra = 1
    
#admin.site.register(Social_link, Social_linkInline)
    
#@admin.register(Social_link)
#class Social_linkAdmin(admin.ModelAdmin):
#     inlines = [
#        Social_linkInline,
#    ]

'''
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish', 'status', 'views', 'slug', 'author')
    list_filter = ('status', 'created', 'publish', 'author')
    # list_editable = ['price', 'available']
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', '-publish')
    # list_per_page = 3
'''