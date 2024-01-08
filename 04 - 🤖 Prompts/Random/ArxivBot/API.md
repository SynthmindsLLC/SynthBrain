openapi: "3.0.0"
info:
  version: 1.0.0
  title: arXiv Article Search
servers:
  - url: https://export.arxiv.org/api
paths:
  /query:
    get:
      summary: Search for articles on arXiv
      operationId: searchArxiv
      tags:
        - articles
      parameters:
        - name: search_query
          in: query
          description: The query string to search for articles.
          required: true
          schema:
            type: string
      responses:
        '200':
          description: An Atom feed of arXiv search results.
          content:
            application/atom+xml: {}
        default:
          description: unexpected error
components:
  schemas: {}