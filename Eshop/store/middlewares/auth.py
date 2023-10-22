from django.shortcuts import redirect
def auth_middleware(get_response):
    # One-time configuration and initialization.
    def middleware(request):
        #print('middleware',dir(request))
        #print(request.__dict__)
        #print(request.META['PATH_INFO'])
        returnUrl =request.META['PATH_INFO']
        if not request.session.get('customer_id'):
            return redirect(f'login?returnUrl={returnUrl}')

        response = get_response(request)
        return response

    return middleware