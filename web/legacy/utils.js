/** Clamp a number into a range. */
export function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

export default function round2(value) {
  return Math.round(value * 100) / 100;
}
