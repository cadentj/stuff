import os
import shutil
import markdown

def build_blog():
    # Ensure the blog output directory exists
    blog_output_dir = 'docs/blog'
    os.makedirs(blog_output_dir, exist_ok=True)

    # List of blog posts for the index page
    blog_posts = []

    # Process each blog post in src/blog
    for post_filename in os.listdir('src/blog'):
        with open(f'src/blog/{post_filename}', 'r') as file:
            content = file.read()

        # Convert markdown to HTML
        content = markdown.markdown(content)

        # Example: Extract title from the first line of content or filename
        title = content.split('\n', 1)[0].replace('<h1>', '').replace('</h1>', '')

        # Insert content into blog_post template
        with open('templates/blog_post.html', 'r') as file:
            post_template = file.read()
        post_html = post_template.replace('{{ title }}', title).replace('{{ content }}', content)

        # Write the post to the output directory
        post_filename = post_filename.replace('.md', '.html')
        post_output_path = os.path.join(blog_output_dir, post_filename)
        with open(post_output_path, 'w') as file:
            file.write(post_html)

        # Add the post to the list for the index
        blog_posts.append((title, post_filename))

    # Generate the blog index page
    with open('templates/blog_index.html', 'r') as file:
        index_template = file.read()
    
    blog_links = ''.join([f'<li><a href="/blog/{filename}">{title}</a></li>' for title, filename in blog_posts])
    index_html = index_template.replace('{{ blog_posts }}', f'<ul>{blog_links}</ul>')

    with open('docs/blog.html', 'w') as file:
        file.write(index_html)

# Ensure the docs directory exists
os.makedirs('docs', exist_ok=True)

with open('src/content.html', 'r') as file:
    content = file.read().strip()

# Read the base template
with open('templates/base.html', 'r') as file:
    template = file.read()

# Replace placeholders with actual content
page = template.replace('{{ content }}', content)

# Write the final HTML to the docs directory
with open('docs/index.html', 'w') as file:
    file.write(page)

# Copy static assets
source_static_dir = 'static'
destination_static_dir = 'docs/static'
if os.path.exists(destination_static_dir):
    shutil.rmtree(destination_static_dir)
shutil.copytree(source_static_dir, destination_static_dir)

build_blog()

print("Site built successfully!")