import type { Currency } from "./types";

/** Format an amount in cents as a price string. */
export function formatPrice(cents: number, currency: Currency): string {
  return `${(cents / 100).toFixed(2)} ${currency}`;
}
