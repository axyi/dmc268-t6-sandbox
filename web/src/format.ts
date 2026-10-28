import type { Currency } from "./types";

/** Format an amount in cents as a price string, currency first. */
export function formatPrice(currency: Currency, cents: number): string {
  return `${currency} ${(cents / 100).toFixed(2)}`;
}
