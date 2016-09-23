# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-23 16:55
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0048_auto_20160923_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField((('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('twocolumn', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('white', 'White'), ('grey', 'Grey'), ('blue', 'Blue')], default='white')), ('left_column_size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('12', '12/12'), ('11', '11/12'), ('10', '10/12'), ('9', '9/12'), ('8', '8/12'), ('7', '7/12'), ('6', '6/12'), ('5', '5/12'), ('4', '4/12'), ('3', '3/12'), ('2', '2/12'), ('1', '1/12'), ('0', '0/12')], default='6')), ('right_column_size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('12', '12/12'), ('11', '11/12'), ('10', '10/12'), ('9', '9/12'), ('8', '8/12'), ('7', '7/12'), ('6', '6/12'), ('5', '5/12'), ('4', '4/12'), ('3', '3/12'), ('2', '2/12'), ('1', '1/12'), ('0', '0/12')], default='6')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='common/blocks/image.html')), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),)))), classname='col4', icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='common/blocks/image.html')), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),)))), classname='col4', icon='arrow-right', label='Right column content'))))), ('threecolumn', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('white', 'White'), ('grey', 'Grey'), ('blue', 'Blue')], default='white')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='common/blocks/image.html')), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),))), ('photo_stream', wagtail.wagtailcore.blocks.StructBlock(()))), classname='col4', icon='arrow-left', label='Left column content')), ('center_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='common/blocks/image.html')), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),))), ('photo_stream', wagtail.wagtailcore.blocks.StructBlock(()))), classname='col4', icon='arrow-right', label='Center column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),))), ('photo_stream', wagtail.wagtailcore.blocks.StructBlock(()))), classname='col4', icon='arrow-right', label='Right column content'))))), ('tab_index', wagtail.wagtailcore.blocks.StructBlock((('tabsIndexes', wagtail.wagtailcore.blocks.StreamBlock((('tab_id', wagtail.wagtailcore.blocks.TextBlock(max_length=25)),))),))), ('tabcontainerblock', wagtail.wagtailcore.blocks.StructBlock((('tabs', wagtail.wagtailcore.blocks.StreamBlock((('tab', wagtail.wagtailcore.blocks.StructBlock((('id', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('isActive', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False)), ('container', wagtail.wagtailcore.blocks.StreamBlock((('two_column_block', wagtail.wagtailcore.blocks.StructBlock((('background', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('white', 'White'), ('grey', 'Grey'), ('blue', 'Blue')], default='white')), ('left_column_size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('12', '12/12'), ('11', '11/12'), ('10', '10/12'), ('9', '9/12'), ('8', '8/12'), ('7', '7/12'), ('6', '6/12'), ('5', '5/12'), ('4', '4/12'), ('3', '3/12'), ('2', '2/12'), ('1', '1/12'), ('0', '0/12')], default='6')), ('right_column_size', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('12', '12/12'), ('11', '11/12'), ('10', '10/12'), ('9', '9/12'), ('8', '8/12'), ('7', '7/12'), ('6', '6/12'), ('5', '5/12'), ('4', '4/12'), ('3', '3/12'), ('2', '2/12'), ('1', '1/12'), ('0', '0/12')], default='6')), ('left_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='common/blocks/image.html')), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),)))), classname='col4', icon='arrow-left', label='Left column content')), ('right_column', wagtail.wagtailcore.blocks.StreamBlock((('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock(template='common/blocks/image.html')), ('appeal', wagtail.wagtailcore.blocks.StructBlock((('icon', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('none', 'none'), ('flask', 'flask'), ('group', 'group'), ('laptop', 'laptop'), ('sitemap', 'sitemap'), ('user', 'user'), ('book', 'book'), ('download', 'download')])), ('topic', wagtail.wagtailcore.blocks.CharBlock(max_length=30, required=True)), ('content', wagtail.wagtailcore.blocks.TextBlock(max_length=255, required=True))), classname='appeal', icon='tick', template='common/blocks/appeal.html')), ('embedded_video', wagtail.wagtailembeds.blocks.EmbedBlock()), ('google_map', wagtail.wagtailcore.blocks.StructBlock((('address', wagtail.wagtailcore.blocks.CharBlock(max_length=255, required=True)), ('map_zoom_level', wagtail.wagtailcore.blocks.CharBlock(default=14, max_length=3, required=True))))), ('twitter_feed', wagtail.wagtailcore.blocks.StructBlock((('username', wagtail.wagtailcore.blocks.CharBlock(required=True)),)))), classname='col4', icon='arrow-right', label='Right column content'))))), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()))))))),))),))), ('customedimage', wagtail.wagtailcore.blocks.StructBlock((('main_image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('style', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('(max-width:225px;max-height:145px)', 'small display'), ('(height:Auto)', 'auto display')], default='(height:Auto)'))))), ('raw_html', wagtail.wagtailcore.blocks.RawHTMLBlock(help_text='With great power comes great responsibility. This HTML is unescaped. Be careful!'))), blank=True, null=True),
        ),
    ]
