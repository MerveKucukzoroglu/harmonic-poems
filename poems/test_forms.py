"""Unit Testing for Forms"""
from django.test import TestCase
from .forms import PoemForm, CommentForm


class TestPoemForm(TestCase):
    """Unit Test for Poems Form"""
    def test_post_title_is_required(self):
        form = PoemForm(({'title': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_post_content_is_required(self):
        form = PoemForm(({'content': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = PoemForm()
        self.assertEqual(
            form.Meta.fields, ('title', 'content', 'excerpt', 'featured_image')
            )


class TestCommentForm(TestCase):
    """Unit Test for Comments Form"""
    def test_post_title_is_required(self):
        form = CommentForm(({'body': ''}))
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))
