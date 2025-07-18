# CLAUDE.md

## Project Overview
This is a personal website/blog built with Python and static site generation. The site focuses on minimalist design with clean typography and subtle interactions.

## Design Preferences
- **Simple and clean**: Keep things minimal, avoid unnecessary complexity
- **Typography-focused**: Uses Inter font family, clean text hierarchy
- **Subtle animations**: Prefer gentle hover effects (like 8px translateX shifts with 0.2s ease transitions)
- **Dark mode support**: All styles should work in both light and dark themes
- **Color scheme**: 
  - Light: #FFFCF0 background, #100F0F text
  - Dark: #100F0F background, #CECDC3 text
  - Accent: #205EA6 (light), #4385BE (dark)

## Code Style
- Favor editing existing files over creating new ones
- Follow existing patterns and conventions
- Use absolute paths for file operations
- Keep CSS simple and readable
- Use semantic HTML structure

## Site Structure
- Blog posts in `src/blog/` as markdown files
- Static assets in `static/` directory
- Templates in `templates/` directory
- Build process uses `build.py`

## Content Style
- Concise, thoughtful writing
- Curated content over quantity
- Personal touches and authentic voice
- Quote-style formatting for meaningful content