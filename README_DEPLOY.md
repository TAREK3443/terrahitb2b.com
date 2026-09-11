# TerraHit B2B — corrected website

This package is ready for a GitHub Pages repository using `terrahitb2b.com` as its custom domain.

## Build

Run:

```bash
python3 build.py
```

The command generates the English pages at the repository root and localized French and Arabic pages under `fr/` and `ar/`.

## Before publishing

1. Confirm that the Basin form endpoint `3b9ec06003b5` belongs to TerraHit and that its notification settings are still correct. The site redirects successful submissions to its own localized confirmation page. For a no-JavaScript fallback, paid Basin accounts can also set `https://terrahitb2b.com/thank-you.html` under Form → Settings → General → Custom Redirect.
2. Confirm the stated 12-month retention period for unsuccessful enquiries and the actual data-transfer safeguards used by the form provider.
3. Replace the existing GitHub Pages files with this package, while preserving repository settings and DNS records.
4. After deployment, submit `https://terrahitb2b.com/sitemap.xml` in Google Search Console and test the form once with a non-sensitive test message.

## Main changes

- Responsive hamburger navigation.
- Separate EN/FR/AR URLs with canonical and `hreflang` tags.
- Specific Algeria–Europe trade-coordination positioning.
- Clear boundary between coordination and regulated activities.
- Accessible form labels, keyboard focus states and skip link.
- TerraHit-branded confirmation pages after successful form submission.
- Home-page titles limited to two lines on desktop layouts.
- Browser-language detection on first display, with the visitor's manual language choice remembered.
- Meta descriptions, Open Graph tags and organization structured data.
- Updated legal and privacy pages identifying GitHub Pages, Cloudflare and Basin.
- No third-party web fonts or analytics scripts.
