Required modules for elasticsearch integration with djangorestframework

1. elasticsearch : official low-level Python client for Elasticsearch
2. elasticsearch-dsl-py - high-level library for writing and running queries against Elasticsearch
3. django-elasticsearch-dsl - wrapper around elasticsearch-dsl-py that allows indexing Django models in Elasticsearch


Notes:

1. In order to transform the article type, we added the type attribute to the ArticleDocument.
2. Because our Article model is in a many-to-many (M:N) relationship with Category and a many-to-one (N:1) relationship with User we needed to take care of the relationships. We did that by adding ObjectField attributes.

