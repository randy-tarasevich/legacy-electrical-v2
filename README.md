# Legacy Electrical CT Website

A professional 4-page website for Legacy Electrical CT, an electrical contracting business in Berlin, CT. Built with Astro.js and Tailwind CSS.

## Pages

- **Home** - Hero section, services overview, why choose us, and CTA
- **About** - Company story, owner bio (Tayler Nadolny-Sipes), values, and service area
- **Services** - Residential, commercial, and specialty electrical services
- **Contact** - Contact form (Web3Forms), contact info, and emergency services

## Tech Stack

- [Astro](https://astro.build/) v5.x
- [Tailwind CSS](https://tailwindcss.com/) v4.x
- [Web3Forms](https://web3forms.com/) for contact form

## Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Configure Web3Forms:**
   - Get your access key from [Web3Forms](https://web3forms.com/)
   - Open `src/pages/contact.astro`
   - Replace `YOUR_WEB3FORMS_ACCESS_KEY` with your actual key:
     ```html
     <input type="hidden" name="access_key" value="your-actual-key-here">
     ```

3. **Update contact information:**
   - Phone number: Search for `(860) 555-1234` and replace with actual number
   - Email: Search for `info@legacyelectricalct.com` and replace if different

4. **Run development server:**
   ```bash
   npm run dev
   ```

5. **Build for production:**
   ```bash
   npm run build
   ```

## Project Structure

```
legacy-electrical/
├── public/
│   └── favicon.svg
├── src/
│   ├── components/
│   │   ├── Navigation.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   └── Layout.astro
│   ├── pages/
│   │   ├── index.astro      (Home)
│   │   ├── about.astro
│   │   ├── services.astro
│   │   └── contact.astro
│   └── styles/
│       └── global.css
├── astro.config.mjs
├── package.json
├── tsconfig.json
└── README.md
```

## Customization

### Colors
Edit the CSS variables in `src/styles/global.css`:
- `--color-electric`: Primary blue (#00d4ff)
- `--color-volt`: Accent yellow (#f5dd00)
- `--color-carbon`: Dark background (#1a1a1a)
- `--color-steel`: Secondary background (#2d2d2d)

### Fonts
The site uses:
- **Oswald** for headings (industrial, bold)
- **Source Sans 3** for body text (clean, readable)

### Adding Owner Photo
In `src/pages/about.astro`, replace the placeholder div with an actual image:
```astro
<img 
  src="/path-to-photo.jpg" 
  alt="Tayler Nadolny-Sipes" 
  class="w-full h-full object-cover"
/>
```

## Deployment

The site can be deployed to any static hosting:
- Netlify
- Vercel
- Cloudflare Pages
- GitHub Pages
- DigitalOcean App Platform

Build command: `npm run build`
Output directory: `dist`

## License

Built for Legacy Electrical CT by Shoreline Web Solutions.
