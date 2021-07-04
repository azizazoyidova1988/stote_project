from django.db import connection
from contextlib import closing


def get_projects():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from project  """)
        projects = dict_fetchall(cursor)
        return projects


def get_product_by_created_at():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id order by created_at desc""")
        pro_new = dict_fetchall(cursor)
        return pro_new


def get_products_by_id(project_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select  *  from project   where project.id=%s """, [project_id])
        project = dict_fetchone(cursor)
        return project


def get_latest_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*,category.name as cat_name,
        country.name as country_name from product left join category on product.category_id=category.id 
        left join country on product.country_id = country.id 
        where product.price < 1200 order by product.price Desc""")
        lat_products = dict_fetchall(cursor)
        return lat_products



def get_services():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from services """)
        services = dict_fetchall(cursor)
        return services


def get_teams():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from team """)
        teams = dict_fetchall(cursor)
        return teams


def get_team_by_id(team_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from team where team.id=%s""", [team_id])
        team = dict_fetchone(cursor)
        return team


def get_news():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from news """)
        news = dict_fetchall(cursor)
        return news


def get_news_by_id(news_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from news where news.id=%s """, [news_id])
        new = dict_fetchone(cursor)
        return new


def get_posts():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select *  from news """)
        posts = dict_fetchall(cursor)
        return posts


def get_testimonials():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from testimonial """)
        testimonials = dict_fetchall(cursor)
        return testimonials


def get_commenter():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from commenter """)
        commenter = dict_fetchall(cursor)
        return commenter


def get_commenter_by_limit():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from commenter order by created_at desc limit 3""" )
        comment = dict_fetchall(cursor)
        return comment

def get_team_by_limit():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  * from team order by created_at desc limit 1""" )
        team = dict_fetchall(cursor)
        return team


def get_mini_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mini_category.*, category.name as c_name from mini_category
            inner join category on mini_category.category_id = category.id """)
        mini_categories = dict_fetchall(cursor)
        return mini_categories


def get_product_details(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select products.*, brands.name as b_name from products
            inner join brands on products.brands_id = brands.id
            where products.id =  %s""", [product_id])
        mini_categories = dict_fetchone(cursor)
        return mini_categories

def get_images():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from image""")
        images = dict_fetchall(cursor)
        return images

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
