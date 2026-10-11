import round2, { clamp } from "./utils.js";

export function quantity(input) {
  return clamp(Number(input), 1, 99);
}

export function average(values) {
  const sum = values.reduce((a, b) => a + b, 0);
  return round2(sum / values.length);
}
