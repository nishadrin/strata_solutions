from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection


PERMITTED_SORTED_IN = ("name", "created_at", )

class PostListView(APIView):
    def get(self, request):
        sort_by = request.query_params.get('sort_by')
        author_id = request.query_params.get('author_id')

        if author_id:
            try:
                author_id = int(author_id)
            except ValueError:
                author_id = None
        if sort_by and not isinstance(sort_by, str):
            sort_by = None

        if sort_by and not sort_by.lower() in PERMITTED_SORTED_IN:
            sort_by = None

        with connection.cursor() as cursor:
            query = """
                SELECT p.id, p.name, p.short_description, u.id AS author_id, u.username, u.email,
                       p.img, p.created_at,
                       (SELECT MAX(c.created_at) FROM comments_comment c WHERE c.post_id = p.id) AS last_comment_date,
                       (SELECT c.name FROM comments_comment c WHERE c.post_id = p.id ORDER BY c.created_at DESC LIMIT 1) AS last_comment_author
                FROM posts_post p
                JOIN users_user u ON p.author_id = u.id
            """
            if author_id:
                query += f" WHERE p.author_id = {author_id}"
            if sort_by:
                query += f" ORDER BY {sort_by} DESC"
            cursor.execute(query)
            rows = cursor.fetchall()

            posts = [
                {
                    'id': row[0],
                    'name': row[1],
                    'short_description': row[2],
                    'author': {
                        'id': row[3],
                        'username': row[4],
                        'email': row[5],
                    },
                    'img': row[6],
                    'created_at': row[7],
                    'last_comment_date': row[8],
                    'last_comment_author': row[9],
                }
                for row in rows
            ]

        return Response(posts)


class PostDetailView(APIView):
    def get(self, request, pk):
        with connection.cursor() as cursor:
            post_query = """
                SELECT p.name, p.content, u.id AS author_id, u.username, u.email, p.img
                FROM posts_post p
                JOIN users_user u ON p.author_id = u.id
                WHERE p.id = %s
            """
            cursor.execute(post_query, [pk])
            post_row = cursor.fetchone()

            if not post_row:
                return Response(status=status.HTTP_404_NOT_FOUND)

            comments_query = """
                SELECT c.name, c.content, c.created_at
                FROM comments_comment c
                WHERE c.post_id = %s
                ORDER BY c.created_at DESC
            """
            cursor.execute(comments_query, [pk])
            comments_rows = cursor.fetchall()

            post = {
                'name': post_row[0],
                'content': post_row[1],
                'author': {
                    'id': post_row[2],
                    'username': post_row[3],
                    'email': post_row[4],
                },
                'img': post_row[5],
                'comments': [
                    {
                        'name': row[0],
                        'content': row[1],
                        'created_at': row[2]
                    }
                    for row in comments_rows
                ]
            }

        return Response(post)
