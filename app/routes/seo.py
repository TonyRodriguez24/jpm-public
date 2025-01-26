#sitemap, robots.txt, and 404 routes
from flask import Blueprint, Response, url_for, current_app
import datetime

seo = Blueprint('seo', __name__)

@seo.route('/sitemap.xml', methods=['GET'])
def sitemap():
    """Builds sitemap xml, excludes routes that aren't available without password or ones that shouldn't be on there"""
   

    # Correct endpoint names for excluded routes
    excluded_routes = ['admin', 'dashboard', 'set_password', 'add_contact', 'add_project' 'logout', 'robots_txt', 'sitemap']
    sitemap_xml = ['<?xml version="1.0" encoding="utf-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    try:
        # Generate sitemap entries
        for rule in current_app.url_map.iter_rules():
            # Only include GET methods and routes without arguments
            if rule.methods and "GET" in rule.methods and not rule.arguments:
                if rule.endpoint not in excluded_routes:
                    try:
                        url = url_for(rule.endpoint, _external=True)
                        last_modified = datetime.datetime.now().date()
                        sitemap_xml.append(
                            f'<url><loc>{url}</loc><lastmod>{last_modified}</lastmod></url>'
                        )
                    except Exception as e:
                        print(f"Error adding URL for rule {rule}: {e}")

        sitemap_xml.append('</urlset>')
        sitemap_content = '\n'.join(sitemap_xml)

        # Return the generated sitemap
        return Response(sitemap_content, mimetype='application/xml')

    except Exception as e:
        return Response("Error generating sitemap", status=500, mimetype='text/plain')

@seo.route('/robots.txt')
def robots_txt():
    """Robots.txt file"""

    response = """User-agent: *
                Disallow: /admin
                Disallow: /admin/dashboard
                Disallow: /admin/set-password
                Disallow: /admin/add-contact
                Disallow: /admin/edit-contact/*
                Disallow: /admin/add-project
                Disallow: /admin/edit-project/*
                Disallow: /admin/logout
                Allow: /

                Sitemap: https://jpmandsons.com/sitemap.xml
            """
    return Response(response, mimetype='text/plain')