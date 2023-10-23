from django.utils.deprecation import MiddlewareMixin

class ForceJsonResponseMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Verifica si la URL comienza con "/api/"
        if request.path.startswith('/api/'):
            # Configura el encabezado "Accept" para JSON
            request.META['HTTP_ACCEPT'] = 'application/json'