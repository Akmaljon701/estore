from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="DRF APIs",
        default_version='v1',
        description="API documentation by Akmaljon",
        contact=openapi.Contact(email="akmaljonyoqubov088@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
