/*
 * assets/js/form.js — Contact form spam filter + honeypot check.
 *
 * Silently redirects to `/` on any spam signal so bots think they succeeded
 * and stop retrying (Echo Local pattern, battle-tested across 6 sites — see
 * reference_spam_filter_patterns.md). Netlify's own honeypot + Akismet also
 * catch spam server-side; this is the client-side pre-filter that keeps the
 * intake inbox and spam signals quiet.
 *
 * Adapted for the legal vertical: keeps the crypto/SEO/pharma/419 core, adds
 * legal-adjacent solicitation patterns (guest posts to lawyers, "law firm SEO"
 * pitches, debt-recovery scams). Any match = silent redirect.
 */
(function () {
  'use strict';

  var form = document.querySelector('#contact-form');
  if (!form) return;

  // 8 spam regex checks (≥6 required by plan verify contract).
  // Each check is spelled with its own .test() so the pattern is auditable
  // grep-side (Echo Local convention — see reference_spam_filter_patterns.md).
  function isSpam(text) {
    if (!text) return false;
    // 1. Crypto/finance pitches.
    if (/\b(bitcoin|crypto|nft|forex|binance|coinbase)\b/i.test(text)) return true;
    // 2. SEO / agency solicitation (adapted for legal vertical).
    if (/\b(seo services?|guest post|link building|backlinks?|domain authority|law firm seo)\b/i.test(text)) return true;
    // 3. 3+ URLs in a single message body.
    if (/(https?:\/\/[^\s]+.*){3,}/i.test(text)) return true;
    // 4. 11+ repeated same character (aaaaaaaaaaa gibberish).
    if (/(.)\1{10,}/.test(text)) return true;
    // 5. Non-Latin script bursts (Cyrillic/Arabic/CJK 5+ chars — common bot signature).
    if (/[\p{Script=Cyrillic}\p{Script=Arabic}\p{Script=Han}]{5,}/u.test(text)) return true;
    // 6. Classic pharma / adult.
    if (/\b(viagra|cialis|casino|xanax|tramadol|escort)\b/i.test(text)) return true;
    // 7. Content-farm outreach ("write for us" / "sponsored post").
    if (/\b(write for us|sponsored (post|content)|paid guest|content collaboration)\b/i.test(text)) return true;
    // 8. 419 / advance-fee / fake debt-recovery.
    if (/\b(loan approval|nigerian prince|inheritance fund|wire transfer|debt recovery agent)\b/i.test(text)) return true;
    return false;
  }

  form.addEventListener('submit', function (event) {
    // Honeypot: if filled, silently redirect. Netlify also catches it server-side.
    var bot = form.querySelector('input[name="bot-field"]');
    if (bot && bot.value.trim() !== '') {
      event.preventDefault();
      window.location.href = '/';
      return;
    }

    // Message + name body regex sweep.
    var message = form.querySelector('textarea[name="message"]');
    var name = form.querySelector('input[name="name"]');
    var suspicious =
      (message && isSpam(message.value)) ||
      (name && isSpam(name.value));

    if (suspicious) {
      event.preventDefault();
      window.location.href = '/';
      return;
    }

    // Otherwise allow the normal Netlify form submission to proceed.
  });
}());
