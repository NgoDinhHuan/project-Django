from django.contrib import admin
from .models import Setting, Slide, Category, Post,Imageslide,Email,Order,Order_detail,OrderSummary
from django.db.models import Count, Sum, Min, Max, DateTimeField
from django.db.models.functions import Trunc
import pandas as pd
class SettingAdmin(admin.ModelAdmin):
    pass


class SlideAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass
class PosttestAdmin(admin.ModelAdmin):
    pass
class ImagelistAdmin(admin.StackedInline):
    model = Imageslide

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}  # Gợi ý trường slug theo category_name
    inlines = [ImagelistAdmin]

class EmailAdmin(admin.ModelAdmin):
    model = Email
    pass


class Order_detailAdmin(admin.TabularInline):
    model = Order_detail

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id","payment_code", "full_name", "email","number_phone","fulfilled","order_status")
    list_filter = ('order_status', 'fulfilled',)
    inlines = [
        Order_detailAdmin,
    ]
admin.site.register(Category, CategoryAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Setting, SettingAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Order, OrderAdmin)
#admin.site.register(Order_detail, Order_detailAdmin)

# Register your models here.
def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'week'
    return 'month'

@admin.register(OrderSummary)
class OrderSummaryAdmin(admin.ModelAdmin):
    #list_filter = ('id_order.order_status', 'id_order.fulfilled',)
    change_list_template = 'order_summary_change_list.html'
    date_hierarchy = 'create_date'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset.all().filter(id_order__order_status='OK')

        except (AttributeError, KeyError):
            return response

        metrics = {
   #         'cate_name':Max('id_category.category_name'),
            'num': Count('id_category'),
            'total_sales': Sum('qty'),
            'total_shipping_cost': Sum('ship_cost'),#Sum('shipping_cost'),
            'total_no_shipping_cost':Sum('amount'), #Sum(F('total') - F('shipping_cost')),
            'percent_of_total':Sum('amount'),# Sum(F('total') - F('shipping_cost') / F('total')),
        }

        response.context_data['summary'] = list(
            qs
                .values('id_category')
                .annotate(**metrics)
                .order_by('-create_date')
        )
        df = pd.DataFrame(response.context_data['summary'])


        for data in df.itertuples():
           # df.set_value(index, 'Slub', '22')
            df.loc[data.Index,'Name'] = Category.objects.all().filter(id=int(data.id_category)).values('category_name')[0].get("category_name")
            df.loc[data.Index,'slug'] = Category.objects.all().filter(id=int(data.id_category)).values('slug')[0].get("slug")
           # print(data.Index)
           # df['Slub_name'].iloc[data.index] = 'x'
                # Category.objects.all().filter(id=int(data.id_category)).values('category_name')[0].get("category_name")

      #  print(response.context_data['summary'])

        response.context_data['summary']= df.itertuples()
        print(response.context_data['summary'])
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        period = get_next_in_date_hierarchy(request, self.date_hierarchy)
        response.context_data['period'] = period
        summary_over_time = qs.annotate(
            period=Trunc('create_date', 'day', output_field=DateTimeField()),
        ).values('period').annotate(total=Sum('amount')).order_by('period')
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
               ((x['total'] or 0) - low) / (high - low) * 100
               if high > low else 0,
        } for x in summary_over_time]

        return response