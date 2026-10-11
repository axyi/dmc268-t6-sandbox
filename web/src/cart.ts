import { formatPrice } from "./format";
import type { CartLine, Currency } from "./types";

/** Sum of all cart lines in cents. */
export function cartTotal(lines: CartLine[]): number {
  return lines.reduce((sum, line) => sum + line.priceCents * line.quantity, 0);
}

export function cartLabel(lines: CartLine[], currency: Currency): string {
  return formatPrice(cartTotal(lines), currency);
}
