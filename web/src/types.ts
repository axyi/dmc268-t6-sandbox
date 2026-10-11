/** One line of a cart. */
export interface CartLine {
  sku: string;
  quantity: number;
  priceCents: number;
}

export type Currency = "EUR" | "USD";
