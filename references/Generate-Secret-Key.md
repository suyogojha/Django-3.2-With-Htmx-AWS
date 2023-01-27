# Generate a one-off secret key in Django


The code:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```