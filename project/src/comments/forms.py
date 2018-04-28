from django.views.generic import CreateView


class MyCreateView(CreateView):
    def get_form_kwargs(self):
        # pass "user" keyword argument with the current user to your form
        kwargs = super(MyCreateView, self).get_form_kwargs()
        kwargs['question_id'] = self.request.GET.get('q_id')
        if self.request.GET.get('com_id') is not None:
            kwargs['comment_id'] = self.request.GET.get('com_id')
        else:
            kwargs['comment_id'] = None
        return kwargs