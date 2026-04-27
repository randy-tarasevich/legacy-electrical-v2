# Legacy Electrical v2

Production website for Legacy Electrical, built with [Astro 6](https://astro.build) and [Tailwind CSS v4](https://tailwindcss.com), ready for Cloudflare Pages.

---

## What's included

- Core pages: Home, About, Services, Contact, and contact success confirmation
- Tailwind v4 tokenized theming via `src/styles/theme.css`
- SEO basics: title/description, canonical URLs, Open Graph, JSON-LD, sitemap, robots.txt
- Responsive layout with sticky header, mobile nav drawer, and reusable sections
- Cloudflare-compatible static output (`dist`) and headers via `public/_headers`

---

## Quick start

```bash
# 1. Install dependencies
npm install

# 2. Start dev server
npm run dev
# http://localhost:4321

# 3. Build for production
npm run build

# 4. Preview production output
npm run preview
```

---

## Key configuration files

- `src/data/client.ts` - business data (name, phone, email, address, socials)
- `src/config/brand.ts` - branding (site name, tagline, colors, fonts, SEO defaults)
- `src/styles/theme.css` - Tailwind v4 design tokens
- `astro.config.mjs` - Astro site config and integrations
- `wrangler.toml` - Cloudflare Worker/asset deployment config
- `public/_headers` - security and cache headers for Cloudflare Pages

---

## Cloudflare Pages deploy settings

- Framework preset: `Astro`
- Build command: `npm run build`
- Build output directory: `dist`
- Node version: `22`

After deploying, confirm these match your production domain:

- `src/data/client.ts` -> `domain`
- `src/config/brand.ts` -> `url`
- `astro.config.mjs` -> `site`

---

## Commands reference

- `npm run dev` - start local development server
- `npm run build` - generate static site in `dist`
- `npm run preview` - serve built output locally
