/**
 * ─────────────────────────────────────────────────────────────────────────────
 * CLIENT DATA
 * ─────────────────────────────────────────────────────────────────────────────
 * Business-specific copy: name, phone, email, address, socials.
 * Imported by Header, Footer, Contact page, and Head/SEO components.
 *
 * No component should hardcode a business name or phone number —
 * everything comes from this file or brand.ts.
 * ─────────────────────────────────────────────────────────────────────────────
 */

export const client = {
  name: 'Legacy Electrical',
  email: 'tayler@legacyelectricalct.com',
  phoneForTel: '860-604-9325',
  phoneFormatted: '860-604-9325',
  /** Business / contractor license number. Displayed in the header and footer
   *  as a trust signal. Set to an empty string to hide it. */
  license: 'License: ELC.0207936-E1 (CT)',
  address: {
    lineOne: '',
    lineTwo: '',
    city: 'East Berlin',
    state: 'CT',
    zip: '06023',
    country: 'US',
    mapLink: 'https://maps.app.goo.gl/example',
  },
  socials: {
    facebook: 'https://www.facebook.com/',
    instagram: 'https://www.instagram.com/',
    google: 'https://www.google.com/maps',
  },
  domain: 'https://www.legacyelectrical.com',
} as const;

export type Client = typeof client;
