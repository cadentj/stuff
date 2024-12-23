import os
import shutil
import markdown

##### CONSTANTS #####

BLOG_DIR = 'src/blog'
BLOG_OUTPUT_DIR = 'docs/blog'

with open('templates/blog_post.html', 'r') as file:
    BLOG_TEMPLATE = file.read()

with open('templates/blog_index.html', 'r') as file:
    BLOG_INDEX_TEMPLATE = file.read()

with open('templates/base.html', 'r') as file:
    BASE_TEMPLATE = file.read()

# Prepare the output directory
os.makedirs('docs', exist_ok=True)

##### BUILD BLOG #####

def extract_metadata(content):
    """Extract metadata between --- markers from markdown content"""
    lines = content.split('\n')
    metadata = {}
    
    # Find start of metadata section
    start_index = -1
    end_index = -1
    for i, line in enumerate(lines):
        if line.strip() == '---':
            if start_index == -1:
                start_index = i
            else:
                end_index = i
                break
    
    # If we found a metadata section
    if start_index != -1 and end_index != -1:
        # Parse metadata section
        for line in lines[start_index + 1:end_index]:
            if ':' in line:
                key, value = line.split(':', 1)
                metadata[key.strip()] = value.strip()
        
        # Remove metadata section from content
        content = '\n'.join(lines[:start_index] + lines[end_index + 1:])
    
    return metadata, content

def extract_title(content):
    return content.split('\n', 1)[0] \
        .replace('<h1>', '') \
        .replace('</h1>', '')

def make_post(post_filename):
    # Load
    path = os.path.join(BLOG_DIR, post_filename)
    with open(path, 'r') as file:
        content = file.read()
    
    # Extract metadata
    metadata, content = extract_metadata(content)
    
    # Convert markdown to HTML
    content = markdown.markdown(content)
    title = extract_title(content)

    # Convert
    post_html = BLOG_TEMPLATE \
        .replace('{{ title }}', title) \
        .replace('{{ content }}', content)

    # Write
    post_filename = post_filename.replace('.md', '.html')
    post_output_path = os.path.join(BLOG_OUTPUT_DIR, post_filename)
    with open(post_output_path, 'w') as file:
        file.write(post_html)

    return title, post_filename, metadata

def build_blog():
    os.makedirs(BLOG_OUTPUT_DIR, exist_ok=True)

    # Build individual posts
    blog_posts = []
    for post_filename in os.listdir(BLOG_DIR):
        blog_posts.append(make_post(
            post_filename,
        ))
    
    # Filter out posts where Visible is False
    visible_posts = [
        (title, filename) 
        for title, filename, metadata in blog_posts 
        if metadata.get('Visible', 'True').lower() != 'false'
    ]
    
    # Build index with links to posts
    blog_links = ''.join([
        f'<li><a href="/blog/{filename}">{title}</a></li>' 
        for title, filename in visible_posts
    ])
    index_html = BLOG_INDEX_TEMPLATE.replace('{{ blog_posts }}', f'<ul class="blog-posts">{blog_links}</ul>')

    # Write
    with open('docs/blog.html', 'w') as file:
        file.write(index_html)

##### BUILD SITE #####
 
def build_main():

    with open('src/content.html', 'r') as file:
        content = file.read().strip()

    page = BASE_TEMPLATE.replace('{{ content }}', content)

    with open('docs/index.html', 'w') as file:
        file.write(page)

def move(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

##### MAIN #####

def main():

    build_blog()

    build_main()

    move(
        'static',
        'docs/static',
    )

    print("Site built successfully!")

if __name__ == '__main__':
    main()